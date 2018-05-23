import random
import string
import tautology_generator as t_gen
import ast_parser
import copy

class Dead_Generator():

    var_types = ["bool", "uint", "int", "string"]

    statement_types = ["keyword", "var_decl", "loop"]

    keywords = { "any" : ["throw", "return"],
                 "loop" : ["break", "continue"] }

    def __init__(self, block, expr_depth):
        self.block = block
        self.variables = copy.deepcopy(self.block["scope_vars"])
        self.functions = self.block["funcs"]
        self.depth = expr_depth

    def gen_dead_block(self):
        """ The main function of the dead code generator

            Returns:
                a string to directly place into the contract 
        """
        expr_frame = ""
        if (decision(0.5)):
            expr_frame = self.gen_if_frame(False)
        else:
            expr_frame = self.gen_while_frame()

        expr_body = self.gen_body(4)

        dead_code = expr_frame.format(expr_body)

        return dead_code  

    def gen_if_frame(self, bvalue):
        """ Generate an if statement with a generated condition and a placeholder in the body
            
            @param bvalue: False when the if is a top - level statement
                           Can be True if we have an if within a dead block
        """
        if_cond = "\nif({0})"
        if_body = " {{ \n\t// ***Generated*** \n{0}\n}}\n"

        cond = self.get_condition(bvalue)
        if_cond = if_cond.format(cond)
        if_stat = if_cond + if_body

        return if_stat

    def gen_while_frame(self):
        """ Generate a dead top-level while statement skeleton and its false condition """
        while_cond = "\nwhile({0})"
        while_body = " {{ " + "\n\t// *** Generated *** \n{0}\n" + "}}\n"

        cond = self.get_condition(False)
        while_cond = while_cond.format(cond)
        while_stat = while_cond + while_body

        return while_stat

    def get_condition(self, bvalue):
        """ Generate a false statement to insert in the if/while condition block
            Call the external module Tautology_Generator for that
        """
        tg = t_gen.Tautology_Generator(self.block, self.depth)
        cond = tg.gen_condition(bvalue)

        return cond

    def gen_body(self, n):
        """ Generate the body of a dead code segment 

            @param n: The number of statements in the body

            Returns:
                string to insert in a placeholder position
        """
        code = ""

        for i in range(0, n):
            stat = self.gen_statement()
            code = code + stat + "\n"

        return code

    def gen_statement(self):
        statement_type = random.choice(self.statement_types)
        expr = ""

        if (statement_type == "keyword"):
            expr = random.choice(self.keywords["any"])
            expr = "\t" + expr + ";"
        elif (statement_type == "var_decl"):
            var = self.declare_var()
            expr = ast_parser.var_to_string(var)
            expr = "\t" + expr + ";"
        elif (statement_type == "loop"):
            expr = self.gen_for_loop();

        return expr

    def gen_for_loop(self):
        """ Generate a for loop statement

            @param dead: Boolean value that say whether we will execute the for body at all

            Returns:
                code: The code string that will be inserted into the .sol file
        """
        # construct the frame of the for loop
        for_frame = "\tfor(int {it_name} = {it_val}; {it_name} {sign} {it_stop}; {it_name}{op})"
        for_body = " {{ \n\t{0} \n\t}}\n"

        for_params = self.gen_for_params()
        for_frame = for_frame.format(**for_params)

        for_stats = self.gen_loop_body(for_params["it_name"])
        for_body = for_body.format(for_stats)

        for_stat = for_frame + for_body
        return for_stat

        # mapping = self.find_var("mapping")

    def gen_for_params(self):
        """ Generate all placeholders for a for statement 
            
            Returns:
                params: dictionary containing all missing elements
        """
        params = {}
        params["it_name"] = get_random_name(2)
        params["it_val"] = random.randint(0, 50)
        params["sign"] = random.choice([">", "<", ">=", "<="])
        params["it_stop"] = random.randint(-50, 50)
        params["op"] = random.choice(["++", "--"])

        return params

    def gen_loop_body(self, it_name):
        """ Generate all the statements inside a loop body 
        
            @param it_name: string for the name of the iteration variable
        """
        return "\t" + random.choice(self.keywords["loop"]) + ";"

    # @TESTED
    def find_var(self, var_type, **kwargs):
        """ Check and return an inscope variable of the specified type

            @param var_type: variable type we are searchign for
            @kwargs: in case we are searching for an array or mapping we can specify the composite types

            Returns:
                var: the dictionary representing the variable
        """

        # first find the base type 
        scope_vars = self.variables.get(var_type, None)

        # check if we have vars of the specified type at all
        if (not scope_vars):
            return None

        # check the composite types
        if (not kwargs):
            return random.choice(scope_vars)

        key_type = kwargs.get("key_type")
        value_type = kwargs.get("val_type")

        matching_vars = []

        for var in scope_vars:
            if (var.get("key_type", None) == key_type and var.get("val_type", None) == value_type):
                matching_vars.append(var)

        if(not matching_vars):
            return None

        var = random.choice(matching_vars)
        return var

    # @TESTED
    def declare_var(self, **kwargs):
        """ Generate a random variable in the dead code 

            Returns:
                var: The dictionary format of a variable
        """
        var = {}
        var["name"] = get_random_name(6)
        var["type"] = random.choice(self.var_types)

        # do we want a specific variable
        if(kwargs):
            var_T = kwargs.get("type", None)
            if (not var_T):
                raise ValueError("Bad type provided when declaring variable")
            var["type"] = var_T

            key_type = kwargs.get("key_type", None)
            if (var_T == "array" and not key_type):
                raise ValueError("No key type provided for array")
            if (key_type):
                var["key_type"] = key_type

            self.save_var(var)
            return var

        # random chance of creating an array if no specific type provided in kwargs
        if (decision(0.33)):
            var["type"] = "array"
            var["key_type"] = random.choice(self.var_types)

        self.save_var(var)
        return var

    # @TESTED
    def save_var(self, var):
        var_type = var["type"]
        # save the var into the scope variables
        if(self.variables.get(var_type, None)):
            self.variables[var_type].append(var)
        else:
            self.variables[var_type] = [var]

def decision(prob):
    """generate something wih a certain probability"""
    return (random.random() > prob)

def get_random_name(length):
    rand_str = ''.join(random.choice(string.ascii_lowercase) for m in range(length))
    return "_" + rand_str

def run_generator(block, depth):
    dc_gen = Dead_Generator(block, depth)
    expr = dc_gen.gen_dead_block()

    return expr
