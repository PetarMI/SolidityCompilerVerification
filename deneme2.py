import random
import operator

symbols_str = ['<', '>', '>=', '<=']
symbols = {"<": (lambda x, y: x < y), ">": (lambda x, y: x > y), ">=": (lambda x, y: x >= y),
           "<=": (lambda x, y: x <= y)}
ops_str = ['+', '-', '/', '*']
expr = ""
nums = []

for i in range(10):
    nums.append(random.uniform(-100, 100))
l = len(nums)

def decision(prob):
    """generate something wih a certain probability"""
    return (random.random() > prob)


def gen_tautology(bool, tot_depth, expr):
    tot_depth -= 1
    depth = random.randint(1, 3)

    if (bool):
        expr += " and " + " ( " + gen_inequality(bool, depth) + " ) "
    else:
        expr += " or " + " ( " + gen_inequality(bool, depth) + " ) "

    if tot_depth > 0:
        expr += gen_tautology(bool, tot_depth, expr)
        return expr
    else:
        #print(eval("True" + expr))
        return "" #gen_inequality(bool, depth)


def gen_eq():
    '''generate an equation using one of the ops'''
    eq = ""
    eq_depth = random.randint(1, 3)
    first = 1

    while eq_depth > 0:
        eq_depth -= 1
        num1 = nums[random.randint(0, l - 1)]
        num2 = nums[random.randint(0, l - 1)]

        if first:
            eq += str(num1) + " " + ops_str[random.randint(0, 3)] + " " + str(num2)
            first -= 1
        else:
            eq += " " + ops_str[random.randint(0, 3)] + " " + str(num1) + " " + ops_str[
                random.randint(0, 3)] + " " + str(num2)
    val = eval(eq)
    return eq, val


def gen_inequality(bool, depth):
    expr = []

    while depth > 0:
        depth -= 1
        eq1, val_eq1 = gen_eq()
        eq2, val_eq2 = gen_eq()
        symbol = symbols_str[random.randint(0, 3)]
        res = symbols[symbol](val_eq1, val_eq2)
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

def main():
    gen_tautology(True, 4, "")
    print(eval("True" + expr))

if __name__ == "__main__":
    main()