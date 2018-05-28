import random
import string
import tautology_generator as t_gen
import operator_generator as op_gen
import ast_parser
import copy

class Dead_Generator():

    var_types = ["bool", "uint", "int", "string"]

    statement_types = ["keyword", "var_decl"]

    keywords = { "any" : ["throw", "return"],
                 "loop" : ["break", "continue"] }

    structs = { "if" : "if({0}) {{",
                "while" : "while({0}) {{",
                "for" : "for(uint {it_name} = {it_val}; {it_name} {sign} {it_stop}; {it_name}{op}) {{" }

    init_stats = { "init_arr" : "{arr_name} = new {arr_type}[]({n})",
                   "assign_to_arr" : "{var_name} = {arr_name}[{index}]", 
                   "map_assign" : "{map_name}[{index}] = {op}" }

    generated_line = "// *** Generated ***"

    def __init__(self, block, expr_depth):
        self.block = block
        self.variables = copy.deepcopy(self.block["scope_vars"])
        self.functions = self.block["funcs"]
        self.depth = expr_depth

    def gen_dead_block(self, i):
        """ The main function of the dead code generator
            
            @param i: Indentation level

            Returns:
                a string to directly place into the contract 
        """
        dead_code = ""
        if (decision(0.5)):
            dead_code = self.gen_struct("if", False, i)
        else:
            dead_code = self.gen_struct("while", False, i)

        return dead_code + "\n" + indent("", i)

    def gen_struct(self, struct_type, bvalue, i):
        """ Generate an if/while statement with a generated condition and a statements in the body
            
            @param struct_value: if or while
            @param bvalue: False when the if is a top - level statement
                           Can be True if we have an if within a dead block (not implemented)
            @i: Indentation level
        """
        if (struct_type not in ["if", "while"]):
            raise ValueError("Trying to generate something else than if/while")

        struct_cond = self.structs[struct_type]
        cond = self.get_condition(bvalue)
        struct_cond = struct_cond.format(cond)

        struct_body = indent(self.generated_line, i+1)
        struct_body = struct_body + "\n" + self.gen_body(4, i+1)

        struct = indent(struct_cond, i) + "\n" + struct_body + "\n" + indent("}", i)
        return struct

    def get_condition(self, bvalue):
        """ Generate a false statement to insert in the if/while condition block
            Call the external module Tautology_Generator for that
        """
        tg = t_gen.Tautology_Generator(self.block, self.depth)
        cond = tg.gen_condition(bvalue)

        return cond

    def gen_body(self, n, i):
        """ Generate the body of a dead code segment 

            @param n: The number of statements in the body

            Returns:
                list of indented strings to insert in a placeholder position
        """
        statements = []

        for c in range(0, n - 1):
            statements.append(self.gen_statement(i))

        # generate one for loop because of variable declaration restriction
        statements.append(self.gen_for_loop(i))

        code = concat_lines(statements)
        return code

    def gen_statement(self, i):
        statement_type = random.choice(self.statement_types)
        expr = ""

        if (statement_type == "keyword"):
            expr = random.choice(self.keywords["any"])
            expr = indent(expr + ";", i)
        elif (statement_type == "var_decl"):
            var = self.declare_var()
            expr = ast_parser.var_to_string(var)
            expr = indent(expr + ";", i)

        return expr

    def gen_for_loop(self, i):
        """ Generate a for loop statement

            @param dead: Boolean value that say whether we will execute the for body at all

            Returns:
                code: The code string that will be inserted into the .sol file
        """
        # construct the frame of the for loop
        for_frame = self.structs["for"]
        for_params = self.gen_for_params()
        for_frame = for_frame.format(**for_params)

        for_body = self.gen_loop_body(for_params["it_name"], i+1)

        for_stat = indent(for_frame, i) + "\n" + for_body + "\n" + indent("}", i)
        return for_stat

    # TODO ensure we cant go in there?
    def gen_for_params(self):
        """ Generate all placeholders for a for statement 
            
            Returns:
                params: dictionary containing all missing elements
        """
        params = {}
        params["it_name"] = get_random_name(2)
        params["it_val"] = random.randint(0, 50)
        params["sign"] = random.choice([">", "<", ">=", "<="])
        params["it_stop"] = random.randint(0, 50)
        params["op"] = random.choice(["++", "--"])

        return params

    def gen_loop_body(self, it_name, i):
        """ Generate all the statements inside a loop body 
            The point is to operate on every element of a mapping and an array

            @param it_name: string for the name of the iteration variable
        """
        statements = []

        # find a mapping to operate on
        mapping = self.find_var("mapping")
        if (mapping):
            statements = self.gen_map_loop(mapping, it_name, i)
        else:
            print("No mapping found")
            statements = [indent(random.choice(self.keywords["loop"]) + ";", i)]        

        return concat_lines(statements)

    def gen_map_loop(self, mapping, it_name, i):
        statements = []

        map_key_type = mapping["key_type"]
        map_val_type = mapping["val_type"]

        # find a key array
        kwargs = { "key_type" : map_key_type }
        key_arr = self.find_var("array", **kwargs)

        # if we don't have an array for the key type, generate one
        if (key_arr == None):
            kwargs = { "name" : get_random_name(6), "type" : "array", "key_type" : map_key_type }
            key_arr, stats = self.new_var(i, **kwargs)
            statements.extend(stats)

        # key variable declaration
        kwargs = { "name" : get_random_name(6), "type" : map_key_type, "init_name" : key_arr["name"], "index" : it_name}
        key_el, stats = self.new_var(i, **kwargs)
        statements.extend(stats)

        # map array 
        kwargs = { "key_type" : map_val_type}
        val_arr = self.find_var("array", **kwargs)

        if (val_arr == None):
            kwargs = { "type" : "array", "key_type" : map_val_type}
            val_arr, stats = self.new_var(i, **kwargs)
            statements.extend(stats)

        # value variable declaration
        kwargs = { "name" : get_random_name(6), "type" : map_val_type, "init_name" : val_arr["name"], "index" : it_name}
        val_el, stats = self.new_var(i, **kwargs)
        statements.extend(stats)

        # do the operation
        op = op_gen.get_op(val_el, self.variables)
        kwargs = {"index" : key_el["name"], "op" : op}
        map_op = self.assign_var(mapping, **kwargs)

        statements.append(indent(map_op + ";", i))

        return statements

    # @TESTED
    def find_var(self, var_type, **kwargs):
        """ Check and return an inscope variable of the specified type

            @param var_type: variable type we are searching for
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

    def new_var(self, i, **kwargs):
        """ Function to declare and initialize a new variable
            Basically a wrapper around declare_var and assign_var
        
            @param kwargs: everything needed for the new var. If None provided get a random var

            Returns:
                var: the new variable in dict format
                statements: the list of statements that need to be inserted in the code
        """
        statements = []

        n_var = self.declare_var(**kwargs)
        statements.append(indent(ast_parser.var_to_string(n_var) + ";", i))

        # build he kwargs for the initialization part
        if (kwargs.get("init_name", None)):
            n_var_init = self.assign_var(n_var, **kwargs)
        else:
            n_var_init = self.assign_var(n_var)
        statements.append(indent(n_var_init + ";", i))

        return n_var, statements

    # @TESTED
    # TODO This would have been better with *args and not **kwargs
    def declare_var(self, **kwargs):
        """ Generate a random variable in the dead code 
            
            @param kwargs: name, type and key_type

            Returns:
                var: The dictionary format of a variable
        """
        var = {}
        var["name"] = get_random_name(6)
        var["type"] = random.choice(self.var_types)

        # do we want a specific variable
        if(kwargs):
            var_name = kwargs.get("name", None)
            if (var_name):
                var["name"] = var_name

            var_T = kwargs.get("type", None)
            if (not var_T):
                raise ValueError("Bad type provided when declaring variable")
            var["type"] = var_T

            key_type = kwargs.get("key_type", None)
            if (var_T == "array" and not key_type):
                raise ValueError("No key type provided for array")
            if (key_type):
                var["key_type"] = key_type

            # self.save_var(var)
            return var

        # random chance of creating an array if no specific type provided in kwargs
        if (decision(0.33)):
            var["type"] = "array"
            var["key_type"] = random.choice(self.var_types)

        # self.save_var(var)
        return var

    def assign_var(self, var, **kwargs):
        """ Perform a variable assignment
            If it is an array we initialize it to a new array
            If it is a mapping we assign the key to some new value
            If it is neither the var gets assigned to an element from an array specified in kwargs
            
            @param var: The variable to init
            @param kwargs: When we want to init to sth specific
                           init_name, index, op

            Returns:
                The string to be inserted in the code for the assignment
        """
        var_assign = ""
        var_name = var["name"]

        if (var["type"] == "array"):
            n = random.randint(1, 100)
            var_assign = self.init_stats["init_arr"]
            fargs = {"arr_name" : var_name, "arr_type" : var["key_type"], "n" : n}
        elif (var["type"] == "mapping"):
            var_assign = self.init_stats["map_assign"]
            fargs = {"map_name" : var_name, "index" : kwargs["index"], "op" : kwargs["op"]}
        elif (kwargs):
            # most general case where we are assigning whatever to something specific
            var_assign = self.init_stats["assign_to_arr"]
            fargs = {"var_name" : var_name, "arr_name" : kwargs["init_name"], "index" : kwargs["index"]}
 
        else:
            raise ValueError("Failed to assign a variable")

        var_assign = var_assign.format(**fargs)
        return var_assign

    # @TESTED
    def save_var(self, var):
        var_type = var["type"]
        # save the var into the scope variables
        if(self.variables.get(var_type, None)):
            self.variables[var_type].append(var)
        else:
            self.variables[var_type] = [var]

def indent(stat, n):
    return "\t"*n + stat

def concat_lines(lines):
    code = ""

    for line in lines:
        code += line + "\n"

    return code

def decision(prob):
    """generate something wih a certain probability"""
    return (random.random() > prob)

def get_random_name(length):
    rand_str = ''.join(random.choice(string.ascii_lowercase) for m in range(length))
    return "_" + rand_str

def run_generator(block, depth):
    dc_gen = Dead_Generator(block, depth)
    expr = dc_gen.gen_dead_block(2)

    return expr
