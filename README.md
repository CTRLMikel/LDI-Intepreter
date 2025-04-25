------------------------------------------------------------

✨ Features
------------
- Arithmetic operations: +, -, *, /
- Boolean logic: true, false, and, or, not
- Comparisons: <, >, <=, >=, ==, !=
- Parentheses for grouping: ( ... )
- Correct operator precedence
- Supports floating point numbers
- Strict type checking (no weird true + 1 mixing)

------------------------------------------------------------

📁 Project Structure
---------------------
├── token.py           (Token types and Token class)

├── lexer.py           (Lexer: turns input into tokens)

├── ast_nodes.py       (AST Node classes)

├── parser.py          (Parser: builds AST from tokens)

├── interpreter.py     (Interpreter: evaluates AST)

├── main.py            (Program entry point)

├── BUILD.txt          (Build instructions)

├── README.txt         (Project documentation)

└── examples/          (Example source files)

    ├── example1.txt
    ├── example2.txt
    ├── example3.txt
    ├── example4.txt
    └── example5.txt

------------------------------------------------------------

⚙️ How to Run
--------------
You need Python 3 installed.

1. Open a terminal inside the project folder.
2. Run:
   pip install -r requirements.txt
   python main.py examples/example1.txt

(You can replace example1.txt with any example file.)

------------------------------------------------------------

📝 Example Usage
------------------
Input (example1.txt):
    1 + 2
    3 * 4
    true and false
    !(1 < 2)

Output:
    3
    12
    false
    false

------------------------------------------------------------

❗ Error Handling
------------------
If an expression has invalid syntax or type errors,
the interpreter prints a friendly error message instead of crashing.

------------------------------------------------------------
