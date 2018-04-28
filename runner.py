import ast_walker
import mutator
import ineq_gen
import tautology_generator

contract_file = "Coin"

if_sources, global_vars = ast_walker.run_ast_walker(contract_file)
print("Finding if statements:")
print(if_sources)

print("\nFinding global variables: ")
ast_walker.pretty_print_vars(global_vars)

mutator.do_mutation(contract_file, if_sources)

print("\nRunning inequality generator. OUTPUT:")
#ineq_gen.run_generator()

print("\nRunning boolean generator. OUTPUT:")
tautology_generator.run_generator()