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

def parse_contract(contract):
    return parse_contract_aux(contract, [])

def parse_contract_aux(contract, visible_vars):
    blocks = []

    scope_vars = copy_vars(visible_vars)

    for node in contract:
        # check the bodies of all functions
        if (node["nodeType"] == "FunctionDefinition"):
            # keep searching inside the body of the function
            func_body_blocks = parse_contract_aux(find_nested_nodes(node), scope_vars)
            if (func_body_blocks):
                blocks.extend(func_body_blocks)
        # used for global variables
        if (node["nodeType"] == "VariableDeclaration"):
            var = ap.parse_variable(node)
            # did we recognize the type
            if(var != None):
                scope_vars.append(var)
        # used for local variable declarations
        elif (node["nodeType"] == "VariableDeclarationStatement"):
            # just add the variable to the list of in-scope variables
            var_node = ap.extract_var(node)
            var = ap.parse_variable(var_node)
            # did we recognize the type
            if(var != None):
                scope_vars.append(var)
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

    """supported nodes are 
        - function bodies
        - nested variable declarations 
        - TODO if statement bodies
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

def run_ast_walker(ast_file):
    """Parameter: Just the base name of the ast we are exploring"""
    ast = import_ast(ast_file)
    contract = find_contract_defs(ast)

    blocks = parse_contract(contract)
    blocks = ap.preprocess_blocks(blocks)
    
    # pretty_print_blocks(blocks)

    return blocks
    
run_ast_walker(test_file)
