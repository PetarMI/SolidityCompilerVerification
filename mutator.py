import random
import tautology_generator as t_gen
import dead_generator as dc_gen
import ast_parser as aparse
import operator

class Mutator():

    def __init__(self, seed_contract, blocks, expr_depth):
        self.blocks = blocks
        self.expr_depth = expr_depth
        # path stuff
        self.contract_dir = "contracts/"
        self.mutants_dir = self.contract_dir + "mutants/"
        self.contract_extension = ".sol"
        self.seed_contract = seed_contract
        self.seed_path = self.contract_dir + self.seed_contract + self.contract_extension

    def mutate(self, n):
        mutated_contract = ""

        mutations = self.prepare_mutations(self.blocks)

        with open(self.seed_path) as f:
            for mutation in mutations:
                # extract the mutated code and where it should be written
                code = mutation["code"]
                offset = mutation["offset"]
                pointer = f.tell()
                code_block = f.read(offset - pointer)
                mutated_contract += code_block
                mutated_contract += code

            #read rest of file
            mutated_contract += f.read()
            print(mutated_contract)

        self.write_mutant(mutated_contract, n)

    def write_mutant(self, mutant, n):
        mutant_name = self.mutants_dir + self.seed_contract + str(n) + self.contract_extension

        with open(mutant_name, 'w') as f:
            f.write(mutant)

    def prepare_mutations(self, blocks):
        """ Prepare all mutations for insertion in the code 
            @param: blocks All if statements to be mutated 

            Returns:
                list of mutation dicts
                [ { "code" : <mutation_string>,
                    "offset" : x } ]
        """
        mutations = []

        for block in blocks:
            code = ""
            offset = 0
            src = aparse.get_source(block)

            # do we change the if condition or insert dead code
            if (block.get("if", None)):
                # generate a tautology for this if statement condition
                if(decision()):
                    #Switch statement order
                    code = t_gen.run_generator(block, self.expr_depth, True)
                    offset = src["offset"]
                else:
                    #Do not switch statement order
                    code = t_gen.run_generator(block, self.expr_depth, False)
                    offset = src["offset"] + src["length"]
            else:
                # generate a tautology for this if statement condition
                code = dc_gen.run_generator(block, self.expr_depth)
                offset = src["offset"]

            mutation = { "code" : code,
                         "offset" : offset }

            mutations.append(mutation)

        return self.sort_mutations(mutations)

    def sort_mutations(self, mutations):
        """ Sort the mutations by their offset """
        return sorted(mutations, key=operator.itemgetter("offset"))

    def do_mutation(self):
        mutants = 0

        while (mutants < 3):
            self.mutate(mutants)
            mutants += 1

def decision():
    """mutate every line with 66% probability"""
    return random.random() > 0.5

def run_mutator(seed_contract, blocks, depth):
    mutator = Mutator(seed_contract, blocks, depth)
    mutator.do_mutation()
