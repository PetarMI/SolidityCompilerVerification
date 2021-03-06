""" Deprecated code from ast_walker.py """

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

# dead code generator
def gen_code(self, block):
    """ Generate either a tautology or dead code block to insert into contract
        Uses external modules tautology_generator or dead_generator 
        
        @param: block The if statement we are mutating

        Returns:
            code : string containing the code block
    """
    if(block.get("if"), None):
        """ External function to generate the tautology we will insert in the if condition """
        code = t_gen.run_generator(block, self.expr_depth)
    elif (block.get("return")):
        code = dc_gen.run_generator(block, self.expr_depth)
    else:
        raise KeyError("Attempting to generate unknown block in Mutator")

    return code