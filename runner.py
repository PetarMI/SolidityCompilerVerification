import contract
import mutator
import ineq_gen
import tautology_generator

sources = contract.run_contract()
mutator.do_mutation(sources)
ineq_gen.run_generator()