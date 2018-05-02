import json
import ast_parser as ap

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
    """Find all functions in the contract.

    Raises:
    ValueError if there are no functions in the contract
    """
    functions = []

    for node in contract:
        if (node["nodeType"] == "FunctionDefinition"):
            functions.append(node)

    if (len(functions) > 0):
        return functions
    else:
        raise ValueError("No functions in contract.")

def find_global_vars(contract):
    vars = []

    for node in contract:
        if (node["nodeType"] == "VariableDeclaration"):
            var = ap.parse_variable(node)
            # did we recognize the type
            if(var != None):
                vars.append(var)

    return vars

def find_local_vars(statements):
    vars = []

    for statement in statements:
        if(statement["nodeType"] == "VariableDeclarationStatement"):
            # this is weird - the ast has a list of declarations
            declarations = statement["declarations"]
            for d in declarations:
                # do the same as in find_global_vars
                if (d["nodeType"] == "VariableDeclaration"):
                    var = ap.parse_variable(d)
                    # did we recognize the type
                    if(var != None):
                        vars.append(var)
        else: 
            nested_vars = find_local_vars(find_nested_statements(statement))
            if (nested_vars):
                vars.extend(nested_vars)

    return vars;

def find_ifs(functions):
    """Find all if statements inside a contract.

    Returns:
    A dictionary of function names to a list of if statements.
    """
    if_statements = {}

    for func in functions:
        func_name = func["name"]
        func_body = func["body"]["statements"]
        if_statements[func_name] = []

        for statement in func_body:
            if (statement["nodeType"] == "IfStatement"):
                if_statements[func_name].append(statement)

    return if_statements

def get_sources(statements):
    sources = []

    for func, ifstats in statements.items():
        for ifstat in ifstats:
            # condition is an attibute of the ast -> get the condition of the if statement
            sources.append(ifstat["condition"]["src"])

    return ap.parse_sources(sources)

# TODO nested statements of If-else bodies
def find_nested_statements(node):
    node_body = node.get("body", None)

    # does the statement have a body
    if(node_body != None):
        return node_body.get("statements", [])

    return []

def pretty_print_vars(vars):
    for var in vars:
        for k, v in var.items():
            if(k == "name"):
                print(k + " " + v)
            else:
                print("\t" + k + " " + v)

def run_ast_walker(ast_file):
    """Parameter: Just the base name of the ast we are exploring"""
    ast = import_ast(ast_file)
    contract = find_contract_defs(ast)
    functions = find_contract_funcs(contract)
    if_statements = find_ifs(functions)
    if_sources = get_sources(if_statements)

    g_vars = find_global_vars(contract)
    l_vars = find_local_vars(functions)
    #pretty_print_vars(l_vars)
    print(l_vars)
    return if_sources, g_vars

run_ast_walker(test_file)