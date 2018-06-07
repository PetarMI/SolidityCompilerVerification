import ast_walker
import mutator
import ineq_gen
import tautology_generator
import dead_generator
import ast_parser as ap

contract_file = "WhiteList"
expr_depth = 3

blocks = ast_walker.run_ast_walker(contract_file)
ast_walker.pretty_print_blocks(blocks)

def run_gen_sep(): 
    if_blocks = ap.get_specific_blocks(blocks, "if")
    print("Tautologies for {0} if statements".format(len(if_blocks)))
    for b in if_blocks:
        expr = tautology_generator.run_generator(b, expr_depth)
        #print(expr)

def run_code_gen_sep():
    return_blocks = ap.get_specific_blocks(blocks, "return")
    print("Dead code for {0} return statements".format(len(return_blocks)))
    for b in return_blocks:
        expr = dead_generator.run_generator(b, 2)
        print(expr)

#run_gen_sep()
#print()
#run_code_gen_sep()

mutator.run_mutator(contract_file, blocks, expr_depth)

