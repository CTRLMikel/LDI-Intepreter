# main.py

from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        lines = f.readlines()

    interpreter = Interpreter()

    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            lexer = Lexer(line)
            tokens = lexer.get_tokens()
            parser = Parser(tokens)
            ast = parser.parse()
            result = interpreter.evaluate(ast)
            if isinstance(result, bool):
                print(str(result).lower())
            else:
                print(result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
