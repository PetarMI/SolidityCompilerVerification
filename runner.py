import ast_walker
import mutator
import ineq_gen
import tautology_generator

contract_file = "coin_test"

sources = ast_walker.run_ast_walker(contract_file)
mutator.do_mutation(contract_file, sources)

print("Running inequality generator. OUTPUT:")
ineq_gen.run_generator()

print("\nRunning boolean generator. OUTPUT:")
tautology_generator.run_generator()