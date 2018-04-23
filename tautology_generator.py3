import random 

depth = 3

gen_true = [{"left_expr" : True, "predicate" : " and ", "right_expr" : True}, 
            {"left_expr" : True, "predicate" : " or ", "right_expr" : True},
            {"left_expr" : True, "predicate" : " or ", "right_expr" : False},
            {"left_expr" : False, "predicate" : " or ", "right_expr" : True}]

gen_false = [{"left_expr" : True, "predicate" : " and ", "right_expr" : False}, 
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
        #generate true
        true_expr = random.choice(gen_true)
        expr = gen_expr(true_expr["left_expr"], depth) + true_expr["predicate"] + gen_expr(true_expr["right_expr"], depth)
    else:
        # generate false
        false_expr = random.choice(gen_false)
        expr = gen_expr(false_expr["left_expr"], depth) + false_expr["predicate"] + gen_expr(false_expr["right_expr"], depth)

    return "(" + expr + ")"

def decision(prob):
    """generate something wih a certain probability"""
    return (random.random() > prob)

def do_tests():
    true_pass = True
    false_pass = True

    print("Testing true statements")
    for i in range(500):
        expr = gen_expr(True, 10)
        res = eval(expr)

        if(res == False):
            print ("Error in False at {0}".format(i))
            true_pass = False

    if(true_pass):
        print ("All true tests passed")
    else: 
        print ("True tests NOT passed")

    print("Testing true statements")
    for i in range(500):
        expr = gen_expr(False, 10)
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
    print(gen_tautology())

if __name__ == "__main__":
    main()
