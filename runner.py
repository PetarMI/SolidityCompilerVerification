import ast_walker
import mutator
import ineq_gen
import tautology_generator

contract_file = "Coin"
expr_depth = 3

if_sources, all_vars = ast_walker.run_ast_walker(contract_file)
print("Finding if statements:")
print(if_sources)

print("\nFinding variables: ")
ast_walker.pretty_print_vars(all_vars)

print("\nRunning inequality generator. OUTPUT:")
#ineq_gen.run_generator()

print("\nRunning boolean generator. OUTPUT:")
tautology_generator.run_generator(all_vars, expr_depth)

mutator.run_mutator(contract_file, if_sources, all_vars, expr_depth)