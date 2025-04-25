from token import *

class Lexer:
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.length = len(text)

    def get_tokens(self):
        tokens = []
        while self.index < self.length:
            ch = self.text[self.index]
            if ch.isspace():
                self.index += 1
                continue
            if ch.isdigit() or ch == '.':
                start_idx = self.index
                num_str = ''
                dot_count = 0
                if ch == '.':
                    num_str = '0.'
                    dot_count = 1
                    self.index += 1
                while self.index < self.length and (self.text[self.index].isdigit() or self.text[self.index] == '.'):
                    if self.text[self.index] == '.':
                        if dot_count == 1:
                            raise Exception(f'Multiple dots in number at {self.index}')
                        dot_count += 1
                    num_str += self.text[self.index]
                    self.index += 1
                tokens.append(Token(NUMBER, float(num_str), start_idx))
                continue
            if ch.isalpha():
                start_idx = self.index
                ident = ''
                while self.index < self.length and self.text[self.index].isalpha():
                    ident += self.text[self.index]
                    self.index += 1
                ident = ident.lower()
                if ident == 'true':
                    tokens.append(Token(BOOL, True, start_idx))
                elif ident == 'false':
                    tokens.append(Token(BOOL, False, start_idx))
                elif ident == 'and':
                    tokens.append(Token(AND, None, start_idx))
                elif ident == 'or':
                    tokens.append(Token(OR, None, start_idx))
                elif ident == 'not':
                    tokens.append(Token(NOT, None, start_idx))
                else:
                    raise Exception(f'Unknown identifier {ident}')
                continue
            if ch == '+':
                tokens.append(Token(PLUS, None, self.index))
                self.index += 1
                continue
            if ch == '-':
                tokens.append(Token(MINUS, None, self.index))
                self.index += 1
                continue
            if ch == '*':
                tokens.append(Token(MUL, None, self.index))
                self.index += 1
                continue
            if ch == '/':
                tokens.append(Token(DIV, None, self.index))
                self.index += 1
                continue
            if ch == '(':
                tokens.append(Token(LPAREN, None, self.index))
                self.index += 1
                continue
            if ch == ')':
                tokens.append(Token(RPAREN, None, self.index))
                self.index += 1
                continue
            if ch == '=':
                if self.index + 1 < self.length and self.text[self.index + 1] == '=':
                    tokens.append(Token(EQ, None, self.index))
                    self.index += 2
                    continue
            if ch == '!':
                if self.index + 1 < self.length and self.text[self.index + 1] == '=':
                    tokens.append(Token(NEQ, None, self.index))
                    self.index += 2
                    continue
                else:
                    tokens.append(Token(NOT, None, self.index))
                    self.index += 1
                    continue
            if ch == '<':
                if self.index + 1 < self.length and self.text[self.index + 1] == '=':
                    tokens.append(Token(LE, None, self.index))
                    self.index += 2
                    continue
                else:
                    tokens.append(Token(LT, None, self.index))
                    self.index += 1
                    continue
            if ch == '>':
                if self.index + 1 < self.length and self.text[self.index + 1] == '=':
                    tokens.append(Token(GE, None, self.index))
                    self.index += 2
                    continue
                else:
                    tokens.append(Token(GT, None, self.index))
                    self.index += 1
                    continue
            raise Exception(f'Unknown character {ch} at {self.index}')
        return tokens
