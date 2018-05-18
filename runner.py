import ast_walker
import mutator
import ineq_gen
import tautology_generator

contract_file = "Coin"
expr_depth = 3

blocks, functions = ast_walker.run_ast_walker(contract_file)
    
print("\nFinding variables: ")
print("{0} if statements".format(len(blocks)))
ast_walker.pretty_print_blocks(blocks)

print("\nFinding functions: ")
ast_walker.pretty_print_functions(functions)

"""print("\nRunning inequality generator. OUTPUT:")
in_eq,var_eq = ineq_gen.run_generator(blocks, True)
print(in_eq)
print("=======================================================================================================================================")
print("With vars:")
print(var_eq)"""

def run_gen_sep(): 
    print("\nRunning boolean generator. OUTPUT:")
    for b in blocks:
        scope_vars = b["scope_vars"]
        funcs_no_rec = [f for f in functions if f["name"] != b["func_name"]]
        print("if statement in function {0}".format(b["func_name"]))
        expr = tautology_generator.run_generator(scope_vars, funcs_no_rec, expr_depth)
        print(expr)

run_gen_sep()

mutator.run_mutator(contract_file, blocks, functions, expr_depth)

