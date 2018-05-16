import random
import ineq_gen

all_leaves = { "bool" : { True : ["{0} || true", "true || {0}"],
                          False : ["{0} && false", "false && {0}"] } }

def get_leaf(leaf_T, bvalue):
    leaves = all_leaves.get(leaf_T, None)

    if leaf_T == "uint" or leaf_T == "int":
        leaves = ineq_gen.run_generator(True, bvalue)
    # sanity check
    if (not leaves):
        raise ValueError("No leaves of the following type")

    leaf_expr = random.choice(leaves[bvalue])

    return leaf_expr