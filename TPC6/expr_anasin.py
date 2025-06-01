from expr_analex import lexer

prox_simb = None

def parser_error(simb):
    print(f"Erro sintático: Token inesperado '{simb.type}'")

def rec_term(simb):
    global prox_simb
    if prox_simb.type == simb:
        # print(f"Consumindo token: {prox_simb.type} ({prox_simb.value})")
        prox_simb = lexer.token()
    else:
        parser_error(prox_simb)

#(9-2)*(13-4)
def factor():
    global prox_simb
    if prox_simb.type == 'NUM':
        print("Derivando por P7: factor --> NUM")
        valor = prox_simb.value
        rec_term('NUM')
        print("Reconheci P7: factor --> NUM")
        return valor
    elif prox_simb.type == 'LPAREN':
        print("Derivando por P8: factor --> '(' expr ')' ")
        rec_term('LPAREN')
        valor = expr()
        rec_term('RPAREN')
        print("Reconheci P8: factor --> '(' expr ')' ")
        return valor
    else:
        parser_error(prox_simb)
        return 0

#(9-2)*(13-4)
def term():
    print("Derivando por P4: term --> factor term'")
    valor = factor()
    while prox_simb and prox_simb.type in ('TIMES', 'DIV'):
        op = prox_simb.type
        if op == 'TIMES':
            print("Derivando por P5: term' --> '*' factor term'")
        else:
            print("Derivando por P6: term' --> '/' factor term'")
        rec_term(op)
        if op == 'TIMES':
            valor *= factor()
            print("Reconheci P5: term' --> '*' factor term'")
        elif op == 'DIV':
            valor /= factor()
            print("Reconheci P6: term' --> '/' factor term'")
    print("Reconheci P4: term --> factor term'")
    return valor

#(9-2)*(13-4)
def expr():
    print("Derivando por P1: expr --> term expr'")
    valor = term()
    while prox_simb and prox_simb.type in ('PLUS', 'MINUS'):
        op = prox_simb.type
        if op == 'PLUS':
            print("Derivando por P2: expr' --> '+' term expr'")
        else:
            print("Derivando por P3: expr' --> '-' term expr'")
        rec_term(op)
        if op == 'PLUS':
            valor += term()
            print("Reconheci P2: expr' --> '+' term expr'")
        elif op == 'MINUS':
            valor -= term()
            print("Reconheci P3: expr' --> '-' term expr'")
    print("Reconheci P1: expr --> term expr'")
    return valor

def parse(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    print(f"Analisando expressão: {data}")
    resultado = expr()
    print(f"Expressão '{data}' avaliada como: {resultado}")
    return resultado

# expr    → term expr'
# expr'   → ('+' term expr') | ('-' term expr') | ε
# term    → factor term'
# term'   → ('*' factor term') | ('/' factor term') | ε
# factor  → NUM | '(' expr ')'

# (9-2)*(13-4)

# 2+3
# 67-(2+3*4)
# (9-2)*(13-4)