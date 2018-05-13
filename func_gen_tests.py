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

def test_bool1(): 

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

def test_bool2(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'receiver', 'type': 'address'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool']} ]

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
    
    expected_funcs = ["mint(minter, uint1)", "send(gstrvar, uint1)"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_string1(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'receiver', 'type': 'address'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['string']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool']} ]

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

    funcs = fc.prep_functions(func, 'string', variables)
    
    expected_funcs = ["mint(minter, uint1)"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_uint1(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'receiver', 'type': 'address'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['string']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool']},
            {'name': 'sirene', 
                'params': [{'name': 'eater', 'type': 'address'}, {'name': 'blocks', 'type': 'uint'}], 
                'ret_params': ['uint']},  ]

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

    funcs = fc.prep_functions(func, 'uint', variables)
    
    expected_funcs = ["sirene(minter, uint1)"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_multiple1(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'receiver', 'type': 'address'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['string']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool']},
            {'name': 'sirene', 
                'params': [{'name': 'eater', 'type': 'address'}, {'name': 'blocks', 'type': 'uint'}], 
                'ret_params': ['string']},  ]

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

    funcs = fc.prep_functions(func, 'string', variables)
    
    expected_funcs = ["mint(minter, uint1)", "sirene(minter, uint1)"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_multiple2(): 

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

    funcs = fc.prep_functions(func, 'bool', variables)
    
    expected_funcs = ["send(gstrvar, uint1)", "sirene(minter, uint1)"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_lack_param1(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'receiver', 'type': 'address'}], 
                'ret_params': ['string']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool']} ]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'mapping': [ {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'address',
                        'val_type': 'uint',
                    } ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'uint'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'string', variables)
    expected_funcs = []

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_lack_param2(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'receiver', 'type': 'address'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['string']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool']} ]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'mapping': [ {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'address',
                        'val_type': 'uint',
                    } ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'uint'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'string', variables)
    
    expected_funcs = []

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_no_params1(): 

    func = [{'name': 'mint', 
                'params': [], 
                'ret_params': ['string']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool']} ]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'mapping': [ {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'address',
                        'val_type': 'uint',
                    } ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'uint'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'string', variables)
    expected_funcs = ["mint()"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_no_params2(): 

    func = [{'name': 'mint', 
                'params': [], 
                'ret_params': ['string']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool']},
            {'name': 'sirene', 
                'params': [], 
                'ret_params': ['bool']} ]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'mapping': [ {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'address',
                        'val_type': 'uint',
                    } ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'uint'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'string', variables)
    
    expected_funcs = ["mint()"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_no_params3(): 

    func = [{'name': 'mint', 
                'params': [], 
                'ret_params': ['string']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool']},
            {'name': 'sirene', 
                'params': [], 
                'ret_params': ['string']} ]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'mapping': [ {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'address',
                        'val_type': 'uint',
                    } ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'uint'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'string', variables)
    
    expected_funcs = ["mint()", "sirene()"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_array1(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'sirenca', 'type': 'array', 'key_type': 'uint'}], 
                'ret_params': ['int']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool']},
            {'name': 'sirene', 
                'params': [], 
                'ret_params': ['string']} ]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'mapping': [ {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'address',
                        'val_type': 'uint',
                    } ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'uint'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'int', variables)
    
    expected_funcs = ["mint(garrvar)"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_array2(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'sirenca', 'type': 'array', 'key_type': 'uint'}], 
                'ret_params': ['int']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool']},
            {'name': 'sirene', 
                'params': [], 
                'ret_params': ['int']} ]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'mapping': [ {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'address',
                        'val_type': 'uint',
                    } ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'uint'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'int', variables)
    
    expected_funcs = ["mint(garrvar)", "sirene()"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_array3(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'sirenca', 'type': 'array', 'key_type': 'uint'}], 
                'ret_params': ['int']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool']}]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'mapping': [ {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'address',
                        'val_type': 'uint',
                    } ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'int', variables)
    
    expected_funcs = []

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_array4(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'sirenca', 'type': 'array', 'key_type': 'uint'}], 
                'ret_params': ['int']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'amount', 'type': 'uint'}], 
                'ret_params': ['bool']}]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'mapping': [ {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'address',
                        'val_type': 'uint',
                    } ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'int', variables)
    
    expected_funcs = []

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_array5(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'sirenca', 'type': 'array', 'key_type': 'bool'}], 
                'ret_params': ['int']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'sirenca', 'type': 'array', 'key_type': 'bool'}], 
                'ret_params': ['int']}]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'mapping': [ {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'address',
                        'val_type': 'uint',
                    } ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'bool'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'int', variables)
    
    expected_funcs = ["mint(garrvar)", "send(gstrvar, garrvar)"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_array6(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'sirenca', 'type': 'array', 'key_type': 'uint'}], 
                'ret_params': ['int']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'sirenca', 'type': 'array', 'key_type': 'bool'}], 
                'ret_params': ['int']}]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'mapping': [ {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'address',
                        'val_type': 'uint',
                    } ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'bool'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'int', variables)
    
    expected_funcs = ["send(gstrvar, garrvar)"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_array7(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'sirenca', 'type': 'array', 'key_type': 'uint'}], 
                'ret_params': ['int']}, 
            {'name': 'send',
                'params': [{'name': 'receiver', 'type': 'string'}, {'name': 'sirenca', 'type': 'array', 'key_type': 'bool'}], 
                'ret_params': ['int']}]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'mapping': [ {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'address',
                        'val_type': 'uint',
                    } ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'uint'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'int', variables)
    
    expected_funcs = ["mint(garrvar)"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_mapping1(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'sirenca', 'type': 'mapping', 'key_type': 'string', 'val_type': 'int'}], 
                'ret_params': ['int']}, 
            {'name': 'send',
                'params': [ {'name': 'receiver', 'type': 'string'}, 
                            {'name': 'kartofi', 'type': 'mapping', 'key_type': 'string', 'val_type': 'bool'} ], 
                'ret_params': ['bool']}]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'int', variables)
    
    expected_funcs = []

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_mapping2(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'sirenca', 'type': 'mapping', 'key_type': 'string', 'val_type': 'int'}], 
                'ret_params': ['int']}, 
            {'name': 'send',
                'params': [ {'name': 'receiver', 'type': 'string'}, 
                            {'name': 'kartofi', 'type': 'mapping', 'key_type': 'string', 'val_type': 'bool'} ], 
                'ret_params': ['bool']}]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
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
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'int', variables)

    expected_funcs = []

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_mapping3(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'sirenca', 'type': 'mapping', 'key_type': 'string', 'val_type': 'int'}], 
                'ret_params': ['int']}, 
            {'name': 'send',
                'params': [ {'name': 'kartofi', 'type': 'mapping', 'key_type': 'uint', 'val_type': 'bool'} ], 
                'ret_params': ['int']}]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'mapping': [ 
                        {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'string',
                        'val_type': 'uint', 
                        }, 
                        {
                        'name': 'mapp',
                        'type': 'mapping',
                        'key_type': 'uint',
                        'val_type': 'string', 
                        } 
                    ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'int', variables)
    
    expected_funcs = []

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_mapping4(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'sirenca', 'type': 'mapping', 'key_type': 'string', 'val_type': 'int'}], 
                'ret_params': ['int']}, 
            {'name': 'send',
                'params': [ {'name': 'kartofi', 'type': 'mapping', 'key_type': 'uint', 'val_type': 'bool'} ], 
                'ret_params': ['int']}]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'mapping': [ 
                        {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'string',
                        'val_type': 'int', 
                        }, 
                        {
                        'name': 'mapp',
                        'type': 'mapping',
                        'key_type': 'uint',
                        'val_type': 'string', 
                        } 
                    ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'int', variables)
    
    expected_funcs = ["mint(balances)"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_mapping5(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'sirenca', 'type': 'mapping', 'key_type': 'string', 'val_type': 'int'}], 
                'ret_params': ['int']}, 
            {'name': 'send',
                'params': [ {'name': 'receiver', 'type': 'string'}, 
                            {'name': 'kartofi', 'type': 'mapping', 'key_type': 'uint', 'val_type': 'bool'} ], 
                'ret_params': ['int']}]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'mapping': [ 
                        {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'bool',
                        'val_type': 'int', 
                        }, 
                        {
                        'name': 'mapp',
                        'type': 'mapping',
                        'key_type': 'uint',
                        'val_type': 'bool', 
                        } 
                    ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'int', variables)
    
    expected_funcs = ["send(gstrvar, mapp)"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_mapping6(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'sirenca', 'type': 'mapping', 'key_type': 'string', 'val_type': 'int'}], 
                'ret_params': ['int']}, 
            {'name': 'send',
                'params': [ {'name': 'receiver', 'type': 'string'}, 
                            {'name': 'kartofi', 'type': 'mapping', 'key_type': 'uint', 'val_type': 'bool'} ], 
                'ret_params': ['int']}]

    variables = {   'bool': [ {'name': 'gboolvar', 'type': 'bool'} ],
                    'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'mapping': [ 
                        {
                        'name': 'balances',
                        'type': 'mapping',
                        'key_type': 'string',
                        'val_type': 'int', 
                        }, 
                        {
                        'name': 'mapp',
                        'type': 'mapping',
                        'key_type': 'uint',
                        'val_type': 'bool', 
                        } 
                    ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'int', variables)
    
    expected_funcs = ["mint(balances)", "send(gstrvar, mapp)"]

    assert(funcs_equal(funcs, expected_funcs))

    print("Test PASSED+++++++++++++")

def test_literals1(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'sirenca', 'type': 'bool'}], 
                'ret_params': ['int']}, 
            {'name': 'send',
                'params': [ {'name': 'receiver', 'type': 'string'}, 
                            {'name': 'kartofi', 'type': 'array', 'key_type': 'uint'} ], 
                'ret_params': ['int']}]

    variables = {   'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'int', variables)
    
    expected_funcs = ["mint(True)", "mint(False)"]

    if(len(funcs) == 1 and funcs[0] in expected_funcs):
        print("Test PASSED+++++++++++++")
    else:
        print("Test FAILED-------------")

def test_literals2(): 

    func = [{'name': 'mint', 
                'params': [{'name': 'sirenca', 'type': 'bool'}], 
                'ret_params': ['int']}, 
            {'name': 'send',
                'params': [ {'name': 'receiver', 'type': 'bool'}, 
                            {'name': 'kartofi', 'type': 'array', 'key_type': 'uint'} ], 
                'ret_params': ['int']}]

    variables = {   'string': [ {'name': 'gstrvar', 'type': 'string'} ],
                    'array': [ {'name': 'garrvar', 'type': 'array', 'key_type': 'string'} ],
                    'uint': [ {'name': 'uint1', 'type': 'uint'} ]}

    funcs = fc.prep_functions(func, 'int', variables)
    
    expected_funcs = ["mint(True)", "mint(False)"]

    if(len(funcs) == 1 and funcs[0] in expected_funcs):
        print("Test PASSED+++++++++++++")
    else:
        print("Test FAILED-------------")

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
    test_bool1()
    test_bool2()
    test_string1()
    test_string1()
    test_multiple1()
    test_multiple2()
    test_lack_param1()
    test_lack_param2()
    test_no_params1()
    test_no_params2()
    test_no_params3()
    test_array1()
    test_array2()
    test_array3()
    test_array4()
    test_array5()
    test_array6()
    test_array7()
    test_mapping1()
    test_mapping2()
    test_mapping3()
    test_mapping4()
    test_mapping5()
    test_mapping6()
    test_literals1()
    test_literals2()

run_tests()