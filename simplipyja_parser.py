import ply.yacc as yacc
from simplipyja_lexer import tokens
import semanticAnalyzer

def p_program(p):
    'program : BEGIN stmt_list DONE'
    for stmt in p[2]:
        exec_stmt(stmt)

def p_stmt_list(p):
    '''stmt_list : stmt stmt_list
                 | '''
    p[0] = [p[1]] + p[2] if len(p) == 3 else []

def p_stmt(p):
    '''stmt : assignment
            | print_stmt
            | if_stmt
            | for_loop
            | natural_stmt'''
    p[0] = p[1]

def p_assignment(p):
    'assignment : MEK ID EQ expr'
    p[0] = ('assign', p[2], p[4])

def p_print_stmt(p):
    '''print_stmt : FLING LPAREN STRING RPAREN
                  | FLING LPAREN expr RPAREN'''
    p[0] = ('print', p[3])

def p_if_stmt(p):
    '''if_stmt : IF expr BEGIN stmt_list DONE
               | IF expr BEGIN stmt_list DONE ELSE BEGIN stmt_list DONE'''
    if len(p) == 6:
        p[0] = ('if', p[2], p[4], [])
    else:
        p[0] = ('if', p[2], p[4], p[8])

def p_for_loop(p):
    'for_loop : FOR ID EQ expr TO expr BEGIN stmt_list DONE'
    p[0] = ('for', p[2], p[4], p[6], p[8])

def p_natural_stmt(p):
    'natural_stmt : SET ID TO expr'
    p[0] = ('assign', p[2], p[4])

def p_expr_binop(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr MUL expr
            | expr DIV expr
            | expr GT expr
            | expr LT expr
            | expr GE expr
            | expr LE expr
            | expr EQEQ expr
            | expr NEQ expr'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expr_group(p):
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]

def p_expr_number(p):
    'expr : NUMBER'
    p[0] = p[1]

def p_expr_string(p):
    'expr : STRING'
    p[0] = p[1]

def p_expr_id(p):
    'expr : ID'
    p[0] = ('var', p[1])

def p_error(p):
    if p:
        raise SyntaxError(f"Syntax error at '{p.value}' (line {p.lineno})")
    else:
        raise SyntaxError("Syntax error at EOF")


def exec_stmt(stmt):
    if stmt[0] == 'assign':
        _, var, val = stmt
        result = eval_expr(val)
        semanticAnalyzer.declare_variable(var, result)

    elif stmt[0] == 'print':
        print(eval_expr(stmt[1]) if isinstance(stmt[1], tuple) else stmt[1])

    elif stmt[0] == 'if':
        _, condition, true_block, false_block = stmt
        if eval_expr(condition):
            for s in true_block:
                exec_stmt(s)
        else:
            for s in false_block:
                exec_stmt(s)

    elif stmt[0] == 'for':
        _, var, start, end, body = stmt
        for i in range(int(eval_expr(start)), int(eval_expr(end)) + 1):
            if var not in semanticAnalyzer.symbol_table:
                semanticAnalyzer.declare_variable(var, i)
            else:
                semanticAnalyzer.set_value(var, i)
            for s in body:
                exec_stmt(s)


def eval_expr(expr):
    if isinstance(expr, tuple):
        if expr[0] == 'binop':
            op = expr[1]
            left = eval_expr(expr[2])
            right = eval_expr(expr[3])

            if op == '+':
                # Handle string or number addition
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                return left / right
            elif op == '>':
                return left > right
            elif op == '<':
                return left < right
            elif op == '>=':
                return left >= right
            elif op == '<=':
                return left <= right
            elif op == '==':
                return left == right
            elif op == '!=':
                return left != right
            else:
                raise Exception(f"Unsupported operator: {op}")

        elif expr[0] == 'var':
            return semanticAnalyzer.get_value(expr[1])

    # literal values (numbers or strings)
    return expr


parser = yacc.yacc()
