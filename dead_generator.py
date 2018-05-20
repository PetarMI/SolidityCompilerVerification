import random
import tautology_generator as t_gen

class Dead_Generator():

    structs = [ "if({0}) {{ \n\t{1}\n}}",
                "while({0}) {{ \n\t{1}\n}}" ]

    def __init__(self, scope_vars, functions, expr_depth):
        self.variables = scope_vars
        self.functions = functions
        self.depth = expr_depth

    def gen_dead_block(self):
        """ The main function of the dead code generator

            Returns:
                a string to directly place into the contract 
        """
        if_cond = self.get_condition()

        dead_code = random.choice(self.structs).format(if_cond, "throw;")

        return dead_code    

    def get_condition(self):
        """ Generate a false statement to insert in the if/while condition block
            Call the external module Tautology_Generator for that
        """
        tg = t_gen.Tautology_Generator(self.variables, self.functions, self.depth)
        cond = tg.gen_condition(False)

        return cond

def run_generator(contract_vars, functions, depth):
    dc_gen = Dead_Generator(contract_vars, functions, depth)
    expr = dc_gen.gen_dead_block()

    return expr