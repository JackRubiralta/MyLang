def parse_block(tokens, start_index=0):
    block = []
    i = start_index

    while i < len(tokens):
        token, value = tokens[i]
        match token:
            case 'VAR' | 'CONST':
                decl_type = 'const' if token == 'CONST' else 'var'
                _, name = tokens[i+1]
                _, type_ = tokens[i+2]
                _, _ = tokens[i+3]  # Skip '='
                _, val = tokens[i+4]
                block.append([decl_type, name, type_, '=', [val]])
                i += 6  # Skip to token after ';'
            case 'IDENT' if tokens[i+1][0] == 'ASSIGN':
                name = value
                expr = []
                i += 2  # Skip 'IDENT' and '='
                while tokens[i][0] != 'END':
                    expr.append(tokens[i][1])
                    i += 1
                block.append([name, '=', expr])
                i += 1  # Skip 'END'
            case 'IF':
                condition = []
                i += 2  # Skip 'IF' and '('
                while tokens[i][0] != 'RPAREN':
                    condition.append(tokens[i][1])
                    i += 1
                i += 2  # Skip ')' and '{'
                if_body, i = parse_block(tokens, i)
                current_block = ['if', condition, if_body]
                block.append(current_block)
                while i < len(tokens) and tokens[i][0] == 'ELSE':
                    if i+1 < len(tokens) and tokens[i+1][0] == 'IF':  # Handling 'else if'
                        i += 2  # Move past 'ELSE' and 'IF'
                        condition = []
                        while tokens[i][0] != 'RPAREN':
                            condition.append(tokens[i][1])
                            i += 1
                        i += 2  # Skip ')' and '{'
                        else_if_body, i = parse_block(tokens, i)
                        current_block.append(['else if', condition, else_if_body])
                    else:  # Handling 'else'
                        i += 2  # Move past 'ELSE' and '{'
                        else_body, i = parse_block(tokens, i)
                        current_block.append(['else', else_body])
            case 'WHILE':
                condition = []
                i += 2  # Skip 'WHILE' and '('
                while tokens[i][0] != 'RPAREN':
                    condition.append(tokens[i][1])
                    i += 1
                i += 2  # Skip ')' and '{'
                while_body, i = parse_block(tokens, i)
                block.append(['while', condition, while_body])
            case 'BREAK':
                block.append(['break'])
                i += 2  # Skip 'BREAK' and ';'
            case 'RBRACE':
                i += 1  # Move past the closing brace
                return block, i  # Exit the loop and return from the current block parsing
            case _:
                i += 1  # Skip unrecognized tokens or handling for other future cases

    return block, i

# Use the corrected parse_block in the parse function
def parse(tokens):
    structured_format, _ = parse_block(tokens)
    return structured_format
