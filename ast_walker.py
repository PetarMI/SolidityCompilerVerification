import json
import ast_parser as ap
import sys

contract_dir = "contracts/"
ast_extension = ".json"
test_file = "WhiteList"

def import_ast(ast_file):
    """Takes the .json produced by Truffle and extracts just the ast"""
    json_data = json.load(open(contract_dir + ast_file + ast_extension))
    ast = json_data["ast"]
    return ast

def find_contract_defs(ast):
    """ Find all contracts inside an ast file.

        Returns:
        contracts: [ { "name" : <contract_name>,
                       "contents" : [<statements in contract>] } ]
    """
    all_nodes = ast["nodes"]
    contracts = []

    for node in all_nodes:
        contract = {}
        
        if (node["nodeType"] == "ContractDefinition"):
            contract["name"] = node["name"]
            contract_statements = node.get("nodes", None)

            if (contract_statements):
                contract["contents"] = contract_statements
                contracts.append(contract)

    return contracts

def find_contract_funcs(contract):
    """ Find all functions in the contract.
        Return a list of the sort:
        [ {
            "name" : "<name>"
            "params" : list of variables as parsed by parse_variable in ast_parser
            "return_type" : "<return type>"    
          }, ...
        ] 
    """
    functions = []

    for node in contract:
        if (node["nodeType"] == "FunctionDefinition"):

            # check if it can be used within contract
            if (node.get("visibility", None) == "external"):
                continue
            
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

def parse_contracts(contracts):
    """ Parse all contracts in the .sol file 
        
        @param: result from find_contract_defs

        Returns:
            all_blocks A flat list of all blocks found in the .sol file
            { "if" : <if_stat>,
              "scope_vars" : <variable in scope for that if node>,
              "funcs : <list of available functions to use"
              "func_name" : <name of the function we are currently in> }
    """
    all_blocks = []

    for contract in contracts:
        contract_contents = contract["contents"]

        # find functions and blocks (if statements) in a particular contract
        contract_funcs = find_contract_funcs(contract_contents)
        contract_blocks = parse_contract_aux(contract_contents, [], "")

        # add the lost of available functions to each block
        for block in contract_blocks:
            funcs_no_rec = [f for f in contract_funcs if f["name"] != block["func_name"]]
            block["funcs"] = funcs_no_rec

        contract_blocks = ap.preprocess_blocks(contract_blocks)
        all_blocks.extend(contract_blocks)

    return all_blocks

# TODO this may use some refactoring cause it's ugly
def parse_contract_aux(contract, visible_vars, func_name):
    """ Find all if blocks in the contract

    @param: contract All nodes in the contract
    @param: visible_vars The visible vars at this level
    @param: func_name What function we are in right now
    
    @returns: list of blocks of the type
              { "if" : <if_stat>,
                "scope_vars" : <variable in scope for that if node>,
                "func_name" : <name of the function we are currently in> }
    """
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

            # note we are inside a certain function
            func_name = node["name"]

            # keep searching inside the body of the function
            func_body_blocks = parse_contract_aux(find_nested_nodes(node, "func"), func_vars, func_name)
            if (func_body_blocks):
                blocks.extend(func_body_blocks)
        if (node["nodeType"] == "VariableDeclaration" or node["nodeType"] == "VariableDeclarationStatement"):
            var_node = ap.extract_var(node)
            scope_vars.extend(find_vars([var_node]))
        # check the bodies of all if statements
        elif (node["nodeType"] == "IfStatement"):
            # create a new block consisting of if statement, the visible vars and more nested blocks
            block = {"if" : node, "scope_vars" : copy_vars(scope_vars), "func_name" : func_name}
            blocks.append(block)

            if_body_blocks = parse_contract_aux(find_nested_nodes(node, "if"), scope_vars, func_name)
            if (if_body_blocks):
                blocks.extend(if_body_blocks)

            else_body_blocks = parse_contract_aux(find_nested_nodes(node, "else"), scope_vars, func_name)
            if (else_body_blocks):
                blocks.extend(else_body_blocks)
        elif (node["nodeType"] == "ForStatement"):
            # add the looping var and pass it as in-scope in the body of the for
            init_node = node.get("initializationExpression", None)
            if (init_node):
                init_var = ap.extract_var(init_node)
                # make the init variable visible only in the for loop body
                for_vars = copy_vars(scope_vars)
                for_vars.extend(find_vars([init_var]))

            for_body_blocks = parse_contract_aux(find_nested_nodes(node, "for"), for_vars, func_name)
            if (for_body_blocks):
                blocks.extend(for_body_blocks)
        elif (node["nodeType"] == "Return"):
            block = {"return" : node, "scope_vars" : copy_vars(scope_vars), "func_name" : func_name}
            blocks.append(block)

    return blocks

def find_nested_nodes(node, node_type):
    nodes = []

    """ Auxiliary function to return a list of statements inside a node 
        supported nodes are 
        - function bodies
        - if and else bodies
        - for loop bodies
    """
    if (node_type == "func" or node_type == "for"):
        func_body = node.get("body", None)

        if(func_body):
            nodes.extend(func_body.get("statements", []))

    elif (node_type == "if"):
        if_body = node.get("trueBody", None)
        
        if(if_body != None):
            nodes.extend(if_body.get("statements", []))

    elif (node_type == "else"):
        else_body = node.get("falseBody", None)
        
        if(else_body != None):
            nodes.extend(else_body.get("statements", []))
    
    return nodes

def find_vars(nodes):
    """ Parses VariableDeclaration nodes to format all vars into a dictionary """
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
    print ("Total of {0} blocks".format(len(blocks)))

    for block in blocks:
        if (block.get("if", None)):
            stat = "If"
        else:
            stat = "Return"
        print("{0} statement in function: {1}:".format(stat, block["func_name"]))
        print("Available variables:")
        for k, v in block["scope_vars"].items():
            sys.stdout.write(k + " : ")
            for var in v:
                sys.stdout.write(var["name"] + ", ")
            print()
        print("Available functions:")
        for f in block["funcs"]:
            sys.stdout.write(f["name"] + ", ")
        print("\n")

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

def pretty_print_contracts(contracts):
    print("Contracts:")
    for contract in contracts:
        print(contract["name"])

    print("")

def run_ast_walker(ast_file):
    """ 
        @param: ast_file Just the base name of the ast we are exploring 
        
        Returns: 
            blocks A flat list of all blocks in the .sol file
    """
    ast = import_ast(ast_file)
    contracts = find_contract_defs(ast)

    pretty_print_contracts(contracts)

    blocks = parse_contracts(contracts)
    
    #pretty_print_blocks(blocks)
   
    return blocks
    
# run_ast_walker(test_file)
