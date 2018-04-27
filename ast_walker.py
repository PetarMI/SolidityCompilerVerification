import json

contract_dir = "contracts/"
ast_extension = ".json"
test_file = "coin_test"

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

    return parse_sources(sources)

#TODO sort them
def parse_sources(sources):
    """Return each source as a pair of offset and block length"""
    parsed_sources = []

    for src in sources:
        split_source = src.split(":")
        parsed_sources.append([int(split_source[0]), int(split_source[1])])

    return parsed_sources

def run_ast_walker(ast_file):
    """Parameter: Just the base name of the ast we are exploring"""
    ast = import_ast(ast_file)
    contract = find_contract_defs(ast)
    functions = find_contract_funcs(contract)
    if_statements = find_ifs(functions)
    sources = get_sources(if_statements)

    print(sources)
    return sources

# run_ast_walker()