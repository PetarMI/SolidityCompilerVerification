import random
import tautology_generator as t_gen

class Mutator():

    def __init__(self, seed_contract, sources, scope_vars, expr_depth):
        self.seed_contract = seed_contract
        self.sources = sources
        self.tgen = t_gen.Tautology_Generator(scope_vars, expr_depth)

        self.contract_dir = "contracts/"
        self.mutants_dir = self.contract_dir + "mutants/"
        self.contract_extension = ".sol"
        self.seed_path = self.contract_dir +self.seed_contract + self.contract_extension

    def mutate(self, n):
        mutated = False
        mutated_contract = ""

        with open(self.seed_path) as f:
            for src in self.sources:
                offset = src[0]
                length = src[1]
                
                pointer = f.tell()
                block = f.read(offset + length - pointer)
                mutated_contract += block
                
                if (decision()):
                    mutated_contract += (self.gen_tautology())
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

    def gen_tautology(self):
        """External function
        Generate the tautology we will insert in the if condition"""
        return self.tgen.gen_tautology()

    def do_mutation(self):
        mutants = 0

        while (mutants < 3):
            if(self.mutate(mutants)):
                mutants += 1

def decision():
    """mutate every line with 66% probability"""
    return random.random() > 0.33

def run_mutator(seed_contract, if_stats, contract_vars, depth):
    mutator = Mutator(seed_contract, if_stats, contract_vars, depth)
    mutator.do_mutation()
