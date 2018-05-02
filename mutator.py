import random
import tautology_generator as t_gen

contract_dir = "contracts/"
mutants_dir = contract_dir + "mutants/"
contract_extension = ".sol"

def mutate(seed_contract, sources, n):
    mutated = False
    mutated_contract = ""
    seed_path = contract_dir + seed_contract + contract_extension

    with open(seed_path) as f:
        for src in sources:
            offset = src[0]
            length = src[1]
            
            pointer = f.tell()
            block = f.read(offset + length - pointer)
            mutated_contract += block
            
            if (decision()):
                mutated_contract += (gen_tautology())
                mutated = True
        
        #read rest of file
        mutated_contract += f.read()

    if (mutated):
        write_mutant(mutated_contract, seed_contract, n)
        return True
    else:
        return False

def write_mutant(mutant, seed_contract, n):
    mutant_name = mutants_dir + seed_contract + str(n) + contract_extension

    with open(mutant_name, 'w') as f:
        f.write(mutant)

def gen_tautology():
    """External function
    Generate the tautology we will insert in the if condition"""
    return tgen.gen_tautology()

def decision():
    """mutate every line with 66% probability"""
    return random.random() > 0.33

def do_mutation(seed_contract, sources):
    mutants = 0

    while (mutants < 3):
        if(mutate(seed_contract, sources, mutants)):
            mutants += 1
