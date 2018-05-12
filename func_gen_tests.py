import function_caller as fc

def test_empty1(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'receiver', 'type': 'address'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': []}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'address'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': []} ]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'address': [ {'name': 'minter', 'type': 'address'},
                                 {'name': 'receiver', 'type': 'address'} ],
                    'mapping': [ {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'address',
                        'val_type': 'uint',
                    } ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'uint'} ],
                    'uint': [ {'name': 'amount', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, "bool", variables)

    expected_funcs = []

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_empty2(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'receiver', 'type': 'address'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool', 'uint']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'address'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': []} ]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'address': [ {'name': 'minter', 'type': 'address'},
                                 {'name': 'receiver', 'type': 'address'} ],
                    'mapping': [ {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'address',
                        'val_type': 'uint',
                    } ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'uint'} ],
                    'uint': [ {'name': 'amount', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, "bool", variables)

    expected_funcs = []

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test3(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'receiver', 'type': 'address'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'address'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': []} ]

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

    funcs = fc.prep_functions(func, 'bool', variables)
    
    expected_funcs = ["mint(minter, uint1)"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def funcs_equal(res_funcs, expected_funcs):
    if (len(res_funcs) != len(expected_funcs)):
        return False

    for (r, e) in zip(res_funcs, expected_funcs):
        if (r != e):
            return False

    return True 

def run_tests():
    test_empty1()
    test_empty2()
    test3()

run_tests()