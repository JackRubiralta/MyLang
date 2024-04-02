def parse_function_parameters(ftype):
    # This is a simplified parser for the function type string.
    # It assumes a single type for return and parameters for demonstration.
    # Extract parameter types from the ftype string, e.g., "int(int, float)"
    param_types = ftype[ftype.find('(')+1:ftype.rfind(')')].split(',')
    params = []
    for p in param_types:
        if p.strip():  # Check if not empty after stripping whitespace
            params.append(['const', 'param', p.strip()])  # Simplified; in real cases, names and const/var would vary
            
    return params

def parse_block(tokens, start_index=0):
    block = []
    i = start_index

    while i < len(tokens):
        token, value = tokens[i]
        match token:
            case 'CONST' | 'VAR':
                decl_type = 'const' if token == 'CONST' else 'var'
                _, name = tokens[i+1]
                if tokens[i+2][0] == "TYPE" or tokens[i+2][0] == "ARRAY_TYPE":
                    _, type_ = tokens[i+2]
                    i += 3  # Move past type
                    if tokens[i][0] == 'ASSIGN':
                        i += 1  # Skip '='
                        val = []
                        if tokens[i][0] == 'ARRAY_INIT':
                            val = tokens[i][1]
                        else:
                            while tokens[i][0] != 'END':
                                val.append(tokens[i][1])
                                i += 1
                        block.append([decl_type, name, type_, '=', val])
                        i += 1  # Skip 'END' or extra increment from loop
                elif tokens[i+2][0] == "FTYPE":
                    _, ftype = tokens[i+2]
                    
                    params = parse_function_parameters(ftype)
                    i += 4  # Adjust to after 'FTYPE', considering '='
                    if tokens[i][0] == 'LPAREN':

                        i += 1  # Skip 'LPAREN'
                        j = 0
                        t = 0
                        while tokens[i][0] != 'RPAREN':
                            if tokens[i][0] == 'IDENT':
                                if params[t][1] == 'param':
                                    params[t][1] = tokens[i][1]
                                    t = t + 1
                                    
                                
                            
                            i += 1  # Skipping parameters parsing for now
                        i += 1  # Skip 'RPAREN'
                    if tokens[i][0] != 'LBRACE':
                        raise ValueError("Expected '{' at the start of function body")
                    i += 1  # Skip '{'
                    function_body, i = parse_block(tokens, i)
                    block.append([decl_type, name, ftype, '=', [params, function_body]])
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
                i += 1  # Skip ')'
                if tokens[i][0] != 'LBRACE':
                    raise ValueError("Expected '{' after IF condition")
                i += 1  # Skip '{'
                if_body, i = parse_block(tokens, i)
                current_block = ['if', condition, if_body]
                if i < len(tokens) and tokens[i][0] == 'ELSE':
                    i += 1  # Skip 'ELSE'
                    if tokens[i][0] == 'LBRACE':
                        i += 1  # Skip '{'
                        else_body, i = parse_block(tokens, i)
                        current_block.append(['else', else_body])
                block.append(current_block)
            case 'RETURN':
                expr = []
                i += 1  # Skip 'RETURN'
                while tokens[i][0] != 'END':
                    expr.append(tokens[i][1])
                    i += 1
                block.append(['return', expr])
                i += 1  # Skip 'END'
            case 'RBRACE':
                i += 1  # Move past the closing brace
                return block, i
            case _:
                i += 1  # Skip unrecognized tokens or handling for other future cases

    return block, i



# Use the corrected parse_block in the parse function
def parse(tokens):
    structured_format, _ = parse_block(tokens)
    return structured_format
