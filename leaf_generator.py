import random

all_leaves = { "bool" : { True : ["{0} || true", "true || {0}"],
                          False : ["{0} && false", "false && {0}"] } }

def get_leaf(leaf_T, bvalue):
    leaves = all_leaves.get(leaf_T, None)

    # sanity check
    if (not leaves):
        raise ValueError("No leaves of the following type")

    leaf_expr = random.choice(leaves[bvalue])

    return leaf_expr