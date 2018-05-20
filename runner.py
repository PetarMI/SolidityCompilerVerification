import ast_walker
import mutator
import ineq_gen
import tautology_generator
import dead_generator

contract_file = "WhiteList"
expr_depth = 3

blocks = ast_walker.run_ast_walker(contract_file)
ast_walker.pretty_print_blocks(blocks)

"""print("\nRunning inequality generator. OUTPUT:")
in_eq,var_eq = ineq_gen.run_generator(blocks, True)
print(in_eq)
print("=======================================================================================================================================")
print("With vars:")
print(var_eq)"""

def run_gen_sep(): 
    print("\nRunning boolean generator. OUTPUT:")
    for b in blocks:
        expr = tautology_generator.run_generator(b, expr_depth)
        print(expr)

def run_code_gen_sep():
    for b in blocks:
        expr = dead_generator.run_generator(b, 2)
        print(expr)

"""run_gen_sep()
print()
run_code_gen_sep()"""

mutator.run_mutator(contract_file, blocks, expr_depth)

