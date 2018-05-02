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

def find_vars(contract):
    return ap.preprocess_vars(find_vars_aux(contract))

def find_vars_aux(contract):
    all_vars = []

    for node in contract:
        if (node["nodeType"] == "VariableDeclaration"):
            var = ap.parse_variable(node)
            # did we recognize the type
            if(var != None):
                all_vars.append(var)
        else: 
            nested_vars = find_vars_aux(find_nested_nodes(node))
            if (nested_vars):
                all_vars.extend(nested_vars)

    return all_vars;

def get_sources(statements):
    sources = []

    for func, ifstats in statements.items():
        for ifstat in ifstats:
            # condition is an attibute of the ast -> get the condition of the if statement
            sources.append(ifstat["condition"]["src"])

    return ap.parse_sources(sources)

def find_nested_nodes(node):
    nodes = []

    """supported nodes are 
        - function bodies
        - nested variable declarations 
        - TODO if statement bodies
    """
    func_body = node.get("body", None)
    infunc_var = node.get("declarations", None)

    if(func_body != None):
        nodes.extend(func_body.get("statements", []))
    elif(infunc_var != None):
        nodes.extend(infunc_var)
    
    return nodes

def pretty_print_vars(vars):
    for k, v in vars.items():
        print(k)
        for var in v:
            print("\t" + var["name"])

def run_ast_walker(ast_file):
    """Parameter: Just the base name of the ast we are exploring"""
    ast = import_ast(ast_file)
    contract = find_contract_defs(ast)
    functions = find_contract_funcs(contract)
    if_statements = find_ifs(functions)
    if_sources = get_sources(if_statements)

    all_vars = find_vars(contract)
    # pretty_print_vars(all_vars)

    #print(if_sources)
    return if_sources, all_vars

run_ast_walker(test_file)
