import random

class Ineq_Generator():
    # Class to generate random inequalities

    def __init__(self,symbols_str_int, symbols, ops_str, nums, nums_length, variabs, placeholderVal):
        self.symbols_str_int = symbols_str_int
        self.symbols = symbols
        self.ops_str=  ops_str
        self.nums = nums
        self.nums_length = nums_length
        self.variabs = variabs
        self.placeholderVar = placeholderVal

    def gen_eq(self, type):
        '''generate an equation using one of the ops'''
        if type is "integers":
            eq = ""
            eq_depth = random.randint(1, 2)
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

            #if ("uint" in self.variabs.keys()):
             #   for variable in self.variabs['uint']:
              #      variables.append(variable['name'])
            #if ("int" in self.variabs.keys()):
             #   for variable in self.variabs['int']:
              #      variables.append(variable['name'])
            temp = self.placeholderVar
            self.placeholderVar += 1
            retVal = "{" + str(temp) + "}"
            return [retVal]

    def gen_inequality(self, args):
        bool = args[0]
        depth = args[3]
        type = args[4]

        '''generates the inequality itself'''
        while depth > 0:
            depth -= 1

            if type == "integers":
                symbols_str = self.symbols_str_int[0:3]
                length_sym = len(symbols_str)
                symbol = symbols_str[random.randint(0, length_sym-1)]
            else:
                if bool:
                    symbols_str = self.symbols_str_int[2:4]
                else:
                    symbols_str = self.symbols_str_int[0:1]

                length_sym = len(symbols_str)
                symbol = symbols_str[random.randint(0, length_sym - 1)]

            if type == "integers":
                eq1, val_eq1 = self.gen_eq(type)
                eq2, val_eq2 = self.gen_eq(type)
                res = self.symbols[symbol](val_eq1, val_eq2)
            else:
                variabs = self.gen_eq(type)
                eq1 = variabs[random.randint(0, len(variabs)-1)]
                eq2 = eq1
                res = bool

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

    def var_with_expression(self, args):
        vars = []
        eq1, val1 = self.gen_eq("integers")
        eq2, val2 = self.gen_eq("integers")
        bool = args[0]
        #print(self.variabs.keys())
        #if ("uint" in self.variabs.keys()):
         #   for variable in self.variabs['uint']:
          #      vars.append(variable['name'])
        #if ("int" in self.variabs.keys()):
         #   for variable in self.variabs['int']:
          #      vars.append(variable['name'])

        var = "{" + str(self.placeholderVar) + "}"
        self.placeholderVar += 1
            #random.choice(vars)

        if bool:
            op = random.choice(self.ops_str)
            retExpr = "(" + var + " " + op + " (" + eq1 + ") == " + var + " " + op + " (" + eq1 + "))"
        else:
            op = random.choice(self.ops_str)
            retExpr = "(" + var + " " + op + " (" + eq1 + ") == " + var + " " + op + " (" + eq2 + "))"

        return retExpr


    def gen_tautology(self, args):
        bool = args[0]
        args[1] -=  1
        tot_depth = args[1]
        expr = args[2]
        curr_type = args[4]
        depth = random.randint(1, 3)
        args[3] = depth
        #if all (k in self.variabs.keys() for k in ("uint","int")):
        if self.variabs:
            func_list = [self.gen_tautology, self.gen_inequality, self.var_with_expression]
        else:
            func_list = [self.gen_tautology, self.gen_inequality]

        pred_list = [" && ", " || "]
        types = ["integers", "variables"]

        #if ("uint" in self.variabs.keys() or "int" in self.variabs.keys()) :
        if self.variabs:
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
                    retExpr = "(" + "(" + random.choice(func_list)(args) + ")" + random.choice(pred_list) + "(" + random.choice(func_list)(args) + ")" + ")"

        return retExpr

def decision(prob):
        """generate something wih a certain probability"""
        return (random.random() > prob)

def run_generator(varExists, bool):
    symbols_str_int = ['<', '>', '>=', '<=', '==']
    types = ["integers", "variables"]
    symbols = {"<": (lambda x, y: x < y), ">": (lambda x, y: x > y), ">=": (lambda x, y: x >= y), "<=": (lambda x, y: x <= y)}
    ops_str = ['+', '-', '/', '*']
    nums = []
    #bool = decision(0.5)



    for i in range(10):
        nums.append(random.randint(-100000, 100000))
    l = len(nums)

    generatorInt  = Ineq_Generator(symbols_str_int, symbols, ops_str, nums, l, varExists, 0)

    if (varExists) :
        type = random.choice(types)
        #expr_var = generatorInt.var_with_expression(bool)
        #print(expr_var)
    else:
        type = "integers"


    if bool:
        intExpr = generatorInt.gen_tautology([True, 2, "", 1, type])
        #intExpr = "and " + intExpr
    else:
        intExpr = generatorInt.gen_tautology([False, 2, "", 1, type])
        #intExpr = "or " + intExpr

    return intExpr, generatorInt.placeholderVar # expr_var