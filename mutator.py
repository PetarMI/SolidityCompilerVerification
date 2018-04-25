import random

def mutate(fname, sources, n):
    mutated = False
    mutated_contract = ""

    with open(fname) as f:
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
        write_mutant(mutated_contract, n)
        return True
    else:
        return False

def write_mutant(mutant, n):
    mutant_name = "contracts/mutants/coin_test{0}.sol".format(n)

    with open(mutant_name, 'w') as f:
        f.write(mutant)

def gen_tautology():
    """the simplest tautology"""
    return " && (1 == 1)"

def decision():
    """mutate every line with 66% probability"""
    return random.random() > 0.33

#TODO sort them
def parse_sources(sources):
    parsed_sources = []

    for src in sources:
        split_source = src.split(":")
        parsed_sources.append([int(split_source[0]), int(split_source[1])])

    return parsed_sources

def main():
    #hardcoding the lines we got from contract.py for now
    sources = parse_sources(["553:20:0", "698:29:0"])
    mutants = 0

    while (mutants < 3):
        if(mutate("contracts/coin_test.sol", sources, mutants)):
            mutants += 1

if __name__ == "__main__":
    main()