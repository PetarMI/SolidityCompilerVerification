
""" This is a script containing fucntions used only by the ast_walker
    The point is simply to parse statements (ifs, variables, etc) that the walker finds
    and put them in a format in which we can do the mutations later on """

# TODO add support for floats and all uint types
supported_types = {
  "t_bool" : "bool",
  "t_uint256" : "uint",
  "t_int256" : "int",
  "t_string_storage" : "string",
  "t_string_storage_ptr" : "string",
  "t_string_memory_ptr" : "string",
  "t_address" : "address",
  "t_mapping" : "mapping",
  "t_array" : "array"
}

simple_types = ["bool", "int", "uint", "string", "address"]

type_codes = {
    "bool" : "{type} {name}",
    "int" : "{type} {name}",
    "uint" : "{type} {name}",
    "string" : "{type} {name}",
    "address" : "{type} {name}",
    "array" : "{key_type}[] memory {name}",
    "mapping" : "{type} ({key_type} => {val_type}) {name}"
}

#TODO sort them
def get_source(block):
    """ Get the source of a code block

        @param: block The if statement whose source we want 
        @param: part Indicator of whether we want the condition or the end of the if statement

        Returns: 
            { "offset" : x,
              "length" : y }
    """
    raw_src = ""

    if (block.get("if", None)):
        raw_src = block["if"]["condition"]["src"]
    elif (block.get("return", None)): 
        raw_src = block["return"]["src"]
    else:
        raise KeyError("Asking for the source of unknown contract block")

    split_source = raw_src.split(":")
    
    return {"offset" : int(split_source[0]), 
            "length" : int(split_source[1]) }

def extract_var(node):
    """ Get the VariableDeclaration out of a node """
    if (node["nodeType"] == "VariableDeclarationStatement"):
        for var_decl in node["declarations"]:
            if(var_decl["nodeType"] == "VariableDeclaration"):
                return var_decl
    else:
        return node

def parse_variable(var):
    """ Parse a variable declaration node to a dictionary structure
    Example: { "name" : name,
               "type" : type,
               "key_type"  : key_type
               "val_type" : val_type }
    In case of an array treat key_type as the type of the elements
    """
    var_info = {}   
    var_info["name"] = var["name"]

    # get the variable type
    raw_base_type = var["typeDescriptions"]["typeIdentifier"].split("$")[0]
    base_type = infer_type(raw_base_type)

    if (base_type != None):
        var_info["type"] = base_type
    else:
        return None

    composite_types = parse_composite_types(var, base_type)
    if (composite_types != None):
        for k, v in composite_types.items():
            var_info[k] = v
    else: 
        return None

    return var_info

def preprocess_blocks(blocks):
    """ For each block separate its scope variables into types """
    for block in blocks:
        scope_vars = preprocess_vars(block["scope_vars"])
        block["scope_vars"] = scope_vars

    return blocks

def preprocess_vars(flat_vars):
    """ Function to take a flat list of vars 
        and return variables divided into types
        Returns: dictionary with types as keys and lists of vars as values
    """
    proc_vars = {}

    for var in flat_vars:
        v_type = var["type"]
        if (v_type not in proc_vars):
            proc_vars[v_type] = [var]
        else:
            proc_vars[v_type].append(var)

    return proc_vars

# TODO doesn't work with nested types
def parse_composite_types(var, var_type):
    """ Parse the composite types of arrays and mappings 
    Params: 
        The variable node
        The variable base type inferred beforehand"""
    var_info = {}

    if (var_type == "array"):
        # walk the tree to find the necessary info for an array declaration node
        raw_inner_type = var["typeName"]["baseType"]["typeDescriptions"]["typeIdentifier"]
        inner_type = infer_type(raw_inner_type)

        if (inner_type != None):
            var_info["key_type"] = inner_type
        else:
            return None

    elif (var_type == "mapping"):
        # walk the tree to find the necessary info for a mapping declaration node
        raw_key_type = var["typeName"]["keyType"]["typeDescriptions"]["typeIdentifier"]
        raw_val_type = var["typeName"]["valueType"]["typeDescriptions"]["typeIdentifier"]

        key_type = infer_type(raw_key_type)
        val_type = infer_type(raw_val_type)

        if (key_type != None and var_type != None):
            var_info["key_type"] = key_type
            var_info["val_type"] = val_type
        else:
            return None

    return var_info

def get_specific_blocks(blocks, bl_type):
    """ Dirty fucntion used only for testing purposes in runner 
        Return only the if/return blocks
    """
    specific_blocks = []

    for b in blocks:
        if (b.get(bl_type, None)):
            specific_blocks.append(b)

    return specific_blocks

def infer_type(raw_type):
    return supported_types.get(raw_type, None)

def var_to_string(var):
    """ Return the string representation of the dictionary format of a variable 

        @param var: dictionary format of a variable as returned by parse_variable(var)

        Returns:
            code: String format of the var
    """

    var_code = type_codes.get(var.get("type", None), None)

    if (not var_code):
        raise ValueError("Cannot convert variable to string")

    code = var_code.format(**var)

    return code
