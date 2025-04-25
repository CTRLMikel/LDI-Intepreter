# interpreter.py

from token import *
from ast_nodes import *

class Interpreter:
    def evaluate(self, node):
        if isinstance(node, NumberNode):
            return node.value
        if isinstance(node, BoolNode):
            return node.value
        if isinstance(node, UnaryOpNode):
            val = self.evaluate(node.operand)
            if node.op_type == MINUS:
                if isinstance(val, bool):
                    raise Exception("Unary '-' applied to boolean")
                return -val
            if node.op_type == NOT:
                if not isinstance(val, bool):
                    raise Exception("'not' applied to non-boolean")
                return not val
        if isinstance(node, BinOpNode):
            if node.op_type in (AND, OR):
                left = self.evaluate(node.left)
                if not isinstance(left, bool):
                    raise Exception("Boolean operation on non-boolean")
                if node.op_type == AND:
                    return left and self.evaluate(node.right)
                else:
                    return left or self.evaluate(node.right)

            left = self.evaluate(node.left)
            right = self.evaluate(node.right)

            if node.op_type == PLUS:
                if isinstance(left, bool) or isinstance(right, bool):
                    raise Exception("Type error: '+' expects numbers")
                return left + right
            if node.op_type == MINUS:
                if isinstance(left, bool) or isinstance(right, bool):
                    raise Exception("Type error: '-' expects numbers")
                return left - right
            if node.op_type == MUL:
                if isinstance(left, bool) or isinstance(right, bool):
                    raise Exception("Type error: '*' expects numbers")
                return left * right
            if node.op_type == DIV:
                if isinstance(left, bool) or isinstance(right, bool):
                    raise Exception("Type error: '/' expects numbers")
                if right == 0:
                    raise Exception("Division by zero")
                return left / right
            if node.op_type == EQ:
                return left == right
            if node.op_type == NEQ:
                return left != right
            if node.op_type == LT:
                return left < right
            if node.op_type == LE:
                return left <= right
            if node.op_type == GT:
                return left > right
            if node.op_type == GE:
                return left >= right
        raise Exception("Unknown node")
