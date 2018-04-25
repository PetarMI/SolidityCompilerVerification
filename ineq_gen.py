import random

class Ineq_Generator():
    # Class to generate random inequalities

    def __init__(self,symbols_str, symbols, ops_str, nums, nums_length):
        self.symbols_str = symbols_str
        self.symbols = symbols
        self.ops_str=  ops_str
        self.nums = nums
        self.nums_length = nums_length

    def gen_tautology(self, bool, tot_depth, expr):
        '''recursively generates tautology consisting of inequalities'''
        tot_depth -= 1
        depth = random.randint(1, 3)

        if (bool):
            expr += " and " + " ( " + self.gen_inequality(bool, depth) + " ) "
        else:
            expr += " or " + " ( " + self.gen_inequality(bool, depth) + " ) "

        if tot_depth > 0:
            expr += self.gen_tautology(bool, tot_depth, expr)
            return expr
        else:
            return ""


    def gen_eq(self):
        '''generate an equation using one of the ops'''
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


    def gen_inequality(self, bool, depth):
        '''generates the inequality itself'''
        while depth > 0:
            depth -= 1
            eq1, val_eq1 = self.gen_eq()
            eq2, val_eq2 = self.gen_eq()
            symbol = self.symbols_str[random.randint(0, 3)]
            res = self.symbols[symbol](val_eq1, val_eq2)
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


def decision(prob):
        """generate something wih a certain probability"""
        return (random.random() > prob)

def run_generator():
    symbols_str = ['<', '>', '>=', '<=']
    symbols = {"<": (lambda x, y: x < y), ">": (lambda x, y: x > y), ">=": (lambda x, y: x >= y), "<=": (lambda x, y: x <= y)}
    ops_str = ['+', '-', '/', '*']
    nums = []
    for i in range(10):
        nums.append(random.uniform(-100, 100))
    l = len(nums)

    generator  = Ineq_Generator(symbols_str, symbols, ops_str, nums, l)
    if decision(0.5):
        expr = generator.gen_tautology(True, 4, "")
        print(expr)
        print(eval("True" + expr))
    else:
        expr = generator.gen_tautology(False, 4, "")
        print(expr)
        print(eval("False" + expr))
