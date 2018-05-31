import sys
sys.path.insert(0, '..')
import operator_generator as op_gen


def op_gen_bool():
    variables = {'bool': [{'name': 'gboolvar', 'type': 'bool'},
                          {'name': 'boolvar', 'type': 'bool'}],
                 'string': [{'name': 'gstrvar', 'type': 'string'}],
                 'mapping': [
                     {
                         'name': 'balances',
                         'type': 'mapping',
                         'key_type': 'address',
                         'val_type': 'int',
                     },
                     {
                         'name': 'mapp',
                         'type': 'mapping',
                         'key_type': 'string',
                         'val_type': 'string',
                     }
                 ],
                 'array': [{'name': 'garrvar', 'type': 'array', 'key_type': 'string'}],
                 'uint': [{'name': 'uint1', 'type': 'uint'}]}

    var = {"name" : "myvar", "type" : "bool"}

    expr = op_gen.get_op(var, variables)
    print (expr)

def op_gen_int():
    variables = {'bool': [{'name': 'gboolvar', 'type': 'bool'},
                          {'name': 'boolvar', 'type': 'bool'}],
                 'string': [{'name': 'gstrvar', 'type': 'string'}],
                 'mapping': [
                     {
                         'name': 'balances',
                         'type': 'mapping',
                         'key_type': 'address',
                         'val_type': 'int',
                     },
                     {
                         'name': 'mapp',
                         'type': 'mapping',
                         'key_type': 'string',
                         'val_type': 'string',
                     }
                 ],
                 'array': [{'name': 'garrvar', 'type': 'array', 'key_type': 'string'}],
                 'uint': [{'name': 'uint1', 'type': 'uint'}]}

    var = {"name" : "myvar", "type" : "int"}

    expr = op_gen.get_op(var, variables)
    print (expr)

def op_gen_uint():
    variables = {'bool': [{'name': 'gboolvar', 'type': 'bool'},
                          {'name': 'boolvar', 'type': 'bool'}],
                 'string': [{'name': 'gstrvar', 'type': 'string'}],
                 'mapping': [
                     {
                         'name': 'balances',
                         'type': 'mapping',
                         'key_type': 'address',
                         'val_type': 'int',
                     },
                     {
                         'name': 'mapp',
                         'type': 'mapping',
                         'key_type': 'string',
                         'val_type': 'string',
                     }
                 ],
                 'array': [{'name': 'garrvar', 'type': 'array', 'key_type': 'string'}],
                 'uint': [{'name': 'uint1', 'type': 'uint'},
                          {'name': 'uint2', 'type': 'uint'}]}

    var = {"name" : "myvar", "type" : "uint"}

    expr = op_gen.get_op(var, variables)
    print (expr)

def run():
    print("Generating boolean expressions")
    for i in range(0, 5):
        op_gen_bool()

    print()

    print("Generating integer expressions")
    for i in range(0, 5):
        op_gen_int()

    print()

    print("Generating uint expressions")
    for i in range(0, 5):
        op_gen_uint()

if __name__ == "__main__":
    run()
