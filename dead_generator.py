import random
import tautology_generator as t_gen

class Dead_Generator():

    structs = [ "\nif({0}) {{ \n\t\t// *** Generated *** \n\t{1}\n}}",
                "\nwhile({0}) {{ \n\t\t// *** Generated *** \n\t{1}\n}}" ]

    def __init__(self, block, expr_depth):
        self.block = block
        self.variables = self.block["scope_vars"]
        self.functions = self.block["funcs"]
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
        tg = t_gen.Tautology_Generator(self.block, self.depth)
        cond = tg.gen_condition(False)

        return cond

def run_generator(block, depth):
    dc_gen = Dead_Generator(block, depth)
    expr = dc_gen.gen_dead_block()

    return expr