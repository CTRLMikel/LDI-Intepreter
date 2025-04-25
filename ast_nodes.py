class ASTNode:
    pass

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

class BoolNode(ASTNode):
    def __init__(self, value):
        self.value = value

class BinOpNode(ASTNode):
    def __init__(self, left, op_token, right):
        self.left = left
        self.op_token = op_token
        self.op_type = op_token.type
        self.right = right

class UnaryOpNode(ASTNode):
    def __init__(self, op_token, operand):
        self.op_token = op_token
        self.op_type = op_token.type
        self.operand = operand
