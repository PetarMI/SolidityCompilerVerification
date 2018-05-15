import json
import ast_parser as ap
import sys

contract_dir = "contracts/"
ast_extension = ".json"
test_file = "Coin"

def import_ast(ast_file):
    """Takes the .json produced by Truffle and extracts just the ast"""
    json_data = json.load(open(contract_dir + ast_file + ast_extension))
    ast = json_data["ast"]
    return ast

def find_contract_defs(ast):
    """Find all statements inside a contract.

    Raises:
    ValueError if there is nothing in the contract
    """
    all_nodes = ast["nodes"]

    for node in all_nodes:
        if (node["nodeType"] == "ContractDefinition"):
            contract_contents = node.get("nodes", None)
            break

    if (contract_contents != None):
        return contract_contents
    else:
        raise ValueError("Empty contract provided.")

def find_contract_funcs(contract):
    """ Find all functions in the contract.
        Return a list of the sort:
        [ {
            "f_name" : "<name>"
            "params" : list of variables as parsed by parse_variable in ast_parser
            "return_type" : "<return type>"    
          }, ...
        ] 
    """
    functions = []

    for node in contract:
        if (node["nodeType"] == "FunctionDefinition"):
            function = {}
            function["name"] = node["name"]
            
            #find parameters
            parameter_nodes = node["parameters"].get("parameters", [])
            parameters = find_vars(parameter_nodes)
            function["params"] = parameters

            #find return type
            return_nodes = node["returnParameters"].get("parameters", [])
            return_parameters = find_vars(return_nodes)
            function["ret_params"] = return_parameters

            functions.append(function)

    return functions

def parse_contract(contract):
    return parse_contract_aux(contract, [])

def parse_contract_aux(contract, visible_vars):
    blocks = []

    scope_vars = copy_vars(visible_vars)

    for node in contract:
        # check the bodies of all functions
        if (node["nodeType"] == "FunctionDefinition"):
            # add function parameters as inscope variables
            parameter_nodes = node["parameters"].get("parameters", [])
            # hide the function parameters from the rest of the functions
            func_vars = copy_vars(scope_vars)
            func_vars.extend(find_vars(parameter_nodes))
            # keep searching inside the body of the function
            func_body_blocks = parse_contract_aux(find_nested_nodes(node), func_vars)
            if (func_body_blocks):
                blocks.extend(func_body_blocks)
        if (node["nodeType"] == "VariableDeclaration" or node["nodeType"] == "VariableDeclarationStatement"):
            var_node = ap.extract_var(node)
            scope_vars.extend(find_vars([var_node]))
        # check the bodies of all if statements
        elif (node["nodeType"] == "IfStatement"):
            # create a new block consisting of if statement, the visible vars and more nested blocks
            block = {"if" : node, "scope_vars" : copy_vars(scope_vars)}
            blocks.append(block)

            # TODO add trueBody to find_nested_nodes
            if_body_blocks = parse_contract_aux(find_nested_nodes(node), scope_vars)
            if (if_body_blocks):
                blocks.extend(if_body_blocks)

    return blocks

def find_nested_nodes(node):
    nodes = []

    """ Just return a list of statements inside a node 
        supported nodes are 
        - function bodies
        - nested variable declarations 
        - TODO else statement bodies
        - TODO For loops
    """
    func_body = node.get("body", None)
    infunc_var = node.get("declarations", None)
    if_body = node.get("trueBody", None)

    if(func_body != None):
        nodes.extend(func_body.get("statements", []))
    elif(infunc_var != None):
        nodes.extend(infunc_var)
    elif(if_body != None):
        nodes.extend(if_body.get("statements", []))
    
    return nodes

def find_vars(nodes):
    """ Extracts the variable from the node and parses it """
    variables = []

    for var_node in nodes:
        var = ap.parse_variable(var_node)
        # did we recognize the type
        if(var != None):
            variables.append(var)

    return variables

def copy_vars(variables):
    scope_vars = []

    for v in variables:
        scope_vars.append(v)

    return scope_vars

def pretty_print_blocks(blocks):
    for block in blocks:
        print(block["if"]["src"])
        for k, v in block["scope_vars"].items():
            sys.stdout.write(k + " : ")
            for var in v:
                sys.stdout.write(var["name"] + ", ")
            print()
        print()

def pretty_print_functions(functions):
    for func in functions:
        print("Function name: {0}".format(func["name"]))
        sys.stdout.write("Parameters: ")
        for param in func["params"]:
            sys.stdout.write(param["type"] + ", ")
        print()
        sys.stdout.write("Return parameters: ")
        for return_param in func["ret_params"]:
            sys.stdout.write(return_param["type"] + ", ")
        print()

def run_ast_walker(ast_file):
    """Parameter: Just the base name of the ast we are exploring"""
    ast = import_ast(ast_file)
    contract = find_contract_defs(ast)

    functions = find_contract_funcs(contract)

    blocks = parse_contract(contract)
    blocks = ap.preprocess_blocks(blocks)
    
    # pretty_print_blocks(blocks)
    # pretty_print_functions(functions)

    return blocks, functions
    
run_ast_walker(test_file)
