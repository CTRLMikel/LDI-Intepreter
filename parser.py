# parser.py

from ast_nodes import *
from token import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.current_token = tokens[0] if tokens else None

    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = None

    def parse(self):
        if self.current_token is None:
            return None
        node = self.parse_or()
        if self.current_token is not None:
            raise Exception("Invalid syntax")
        return node

    def parse_or(self):
        node = self.parse_and()
        while self.current_token is not None and self.current_token.type == OR:
            op_token = self.current_token
            self.advance()
            right = self.parse_and()
            node = BinOpNode(node, op_token, right)
        return node

    def parse_and(self):
        node = self.parse_equality()
        while self.current_token is not None and self.current_token.type == AND:
            op_token = self.current_token
            self.advance()
            right = self.parse_equality()
            node = BinOpNode(node, op_token, right)
        return node

    def parse_equality(self):
        node = self.parse_comparison()
        while self.current_token is not None and self.current_token.type in (EQ, NEQ):
            op_token = self.current_token
            self.advance()
            right = self.parse_comparison()
            node = BinOpNode(node, op_token, right)
        return node

    def parse_comparison(self):
        node = self.parse_additive()
        while self.current_token is not None and self.current_token.type in (LT, GT, LE, GE):
            op_token = self.current_token
            self.advance()
            right = self.parse_additive()
            node = BinOpNode(node, op_token, right)
        return node

    def parse_additive(self):
        node = self.parse_term()
        while self.current_token is not None and self.current_token.type in (PLUS, MINUS):
            op_token = self.current_token
            self.advance()
            right = self.parse_term()
            node = BinOpNode(node, op_token, right)
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.current_token is not None and self.current_token.type in (MUL, DIV):
            op_token = self.current_token
            self.advance()
            right = self.parse_factor()
            node = BinOpNode(node, op_token, right)
        return node

    def parse_factor(self):
        token = self.current_token
        if token is None:
            raise Exception("Invalid syntax")
        if token.type == PLUS:
            self.advance()
            return self.parse_factor()
        if token.type == MINUS:
            self.advance()
            return UnaryOpNode(token, self.parse_factor())
        if token.type == NOT:
            self.advance()
            return UnaryOpNode(token, self.parse_factor())
        if token.type == NUMBER:
            self.advance()
            return NumberNode(token.value)
        if token.type == BOOL:
            self.advance()
            return BoolNode(token.value)
        if token.type == LPAREN:
            self.advance()
            node = self.parse_or()
            if self.current_token is None or self.current_token.type != RPAREN:
                raise Exception("Mismatched parentheses")
            self.advance()
            return node
        raise Exception(f"Invalid syntax at position {token.position}")
