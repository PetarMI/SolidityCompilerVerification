import random 

class Tautology_Generator():

    not_probability = 0.2

    leafs = { True : ["{0} or True", "True or {0}"],
              False : ["{0} and False", "False and {0}"] }

    true_variants = [{"left_expr" : True, "predicate" : " and ", "right_expr" : True}, 
                     {"left_expr" : True, "predicate" : " or ", "right_expr" : True},
                     {"left_expr" : True, "predicate" : " or ", "right_expr" : False},
                     {"left_expr" : False, "predicate" : " or ", "right_expr" : True}]

    false_variants = [{"left_expr" : True, "predicate" : " and ", "right_expr" : False}, 
                      {"left_expr" : False, "predicate" : " and ", "right_expr" : True},
                      {"left_expr" : False, "predicate" : " and ", "right_expr" : False},
                      {"left_expr" : False, "predicate" : " or ", "right_expr" : False}]

    def __init__(self, scope_vars, expr_depth):
        self.variables = scope_vars
        self.depth = expr_depth

    def gen_tautology(self):
        expr = ""

        # pick whether the outermost predicate is a logical AND or OR
        if(decision(0.5)):
            expr = " and " + self.gen_expr(True, self.depth)
        else:
            expr = " or " + self.gen_expr(False, self.depth)

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
            return " (not " + false_expr + ")"

    def gen_false(self, depth):
        if (decision(self.not_probability)):
            false_expr = random.choice(self.false_variants)
            expr = self.gen_expr(
                false_expr["left_expr"], depth) + false_expr["predicate"] + self.gen_expr(false_expr["right_expr"], depth)
            return "(" + expr + ")"
        else:
            true_expr = self.gen_true(depth - 1)
            return " (not " + true_expr + ")"

    def gen_leaf(self, bvalue):
        if (decision(0.75)):
            return str(bvalue)
        else:
            leaf_expr = random.choice(self.leafs[bvalue])
            var = random.choice(self.variables["bool"])["name"]
            return "(" + leaf_expr.format(var) + ")" # leaf_expr.format(var)

def decision(prob):
    """generate something wih a certain probability"""
    return (random.random() > prob)

def run_generator(contract_vars, depth):
    #do_tests()
    t_gen = Tautology_Generator(contract_vars, depth)
    expr = t_gen.gen_tautology()
    print(expr)
    # print(eval(expr[4:]))
