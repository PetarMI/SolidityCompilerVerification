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

def if_extractor(stmnt):
    ifs_list = []
    if stmnt["trueBody"] != None and "statements" in stmnt["trueBody"].keys():
        for inside_true in stmnt["trueBody"]["statements"]:
            if inside_true["nodeType"] == "IfStatement":
                ifs_list.append(inside_true)
                ifs_list = ifs_list + if_extractor(inside_true)

    if stmnt["falseBody"] != None and "statements" in stmnt["falseBody"].keys():
        for inside_false in stmnt["falseBody"]["statements"]:
            if inside_false["nodeType"] == "IfStatement":
                ifs_list.append(inside_false)
                ifs_list = ifs_list + if_extractor(inside_false)

    return ifs_list

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
                if_statements[func_name] = if_statements[func_name] + if_extractor(statement)
    return if_statements

def get_sources(statements):
    sources = []

    for func, ifstats in statements.items():
        for ifstat in ifstats:
            # condition is an attibute of the ast -> get the condition of the if statement
            sources.append(ifstat["condition"]["src"])

    return ap.parse_sources(sources)

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
    # pretty_print_vars(g_vars)

    return if_sources, g_vars

