import random
import ineq_gen
import function_caller as fc

# leaf_types = ["bool", "int", "uint", "string", "array"]#, "mapping"]
leaf_types = ["bool"]#, "string", "array"]#, "mapping"]

all_leaves = {  "bool" : { 
                    True : ["{0} || true", "true || {0}"],
                    False : ["{0} && false", "false && {0}"] 
                },
                "string" : { 
                    True : ["keccak256({0}) == keccak256({0})"],
                    False : ["keccak256({0}) != keccak256({0})"]
                },
                "array" : {
                    True : ["int({0}.length) > -1", "-1 < int({0}.length)"],
                    False : ["int({0}.length) < -1", "-1 > int({0}.length)"]
                } }

def get_leaf_skeleton(leaf_T, bvalue):
    """ Return a sekeleton for a leaf expression

        @param leaf_T The type of variables to be used in that leaf
        @param bvalue The boolean value of the expression
    
        Returns
            expr The skeleton of the expression with placeholders for the atoms
            var_slots How many variables should be inserted in the expression
    """
    leaves = all_leaves.get(leaf_T, None)

    if leaf_T == "uint" or leaf_T == "int":
        expr, var_slots = ineq_gen.run_generator(True, bvalue)
        return expr, var_slots

    # sanity check
    if (not leaves):
        raise ValueError("No leaves of the following type")
    
    leaf_expr = random.choice(leaves[bvalue])

    return leaf_expr, 1

def pick_leaf(variables, functions):
    """ Pick a type of variable used in leaf based on available vars
        
        @param variables The available variables for the leaf
        @param functions The available functions for the leaf

        Returns
            leaf_T: The type of variable to be used in the leaf
            T_atoms: Atoms available to be used 
    """
    leaf_T = None

    # TODO may need different approach
    for i in range(1, 10):
        leaf_T = random.choice(leaf_types)
        # get all variables of this type (list comprehesnion to get just the names)
        available_vars = variables.get(leaf_T, None)

        T_vars = []
        if (available_vars):
            T_vars = [v["name"] for v in available_vars]            

        # get all functions of this type 
        T_funcs = fc.prep_functions(functions, leaf_T, variables)
        # combine variables and functions that we can insert into leaves
        T_atoms = list(set().union(T_vars, T_funcs))
        # do we have any variables or functions we could use in a leaf of that type
        if (T_atoms):
            return leaf_T, T_atoms

    return leaf_T, None