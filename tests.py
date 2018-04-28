import tautology_generator as tgen

def do_tests():
    true_pass = True
    false_pass = True
    num_expr = 500
    depth = 10

    print("Testing true statements")
    for i in range(num_expr):
        expr = tgen.gen_expr(True, depth)
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
        expr = tgen.gen_expr(False, depth)
        res = eval(expr)

        if(res != False):
            print ("Error in False at {0}".format(i))
            false_pass = False

    if(false_pass):
        print ("All false tests passed")
    else: 
        print ("False tests NOT passed")

do_tests()