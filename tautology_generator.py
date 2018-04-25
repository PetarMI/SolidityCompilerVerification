import random 

depth = 3
not_probability = 0.2

true_variants = [{"left_expr" : True, "predicate" : " and ", "right_expr" : True}, 
                 {"left_expr" : True, "predicate" : " or ", "right_expr" : True},
                 {"left_expr" : True, "predicate" : " or ", "right_expr" : False},
                 {"left_expr" : False, "predicate" : " or ", "right_expr" : True}]

false_variants = [{"left_expr" : True, "predicate" : " and ", "right_expr" : False}, 
                  {"left_expr" : False, "predicate" : " and ", "right_expr" : True},
                  {"left_expr" : False, "predicate" : " and ", "right_expr" : False},
                  {"left_expr" : False, "predicate" : " or ", "right_expr" : False}]

def gen_tautology():
    expr = ""

    # pick whether the outermost predicate is a logical AND or OR
    if(decision(0.5)):
        expr = " and " + gen_expr(True, depth)
    else:
        expr = " or " + gen_expr(False, depth)

    return expr

def gen_expr(bvalue, depth):
    expr = ""

    if(depth < 1 or decision(0.9)):
        return str(bvalue)

    depth -= 1

    #check what the final value of the expression should be
    if(bvalue):
        expr = gen_true(depth)
    else:
        expr = gen_false(depth)

    return expr

def gen_true(depth):
    if (decision(not_probability)):
        true_expr = random.choice(true_variants)
        expr = gen_expr(true_expr["left_expr"], depth) + true_expr["predicate"] + gen_expr(true_expr["right_expr"], depth)
        return "(" + expr + ")"
    else:
        false_expr = gen_false(depth - 1)
        return " (not " + false_expr + ")"

def gen_false(depth):
    if (decision(not_probability)):
        false_expr = random.choice(false_variants)
        expr = gen_expr(false_expr["left_expr"], depth) + false_expr["predicate"] + gen_expr(false_expr["right_expr"], depth)
        return "(" + expr + ")"
    else:
        true_expr = gen_true(depth - 1)
        return " (not " + true_expr + ")"

def decision(prob):
    """generate something wih a certain probability"""
    return (random.random() > prob)

def do_tests():
    true_pass = True
    false_pass = True
    num_expr = 500
    depth = 10

    print("Testing true statements")
    for i in range(num_expr):
        expr = gen_expr(True, depth)
        res = eval(expr)

        if(res == False):
            print ("Error in True at {0}".format(i))
            true_pass = False

    if(true_pass):
        print ("All true tests passed")
    else: 
        print ("True tests NOT passed")

    print("Testing true statements")
    for i in range(num_expr):
        expr = gen_expr(False, depth)
        res = eval(expr)

        if(res != False):
            print ("Error in False at {0}".format(i))
            false_pass = False

    if(false_pass):
        print ("All false tests passed")
    else: 
        print ("False tests NOT passed")


def main():
    #do_tests()
    expr = gen_tautology();
    print(expr)
    # print(eval(expr))

if __name__ == "__main__":
    main()