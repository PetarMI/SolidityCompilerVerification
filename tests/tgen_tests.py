import sys
sys.path.insert(0,'..')
import tautology_generator as t_gen

func = [{'name': 'mint', 
                'params': [{'name': 'receiver', 'type': 'address'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['string']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool']},
            {'name': 'sirene', 
                'params': [{'name': 'eater', 'type': 'address'}, {'name': 'blocks', 'type': 'uint'}], 
                'ret_params': ['bool']},  ]

variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                'address': [ {'name': 'minter', 'type': 'address'} ],
                'mapping': [ {
                    'name': 'balances',
                    'type': 'mapping',
                    'key_type': 'address',
                    'val_type': 'uint',
                } ],
                'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'uint'} ],
                'uint': [ {'name': 'uint1', 'type': 'uint'} ]}


def run_generator(variables, functions, depth):
    for i in range(1, 5):
        expr = t_gen.run_generator(variables, functions, depth)
        print (expr)
        print()

run_generator(variables, func, 3)