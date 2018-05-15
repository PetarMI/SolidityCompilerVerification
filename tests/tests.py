import sys
sys.path.insert(0,'..')
import tautology_generator as t_gen
import random as rand

booleans = ["True", "False"]
var = {'bool': [{'name': 'bvar', 'type': 'bool'}]}

def do_tests():
    true_pass = True
    false_pass = True
    num_expr = 500
    depth = 10

    tgen = t_gen.Tautology_Generator(var, [], depth)

    print("Testing true statements")
    for i in range(num_expr):
        expr = parse_solidity_expr(tgen.gen_expr(True, depth))
        res = eval(expr)

        if(res == False):
            print ("Error in True at {0}".format(i))
            true_pass = False

    if(true_pass):
        print ("All true tests passed")
    else: 
        print ("True tests NOT passed")

    print("Testing false statements")
    for i in range(num_expr):
        expr = parse_solidity_expr(tgen.gen_expr(False, depth))
        res = eval(expr)

        if(res != False):
            print ("Error in False at {0}".format(i))
            false_pass = False

    if(false_pass):
        print ("All false tests passed")
    else: 
        print ("False tests NOT passed")

def parse_solidity_expr(expr):
    # This is very crude
    expr = expr.replace("||", "or")
    expr = expr.replace("&&", "and")
    expr = expr.replace("!", "not")
    expr = expr.replace("true", "True")
    expr = expr.replace("false", "False")
    expr = expr.replace("bvar", rand.choice(booleans))
    return expr

do_tests()