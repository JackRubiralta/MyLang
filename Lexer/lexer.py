import re

def tokenize(code):
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),  # Match integers and decimals
        ('NEQ',      r'!='),
        ('EQ',       r'=='),
        ('LTE',      r'<='),
        ('GTE',      r'>='),
        ('LT',       r'<'),
        ('GT',       r'>'),
        ('ASSIGN',   r'='),
        ('END',      r';'),
        ('OP',       r'[+\-*/]'),
        ('VAR',      r'\bvar\b'),
        ('CONST',    r'\bconst\b'),  # Recognize 'const' for constant declarations
        ('IF',       r'\bif\b'),
        ('ELSE',     r'\belse\b'),
        ('WHILE',    r'\bwhile\b'),
        ('BREAK',    r'\bbreak\b'),
        ('TYPE',     r'\bint\b|\bfloat\b|\bstring\b'),
        ('IDENT',    r'[a-zA-Z_]\w*'),
        ('LPAREN',   r'\('),
        ('RPAREN',   r'\)'),
        ('LBRACE',   r'\{'),
        ('RBRACE',   r'\}'),
        ('SKIP',     r'[ \t\n]+'),
        ('MISMATCH', r'.'),
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    tokens = []
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            value = int(value) if value.isdigit() else float(value)
        elif kind in ['SKIP', 'MISMATCH'] and kind != 'MISMATCH':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value}')
        tokens.append((kind, value))
    return tokens
