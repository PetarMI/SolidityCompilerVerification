import json

def import_ast():
    """Takes the .json produced by Truffle and extracts just the ast""" 
    json_data = json.load(open("contracts/Token.json"))
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
            sources.append(ifstat["condition"]["src"])

    return sources

def main():
    ast = import_ast()
    contract = find_contract_defs(ast)
    functions = find_contract_funcs(contract)
    if_statements = find_ifs(functions)
    sources = get_sources(if_statements)

    print(sources)

if __name__ == "__main__":
    main()