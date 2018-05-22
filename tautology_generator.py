import random 
import leaf_generator as leaf_gen

class Tautology_Generator():

    not_probability = 0.2

    true_variants = [{"left_expr" : True, "predicate" : " && ", "right_expr" : True}, 
                     {"left_expr" : True, "predicate" : " || ", "right_expr" : True},
                     {"left_expr" : True, "predicate" : " || ", "right_expr" : False},
                     {"left_expr" : False, "predicate" : " || ", "right_expr" : True}]

    false_variants = [{"left_expr" : True, "predicate" : " && ", "right_expr" : False}, 
                      {"left_expr" : False, "predicate" : " && ", "right_expr" : True},
                      {"left_expr" : False, "predicate" : " && ", "right_expr" : False},
                      {"left_expr" : False, "predicate" : " || ", "right_expr" : False}]

    def __init__(self, block, expr_depth):
        self.variables = block["scope_vars"]
        self.functions = block["funcs"]
        self.depth = expr_depth

    def gen_tautology(self):
        expr = ""

        # pick whether the outermost predicate is a logical AND or OR
        if(decision(0.5)):
            expr = " && " + self.gen_expr(True, self.depth)
        else:
            expr = " || " + self.gen_expr(False, self.depth)

        return expr

    def gen_condition(self, bvalue):
        """ Generate a false expresson which will be inserted in a
            dead if/while block """
        expr = self.gen_expr(bvalue, self.depth)
        return expr

    def gen_expr(self, bvalue, depth):
        expr = ""

        # we reached the max depth - return a leaf
        if(depth < 1 or decision(0.9)):
            return self.gen_leaf(bvalue)

        depth -= 1

        #check what the final value of the expression should be
        if(bvalue):
            expr = self.gen_true(depth)
        else:
            expr = self.gen_false(depth)

        return expr

    def gen_true(self, depth):
        if (decision(self.not_probability)):
            true_expr = random.choice(self.true_variants)
            expr = self.gen_expr(
                true_expr["left_expr"], depth) + true_expr["predicate"] + self.gen_expr(true_expr["right_expr"], depth)
            return "(" + expr + ")"
        else:
            false_expr = self.gen_false(depth - 1)
            return " (!" + false_expr + ")"

    def gen_false(self, depth):
        if (decision(self.not_probability)):
            false_expr = random.choice(self.false_variants)
            expr = self.gen_expr(
                false_expr["left_expr"], depth) + false_expr["predicate"] + self.gen_expr(false_expr["right_expr"], depth)
            return "(" + expr + ")"
        else:
            true_expr = self.gen_true(depth - 1)
            return " (!" + true_expr + ")"

    def gen_leaf(self, bvalue):
        # pick the leaf type based on available vars and functions
        leaf_T, T_atoms = leaf_gen.pick_leaf(self.variables, self.functions)

        #TODO may need different approach
        if (T_atoms):
            atoms = []
            leaf_expr, var_slots = leaf_gen.get_leaf_skeleton(leaf_T, bvalue)

            for i in range(var_slots):
                atoms.append(random.choice(T_atoms))

            return "(" + leaf_expr.format(*atoms) + ")"
        else:
            return get_literal(bvalue)

def decision(prob):
    """generate something wih a certain probability"""
    return (random.random() > prob)

def get_literal(bvalue) -> str:
    if(bvalue):
        return "true"
    else:
        return "false"

def run_generator(block, depth):
    t_gen = Tautology_Generator(block, depth)
    expr = t_gen.gen_tautology()

    return expr
