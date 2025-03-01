import ply.lex as lex
import re

tokens = (
    'SELECT', 'WHERE', 'LIMIT',
    'A', 'VAR', 'PREFIX', 'URI',
    'STRING', 'NUMBER',
    'LBRACE', 'RBRACE', 'DOT', 'COLON', 'AT'
)

t_SELECT = r'select'
t_WHERE = r'where'
t_LIMIT = r'LIMIT'
t_A = r'\ba\b'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOT = r'\.'
t_COLON = r':'
t_AT = r'@'

def t_VAR(t):
    r'\?[a-zA-Z]+'
    return t

def t_PREFIX(t):
    r'[a-zA-Z]+:'
    return t

def t_URI(t):
    r'[a-zA-Z]:.+'
    match = re.match(r'[^:]+:(.+)', t.value)
    if match:
        t.value = match.group(1)  # Obtiene solo la parte después de `:`
    return t

def t_STRING(t):
    r'"[^"]+"(@[a-zA-Z]+)?'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

def t_COMMENT(t): 
    r'\#.*' 
    pass 
    # No return value. Token discarded

lexer = lex.lex()

data = ''' 
# DBPedia: obras de Chuck Berry 
select ?nome ?desc where { 
    ?s a dbo:MusicalArtist. 
    ?s foaf:name "Chuck Berry"@en . 
    ?w dbo:artist ?s. 
    ?w foaf:name ?nome. 
    ?w dbo:abstract ?desc 
} LIMIT 1000 
'''

lexer.input(data)

for tok in lexer: 
    print(tok)

