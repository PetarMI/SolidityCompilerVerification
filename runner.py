import ast_walker
import mutator
import ineq_gen
import tautology_generator

contract_file = "Coin"
expr_depth = 3

blocks, functions = ast_walker.run_ast_walker(contract_file)

print("\nFinding variables: ")
ast_walker.pretty_print_blocks(blocks)

print("\nFinding functions: ")
ast_walker.pretty_print_functions(functions)

"""print("\nRunning inequality generator. OUTPUT:")
in_eq,var_eq = ineq_gen.run_generator(all_vars)
print(in_eq)
print("=======================================================================================================================================")
print("With vars:")
print(var_eq)"""

print("\nRunning boolean generator. OUTPUT:")
for b in blocks:
	scope_vars = b["scope_vars"]
	print("if statement")
	expr = tautology_generator.run_generator(scope_vars, functions, expr_depth)
	print(expr)

# mutator.run_mutator(contract_file, blocks, expr_depth)