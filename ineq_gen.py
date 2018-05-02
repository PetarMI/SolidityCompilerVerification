import random

class Ineq_Generator():
    # Class to generate random inequalities

    def __init__(self,symbols_str, symbols, ops_str, nums, nums_length, vars, type):
        self.symbols_str = symbols_str
        self.symbols = symbols
        self.ops_str=  ops_str
        self.nums = nums
        self.nums_length = nums_length
        self.vars = vars
        self.type = type

    def gen_eq(self):
        '''generate an equation using one of the ops'''
        if self.type is "integers":
            eq = ""
            eq_depth = random.randint(1, 3)
            first = 1

            while eq_depth > 0:
                eq_depth -= 1
                num1 = self.nums[random.randint(0, self.nums_length - 1)]
                num2 = self.nums[random.randint(0, self.nums_length - 1)]

                if first:
                    eq += str(num1) + " " + self.ops_str[random.randint(0, 3)] + " " + str(num2)
                    first -= 1
                else:
                    eq += " " + self.ops_str[random.randint(0, 3)] + " " + str(num1) + " " + self.ops_str[
                        random.randint(0, 3)] + " " + str(num2)
            val = eval(eq)
            return eq, val
        else:
            vars = []
            for var in self.vars['uint']:
                vars.append(var['name'])
            return vars

    def gen_inequality(self, bool, depth):
        '''generates the inequality itself'''
        while depth > 0:
            depth -= 1
            length_sym = len(self.symbols_str)
            symbol = self.symbols_str[random.randint(0, length_sym-1)]

            if self.type == "integers":
                eq1, val_eq1 = self.gen_eq()
                eq2, val_eq2 = self.gen_eq()
                res = self.symbols[symbol](val_eq1, val_eq2)
            else:
                vars = self.gen_eq()
                eq1 = vars[random.randint(0, len(vars)-1)]
                eq2 = eq1
                res = decision(0.5)

            if bool:
                if res:
                    return eq1 + " " + symbol + " " + eq2
                else:
                    return eq2 + " " + symbol + " " + eq1
            else:
                if res:
                    return eq2 + " " + symbol + " " + eq1
                else:
                    return eq1 + " " + symbol + " " + eq2

    def gen_tautology(self, bool, tot_depth, expr):
        '''recursively generates tautology consisting of inequalities'''
        tot_depth -= 1
        depth = random.randint(1, 3)

        if self.type == "integers":
            if (decision(0.5)):
                expr += " and " + " ( " + self.gen_inequality(bool, depth) + " ) "
            else:
                expr += " or " + " ( " + self.gen_inequality(bool, depth) + " ) "
        else:
            if (bool):
                if (decision(0.5)):
                    expr += " and " + " ( " + self.gen_inequality(bool, depth) + " ) "
                else:
                    expr += " or " + " ( " + self.gen_inequality(bool, depth) + " ) "
            else:
                if (decision(0.5)):
                    expr += " and " + "not ( " + self.gen_inequality(bool, depth) + " ) "
                else:
                    expr += " or " + "not ( " + self.gen_inequality(bool, depth) + " ) "
        if tot_depth > 0:
            expr += self.gen_tautology(bool, tot_depth, expr)
            return expr
        else:
            return ""


def decision(prob):
        """generate something wih a certain probability"""
        return (random.random() > prob)

def run_generator(vars):
    symbols_str_int = ['<', '>', '>=', '<=']
    symbols_str_var = ['==', '>=', '<=']

    symbols = {"<": (lambda x, y: x < y), ">": (lambda x, y: x > y), ">=": (lambda x, y: x >= y), "<=": (lambda x, y: x <= y)}
    ops_str = ['+', '-', '/', '*']
    nums = []
    for i in range(10):
        nums.append(random.randint(-10000, 10000))
    l = len(nums)

    generatorInt  = Ineq_Generator(symbols_str_int, symbols, ops_str, nums, l, vars, "integers")
    generatorVar  = Ineq_Generator(symbols_str_var, symbols, ops_str, nums, l, vars, "variables")

    if decision(0.5):
        intExpr = generatorInt.gen_tautology(True, 4, "")
    else:
        intExpr = generatorInt.gen_tautology(False, 4, "")

    if decision(0.5):
        varExprs = generatorVar.gen_tautology(True, 4, "")
    else:
        varExprs = generatorVar.gen_tautology(False, 4, "")


    return intExpr, varExprs