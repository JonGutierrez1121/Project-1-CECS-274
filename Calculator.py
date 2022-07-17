#import BinaryTree
#import ChainedHashTable
import DLList
#import operator
import numpy as np
import ArrayStack

class Calculator:
    def __init__(self) :
        self.dict = None #ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k :str, v : float) :
        self.dict.add(k,v)
        
    def matched_expression(self, s : str) -> bool :
        stack = ArrayStack.ArrayStack()
        for char in s:
            if char == ')':
                if stack.size() == 0:
                    return False
                else:
                    stack.pop()
            elif char == '(':
                stack.push(char)
        if stack.size() >= 1:
            return False
        else:
            return True

    def build_parse_tree(self, exp : str) ->str:
        # todo
        pass 

    def _evaluate(self, root):
        op = { '+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        # todo
        pass 

    def evaluate(self, exp):
        parseTree = self.build_parse_tree(exp)
        return self._evaluate(parseTree.r)
        
        
