import random

class Ineq_Generator():
    # Class to generate random inequalities

    def __init__(self,symbols_str_int, symbols_str_var, symbols, ops_str, nums, nums_length, variabs):
        self.symbols_str_int = symbols_str_int
        self.symbols_str_var = symbols_str_var
        self.symbols = symbols
        self.ops_str=  ops_str
        self.nums = nums
        self.nums_length = nums_length
        self.variabs = variabs

    def gen_eq(self, type):
        '''generate an equation using one of the ops'''
        if type is "integers":
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
            variables = []

            for variable in self.variabs['uint']:
                variables.append(variable['name'])
            return variables

    def gen_inequality(self, args):
        bool = args[0]
        depth = args[3]
        type = args[4]

        '''generates the inequality itself'''
        while depth > 0:
            depth -= 1

            if type == "integers":
                length_sym = len(self.symbols_str_int)
                symbol = self.symbols_str_int[random.randint(0, length_sym-1)]
            else:
                length_sym = len(self.symbols_str_var)
                symbol = self.symbols_str_var[random.randint(0, length_sym - 1)]

            if type == "integers":
                eq1, val_eq1 = self.gen_eq(type)
                eq2, val_eq2 = self.gen_eq(type)
                res = self.symbols[symbol](val_eq1, val_eq2)
            else:
                variabs = self.gen_eq(type)
                eq1 = variabs[random.randint(0, len(variabs)-1)]
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

    def gen_tautology(self, args):
        bool = args[0]
        args[1] -=  1
        tot_depth = args[1]
        expr = args[2]
        curr_type = args[4]
        depth = random.randint(1, 3)
        args[3] = depth
        func_list = [self.gen_tautology, self.gen_inequality]
        pred_list = [" and ", " or "]
        types = ["integers", "variables"]

        if "uint" in self.variabs.keys():
            args[4] = random.choice(types)
        else:
            args[4] = "integers"

        if tot_depth < 1 :
            return self.gen_inequality(args)

        if curr_type == "integers":
            retExpr = "(" + "(" + random.choice(func_list)(args) + ")" +  random.choice(pred_list) +  "(" + random.choice(func_list)(args) + ")" + ")"
        else:
            if (bool):
                retExpr = "(" + "(" +random.choice(func_list)(args) + ")" + random.choice(pred_list) + "(" + random.choice(func_list)(args) + ")" + ")"
            else:
                retExpr = "not (" + "(" + random.choice(func_list)(args) + ")" + random.choice(pred_list) + "(" + random.choice(func_list)(args) + ")" + ")"

        return retExpr

def decision(prob):
        """generate something wih a certain probability"""
        return (random.random() > prob)

def run_generator(variabs):
    symbols_str_int = ['<', '>', '>=', '<=']
    symbols_str_var = ['==', '>=', '<=']
    types = ["integers", "variables"]
    symbols = {"<": (lambda x, y: x < y), ">": (lambda x, y: x > y), ">=": (lambda x, y: x >= y), "<=": (lambda x, y: x <= y)}
    ops_str = ['+', '-', '/', '*']
    nums = []

    if "uint" in variabs.keys():
        type = random.choice(types)
    else:
        type = "integers"

    for i in range(10):
        nums.append(random.randint(-10000, 10000))
    l = len(nums)

    generatorInt  = Ineq_Generator(symbols_str_int,symbols_str_var, symbols, ops_str, nums, l, variabs)

    if decision(0.5):
        intExpr = generatorInt.gen_tautology([True, 4, "", 1, type])
        intExpr = "and " + intExpr
    else:
        intExpr = generatorInt.gen_tautology([False, 4, "", 1, type])
        intExpr = "or " + intExpr

    return intExpr