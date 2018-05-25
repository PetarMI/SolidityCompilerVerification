import sys
sys.path.insert(0,'..')
import dead_generator as dead_gen
import unittest

class DeadGenTester(unittest.TestCase):
    def test_no_arrs(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        mapping = { 'name': 'balances',
                    'type': 'mapping',
                    'key_type': 'address',
                    'val_type': 'int' }

        dg = dead_gen.Dead_Generator(block, 3)
        statements = dg.gen_map_loop(mapping, "index", 0)

        print ("Test no arrays")
        print (dead_gen.concat_lines(statements))
        assert(len(statements) == 8)

    def test_no_right_arrs1(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        mapping = { 'name': 'balances',
                    'type': 'mapping',
                    'key_type': 'address',
                    'val_type': 'int' }

        dg = dead_gen.Dead_Generator(block, 3)
        statements = dg.gen_map_loop(mapping, "index", 0)

        print ("Test no arrays")
        print (dead_gen.concat_lines(statements))
        assert(len(statements) == 8)

    def test_no_right_arrs2(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'},
                                                {'name': 'barrvar', 'type': 'array', 'key_type': 'bool'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        mapping = { 'name': 'balances',
                    'type': 'mapping',
                    'key_type': 'address',
                    'val_type': 'int' }

        dg = dead_gen.Dead_Generator(block, 3)
        statements = dg.gen_map_loop(mapping, "index", 0)

        print ("Test no arrays")
        print (dead_gen.concat_lines(statements))
        assert(len(statements) == 8)

    def test_key_arr(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'},
                                                {'name': 'karrvar', 'type': 'array', 'key_type': 'address'},
                                                {'name': 'barrvar', 'type': 'array', 'key_type': 'bool'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        mapping = { 'name': 'balances',
                    'type': 'mapping',
                    'key_type': 'address',
                    'val_type': 'int' }

        dg = dead_gen.Dead_Generator(block, 3)
        statements = dg.gen_map_loop(mapping, "index", 0)

        print ("Test key arrays")
        print (dead_gen.concat_lines(statements))
        assert(len(statements) == 6)

    def test_val_arr(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'},
                                                {'name': 'karrvar', 'type': 'array', 'key_type': 'int'},
                                                {'name': 'barrvar', 'type': 'array', 'key_type': 'bool'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        mapping = { 'name': 'balances',
                    'type': 'mapping',
                    'key_type': 'address',
                    'val_type': 'int' }

        dg = dead_gen.Dead_Generator(block, 3)
        statements = dg.gen_map_loop(mapping, "index", 0)

        print ("Test value arrays")
        print (dead_gen.concat_lines(statements))
        assert(len(statements) == 6)

    def test_arrs(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'},
                                                {'name': 'karrvar', 'type': 'array', 'key_type': 'address'},
                                                {'name': 'barrvar', 'type': 'array', 'key_type': 'int'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        mapping = { 'name': 'balances',
                    'type': 'mapping',
                    'key_type': 'address',
                    'val_type': 'int' }

        dg = dead_gen.Dead_Generator(block, 3)
        statements = dg.gen_map_loop(mapping, "index", 0)

        print ("Test have arrays")
        print (dead_gen.concat_lines(statements))
        assert(len(statements) == 4)

if __name__ == '__main__':
    unittest.main()