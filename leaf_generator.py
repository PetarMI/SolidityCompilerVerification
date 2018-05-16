import random
import function_caller as fc

leaf_types = ["bool"]#, "int", "string", "array", "mapping"]

all_leaves = { "bool" : { True : ["{0} || true", "true || {0}"],
                          False : ["{0} && false", "false && {0}"] } }

def get_leaf_skeleton(leaf_T, bvalue):
    leaves = all_leaves.get(leaf_T, None)

    # sanity check
    if (not leaves):
        raise ValueError("No leaves of the following type")

    leaf_expr = random.choice(leaves[bvalue])

    return leaf_expr

def pick_leaf(variables, functions):
    leaf_T = None

    for i in range(1, 10):
        leaf_T = random.choice(leaf_types)
        # get all variables of this type (list comprehesnion to get just the names)
        T_vars = [v["name"] for v in variables.get(leaf_T, None)]
        # get all functions of this type 
        T_funcs = fc.prep_functions(functions, leaf_T, variables)
        # combine variables and functions that we can insert into leaves
        T_atoms = list(set().union(T_vars, T_funcs))
        # do we have any variables or functions we could use in a leaf of that type
        if (T_atoms):
            return leaf_T, T_atoms

    return leaf_T, None