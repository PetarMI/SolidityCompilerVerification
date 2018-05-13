import random

def prep_functions(funcs, ret_type, scope_vars):
    """ Prepare all functions for calls in the code at a certain point """
    functions = []

    for func in funcs:
        # check if the function has the required return type
        if (not check_return_type(func, ret_type)):
            continue
        func_call = call_function(func, scope_vars)        
        if (func_call):
            functions.append(func_call)

    return functions

def call_function(func, scope_vars):
    # go parameter by parameter and try to find a variable to pass as argument

    func_call = "{0}(".format(func["name"])

    # check if function takes 0 params
    if (len(func["params"]) == 0):
        return func_call + ")"

    for param in func["params"]:
        all_vars = scope_vars.get(param["type"], [])
        matching_vars = []

        for var in all_vars:
            if (match_argument(param, var)):
                matching_vars.append(var)

        # get an argument to pass or a literal
        arg = get_arg(matching_vars, param["type"])
        # if no appropraite argument, we drop this function as callable
        if(not arg):
            return None

        func_call += "{0}, ".format(arg)

    func_call = func_call[:-2]
    func_call += ")"

    return func_call

def get_arg(matching_vars, arg_type):
    if (matching_vars):
        var = random.choice(matching_vars)
        return var["name"]
    elif (arg_type == "int"):
        return str(random.randint(-200, 200))
    elif (arg_type == "uint"):
        return str(random.randint(0, 200))
    elif (arg_type == "bool"):
        return str(random.choice([True, False]))
    else:
        return None

def check_return_type(func, ret_type):
    f_ret_types = func["ret_params"]
    
    # Only support functions of 1 return type for now
    if (len(f_ret_types) == 1 and f_ret_types[0] == ret_type):
        return True
    else:
        return False

def match_argument(param, var):
    """ Special check for arrays and mappings """
    p_key = param.get("key_type", None)
    v_key = var.get("key_type", None)
    p_val = param.get("val_type", None)
    v_val = var.get("val_type", None)

    if (p_key == v_key and p_val == v_val):
        return True
    else:
        return False

"""def get_function_by_type(functions, ret_type)
    functions = []

    for func in functions:
        if (func[ret_params] == ret_type):
            functions.append(func)

    return functions"""
