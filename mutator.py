import random
import tautology_generator as t_gen
import ast_parser as aparse

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
        mutated = False
        mutated_contract = ""

        with open(self.seed_path) as f:
            for block in self.blocks:
                src = aparse.get_source(block)
                offset = src[0]
                length = src[1]

                pointer = f.tell()
                code_block = f.read(offset + length - pointer)
                mutated_contract += code_block
                
                if (decision()):
                    mutated_contract += (self.gen_tautology(block["scope_vars"]))
                    mutated = True
            
            #read rest of file
            mutated_contract += f.read()

        if (mutated):
            self.write_mutant(mutated_contract, n)
            return True
        else:
            return False

    def write_mutant(self, mutant, n):
        mutant_name = self.mutants_dir + self.seed_contract + str(n) + self.contract_extension

        with open(mutant_name, 'w') as f:
            f.write(mutant)

    def gen_tautology(self, scope_vars):
        """External function
        Generate the tautology we will insert in the if condition"""
        return t_gen.run_generator(scope_vars, self.expr_depth)

    def do_mutation(self):
        mutants = 0

        while (mutants < 3):
            if(self.mutate(mutants)):
                mutants += 1

def decision():
    """mutate every line with 66% probability"""
    return random.random() > 0.33

def run_mutator(seed_contract, blocks, depth):
    mutator = Mutator(seed_contract, blocks, depth)
    mutator.do_mutation()
