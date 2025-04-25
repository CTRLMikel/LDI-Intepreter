NUMBER = 'NUMBER'
BOOL = 'BOOL'
PLUS = 'PLUS'
MINUS = 'MINUS'
MUL = 'MUL'
DIV = 'DIV'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
EQ = 'EQ'
NEQ = 'NEQ'
LT = 'LT'
GT = 'GT'
LE = 'LE'
GE = 'GE'
AND = 'AND'
OR = 'OR'
NOT = 'NOT'

class Token:
    def __init__(self, type, value=None, position=None):
        self.type = type
        self.value = value
        self.position = position

    def __repr__(self):
        return f'Token({self.type}, {self.value})'
