# Symbol Table for Variable Management
symbol_table = {}

def check_declaration(var_name):
    if var_name not in symbol_table:
        raise Exception(f"Semantic Error: Variable '{var_name}' used before declaration")

def declare_variable(var_name, value):
    symbol_table[var_name] = value

def get_value(var_name):
    check_declaration(var_name)
    return symbol_table[var_name]

def set_value(var_name, value):
    check_declaration(var_name)
    symbol_table[var_name] = value

def reset_scope():
    global symbol_table
    symbol_table = {}
