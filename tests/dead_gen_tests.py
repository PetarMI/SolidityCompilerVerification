import sys
sys.path.insert(0,'..')
import dead_generator as dead_gen
import unittest

class DeadGenTester(unittest.TestCase):
    def test_no_var_simple(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
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
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        var = dg.find_var("int")
        assert(var == None)

        print("Test PASSED+++++++++++++")

    def test_var_simple1(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
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
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        var = dg.find_var("bool")
        assert(var["type"] == "bool")

        print("Test PASSED+++++++++++++")

    def test_var_simple1(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
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
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        var = dg.find_var("bool")
        assert(var["type"] == "bool")

        print("Test PASSED+++++++++++++")

    def test_var_simple2(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
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
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        var = dg.find_var("string")
        assert(var["type"] == "string")

        print("Test PASSED+++++++++++++")

    def test_var_no_array(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
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
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"key_type": "bool"}
        var = dg.find_var("array", **kwargs)
        assert(var == None)

        print("Test PASSED+++++++++++++")

    def test_var_no_array_key(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
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
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'address'},
                                                {'name': 'arrvar', 'type': 'array', 'key_type': 'int'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"key_type": "string"}
        var = dg.find_var("array", **kwargs)
        assert(var == None)

        print("Test PASSED+++++++++++++")

    def test_var_array(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
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
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'address'},
                                                {'name': 'arrvar', 'type': 'array', 'key_type': 'int'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"key_type": "address"}
        var = dg.find_var("array", **kwargs)
        assert(var["type"] == "array" and var["key_type"] == "address")

        print("Test PASSED+++++++++++++")

    def test_var_no_map1(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'address'},
                                                {'name': 'arrvar', 'type': 'array', 'key_type': 'int'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        var = dg.find_var("mapping")
        assert(var == None)

        print("Test PASSED+++++++++++++")

    def test_var_no_map2(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'address'},
                                                {'name': 'arrvar', 'type': 'array', 'key_type': 'int'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"key_type": "address", "val_type" : "uint"}
        var = dg.find_var("array", **kwargs)
        assert(var == None)

        print("Test PASSED+++++++++++++")

    def test_var_no_map_key1(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
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
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'address'},
                                                {'name': 'arrvar', 'type': 'array', 'key_type': 'int'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"val_type": "string"}
        var = dg.find_var("mapping", **kwargs)
        assert(var == None)

        print("Test PASSED+++++++++++++")

    def test_var_no_map_key2(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
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
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'address'},
                                                {'name': 'arrvar', 'type': 'array', 'key_type': 'int'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"key_type" : "uint", "val_type": "string"}
        var = dg.find_var("mapping", **kwargs)
        assert(var == None)

        print("Test PASSED+++++++++++++")

    def test_var_no_map_value1(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
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
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'address'},
                                                {'name': 'arrvar', 'type': 'array', 'key_type': 'int'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"key_type": "address"}
        var = dg.find_var("mapping", **kwargs)
        assert(var == None)

        print("Test PASSED+++++++++++++")

    def test_var_no_map_value2(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
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
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'address'},
                                                {'name': 'arrvar', 'type': 'array', 'key_type': 'int'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"key_type" : "address", "val_type": "bool"}
        var = dg.find_var("mapping", **kwargs)
        assert(var == None)

        print("Test PASSED+++++++++++++")

    def test_var_map1(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
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
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'address'},
                                                {'name': 'arrvar', 'type': 'array', 'key_type': 'int'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"key_type" : "address", "val_type": "int"}
        var = dg.find_var("mapping", **kwargs)
        assert(var["type"] == "mapping" and var["key_type"] == "address" and var["val_type"] == "int")

        print("Test PASSED+++++++++++++")

    def test_var_map2(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
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
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'address'},
                                                {'name': 'arrvar', 'type': 'array', 'key_type': 'int'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"key_type" : "string", "val_type": "string"}
        var = dg.find_var("mapping", **kwargs)
        assert(var["type"] == "mapping" and var["key_type"] == "string" and var["val_type"] == "string")

        print("Test PASSED+++++++++++++")

    def test_var_map_multiple(self):
        block = {   "scope_vars" : { 'bool': [ {'name': 'gboolvar', 'type': 'bool'},
                                               {'name': 'boolvar', 'type': 'bool'} ],
                                     'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                                     'mapping': [ 
                                        {
                                            'name': 'balances',
                                            'type': 'mapping',
                                            'key_type': 'address',
                                            'val_type': 'uint', 
                                        }, 
                                        {
                                            'name': 'mapp',
                                            'type': 'mapping',
                                            'key_type': 'string',
                                            'val_type': 'string', 
                                        },
                                        {
                                            'name': 'more_balances',
                                            'type': 'mapping',
                                            'key_type': 'address',
                                            'val_type': 'uint', 
                                        }
                                     ],
                                     'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'address'},
                                                {'name': 'arrvar', 'type': 'array', 'key_type': 'int'} ],
                                     'uint': [ {'name': 'uint1', 'type': 'uint'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"key_type" : "address", "val_type": "uint"}
        var = dg.find_var("mapping", **kwargs)
        assert(var["type"] == "mapping" and var["key_type"] == "address" and var["val_type"] == "uint")

        print("Test PASSED+++++++++++++")

    def test_create_and_save_simple_empty(self):
        block = {   "scope_vars" : {},
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"type" : "address"}
        var = dg.declare_var(**kwargs)
        assert(var["type"] == "address" and var.get("key_type", None) == None and var.get("val_type") == None)
        #assert(len(dg.variables["address"]) == 1)

        print("Test PASSED+++++++++++++")

    def test_create_and_save_simple(self):
        block = {   "scope_vars" : { "address" : [ {'name': 'addrvar', 'type': 'address'} ]},
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"type" : "address"}
        var = dg.declare_var(**kwargs)
        assert(var["type"] == "address" and var.get("key_type", None) == None and var.get("val_type") == None)
        #assert(len(dg.variables["address"]) == 2)

        print("Test PASSED+++++++++++++")

    def test_create_and_save_array1(self):
        block = {   "scope_vars" : { "address" : [ {'name': 'addrvar', 'type': 'address'} ]},
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"type" : "array", "key_type" : "string"}
        var = dg.declare_var(**kwargs)
        assert(var["type"] == "array" and var.get("key_type", None) == "string" and var.get("val_type") == None)
        #assert(len(dg.variables["array"]) == 1)

        print("Test PASSED+++++++++++++")

    def test_create_and_save_array2(self):
        block = {   "scope_vars" : { "address" : [ {'name': 'addrvar', 'type': 'address'} ],
                                     "array": [ {'name': 'garrvar', 'type': 'array', 'key_type': 'address'},
                                                {'name': 'arrvar', 'type': 'array', 'key_type': 'int'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"type" : "array", "key_type" : "address"}
        var = dg.declare_var(**kwargs)
        assert(var["type"] == "array" and var.get("key_type", None) == "address" and var.get("val_type") == None)
        #assert(len(dg.variables["array"]) == 3)

        print("Test PASSED+++++++++++++")

    def test_create_and_save_array_fail1(self):
        block = {   "scope_vars" : { "address" : [ {'name': 'addrvar', 'type': 'address'} ],
                                     "array": [ {'name': 'garrvar', 'type': 'array', 'key_type': 'address'},
                                                {'name': 'arrvar', 'type': 'array', 'key_type': 'int'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"key_type" : "address"}
        with self.assertRaises(ValueError):
            dg.declare_var(**kwargs)
        #assert(len(dg.variables["array"]) == 2)

        print("Test PASSED+++++++++++++")

    def test_create_and_save_array_fail2(self):
        block = {   "scope_vars" : { "address" : [ {'name': 'addrvar', 'type': 'address'} ],
                                     "array": [ {'name': 'garrvar', 'type': 'array', 'key_type': 'address'},
                                                {'name': 'arrvar', 'type': 'array', 'key_type': 'int'} ] },
                    "funcs" : [] }

        dg = dead_gen.Dead_Generator(block, 3)
        kwargs = {"type" : "array"}
        with self.assertRaises(ValueError):
            dg.declare_var(**kwargs)
        #assert(len(dg.variables["array"]) == 2)

        print("Test PASSED+++++++++++++")

if __name__ == '__main__':
    unittest.main()

"""def run_tests():
    # find_var() testing
    test_no_var_simple()
    test_var_simple1()
    test_var_simple2()
    test_var_no_array()
    test_var_no_array_key()
    test_var_array()
    test_var_no_map1()
    test_var_no_map2()
    test_var_no_map_key1()
    test_var_no_map_key2()
    test_var_no_map_value1()
    test_var_no_map_value2()
    test_var_map1()
    test_var_map2()
    test_var_map_multiple()

    # declare_var() testing
    test_create_and_save_simple_empty()
    test_create_and_save_simple()
    test_create_and_save_array1()
    test_create_and_save_array2()
    test_create_and_save_array_fail1()

run_tests()"""