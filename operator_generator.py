import random

unary_expr = "{op} {var}"
binary_expr = "{var1} {op} {var2}"

ops = { "bool" : { "!" : "unary",
                   "&&" : "binary",
                   "||" : "binary",
                   "==" : "binary",
                   "!=" : "binary" },

        "uint" : { "~" : "unary",
                   "unary-" : "unary",
                   "-" : "binary",
                   "+" : "binary",
                   "/" : "binary",
                   "*" : "binary",
                   "&" : "binary",
                   "|" : "binary",
                   "^" : "binary",
                   ">>": "binary",
                   "<<":"binary"},

        "int": { "~": "unary",
                 "unary-": "unary",
                 "-": "binary",
                 "+": "binary",
                 "/": "binary",
                 "*": "binary",
                 "&": "binary",
                 "|": "binary",
                 "^": "binary",
                 ">>": "binary",
                 "<<":"binary"}}


def get_op(var, variables):
    type_ops = ops[var["type"]]

    if (not type_ops):
        return var["name"]

    operator, op_type = random.choice(list(type_ops.items()))

    if (operator == "unary-"):
        operator = "-"

    if (op_type == "unary"):
        fargs = {"op" : operator, "var" : var["name"]}
        return unary_expr.format(**fargs)
    else:
        var2 = choose_var(var, variables)
        # TODO randomly choose which var comes first
        fargs = {"var1" : var["name"], "op" : operator, "var2" : var2["name"]}
        return binary_expr.format(**fargs)


def choose_var(var, variables):
    available_vars = variables.get(var["type"], None)

    if (available_vars):
        return random.choice(available_vars)
    else:
        return var