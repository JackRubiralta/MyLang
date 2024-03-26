from Lexer.lexer import tokenize
from Parser.parser import parse
import json


x = [
['var', 'num1', 'int', '=', ['3']],
['num1', '=', ['2']],
['var', 'y', 'int', '=', ['5']],
['y', '=', ['y', '+', 'num1']],

['if', ['(', 'num1', '==', '2', ')'], [
    ['y', '=', ['y', '+', 'num1']], 
    ['var', 'h', 'int', '=', ['5']], 
    ['if', ['(', 'y', '>', '2', ')'], [
        ['y', '=', [1]]
    ]]
]], 
['else', 'if', ['(', 'num1', '==', '3', ')'], [
    ['y', '=', ['y', '+', '2']], 
    ['var', 'h', 'int', '=', ['3']]
]], 
['else', [
    ['y', '=', ['y', '-', 1]],
]],

['num1', '=', ['y', '+', ['(', 'num1', '-', 4, ')']]]
]


def write_structure_to_json(structure, file_path):
    with open(file_path, 'w') as file:
        json.dump(structure, file, indent=4)

def read_code_from_file(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    return code

def main():
    # Assume the paths might change based on your project structure
    code_file_path = './input_code/program.txt'
    output_json_path = './input_code/program.json'
    
    # Read code from file
    code = read_code_from_file(code_file_path)
    
    # Tokenize and parse
    tokens = list(tokenize(code))
    structured_format = parse(tokens)
    
    # Write the structured format to JSON
    write_structure_to_json(structured_format, output_json_path)
    print(structured_format)
    print(f"Parsed structure has been saved to {output_json_path}")

if __name__ == "__main__":
    main()
