import re

def tokenize(code):
    token_specification = [
    ('FTYPE', r'(\bint\b|\bfloat\b|\bstring\b)\s*\(\s*(\bint\b|\bfloat\b|\bstring\b)(\s*,\s*(\bint\b|\bfloat\b|\bstring\b))*\s*\)'),
    # Adjust ARRAY_TYPE to match both specified and unspecified sizes
    ('ARRAY_TYPE', r'(\bint\b|\bfloat\b|\bstring\b)\[\d*\]'),  # Array type like int[3] or int[]
    ('ARRAY_INIT', r'\[([ \t]*\d+(,[ \t]*\d+)*)?[ \t]*\]'),  # Array initialization like [1, 2, 3]
    ('ARRAY_ACCESS', r'[a-zA-Z_]\w*\[\d+\]'),  # e.g., list[1]
    # Existing tokens...
    ('NUMBER',   r'\d+(\.\d*)?'),
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
    ('CONST',    r'\bconst\b'),
    ('IF',       r'\bif\b'),
    ('ELSE',     r'\belse\b'),
    ('WHILE',    r'\bwhile\b'),
    ('BREAK',    r'\bbreak\b'),
    ('RETURN',   r'\breturn\b'),
    ('TYPE',     r'\bint\b|\bfloat\b|\bstring\b'),
    ('IDENT',    r'[a-zA-Z_]\w*'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('LBRACE',   r'\{'),
    ('RBRACE',   r'\}'),
    ('SKIP',     r'[ \t\n]+'),
    ('MISMATCH', r'.'),
    ('FCOMMA',   r'\,'), # kinda temporary
    ]


    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    tokens = []
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            value = int(value) if value.isdigit() else float(value)
        elif kind == 'ARRAY_INIT':
            # Convert array initialization to a list of numbers
            value = [int(x) for x in value.strip('[]').split(',')] if value.strip('[]') else []
        elif kind in ['SKIP', 'MISMATCH'] and kind != 'MISMATCH':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value}')
        tokens.append((kind, value))
    return tokens
