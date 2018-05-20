import random
import tautology_generator as t_gen
import dead_generator as dc_gen
import ast_parser as aparse
import operator

class Mutator():

    def __init__(self, seed_contract, blocks, functions, expr_depth):
        self.blocks = blocks
        self.functions = functions
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
                print(offset)
                pointer = f.tell()
                code_block = f.read(offset - pointer)
                mutated_contract += code_block
                mutated_contract += code
            
            #read rest of file
            mutated_contract += f.read()

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
                    "src" : { "offset" : x,
                              "length" : y} } } ]
        """
        mutations = []

        for block in blocks:
            src = []
            code = ""
            mutation = {}

            # do we change the if condition or insert dead code
            if (decision()):
                src = aparse.get_source(block, "condition")
                # generate a tautology for this if statement condition
                code = (self.gen_code(block, "tautology"))
            else:
                src = aparse.get_source(block, "body")
                # generate a tautology for this if statement condition
                code = (self.gen_code(block, "dead code"))
            
            offset = src["offset"] + src["length"]
            mutation = { "code" : code,
                         "offset" : offset }

            mutations.append(mutation)

        return self.sort_mutations(mutations)

    def gen_code(self, block, stat_type):
        """ Generate either a tautology or dead code block to insert into contract
            Uses external modules tautology_generator or dead_generator 
            
            @param: block The if statement we are mutating
            @param: stat_type Indicating if we want a tautology inside condition or a dead block after

            Returns:
                code : string containing the code block
        """
        scope_vars = block.get("scope_vars", [])
        func_name = block.get("func_name", "")

        # remove a function from list of available functions to avoid recursion
        funcs_no_rec = [f for f in self.functions if f["name"] != func_name]

        if(stat_type == "tautology"):
            """ External function to generate the tautology we will insert in the if condition """
            code = t_gen.run_generator(scope_vars, funcs_no_rec, self.expr_depth)
        elif (stat_type == "dead code"):
            code = dc_gen.run_generator(scope_vars, funcs_no_rec, self.expr_depth)
        else:
            raise KeyError("Attempting to generate unknown block in Mutator")

        return code

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

def run_mutator(seed_contract, blocks, functions, depth):
    mutator = Mutator(seed_contract, blocks, functions, depth)
    mutator.do_mutation()
