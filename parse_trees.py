from binary_trees import BinaryTree
from stacks import Stack

def buildParseTree(math_exp):
    mlist = math_exp.split()
    pStack = Stack()
    aTree = BinaryTree('')
    pStack.push(aTree)
    currentTree = aTree

    for num in mlist:
        # When we see open bracket, make a left child node since number will go there
        if num == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        # if it is operator, we set that parent to be the operator then make a right child
        elif num in ['+','-','*','/']:
            currentTree.setRootVal(num)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        # closing the bracket so go back to the parent of the operator node
        elif num == ')':
            currentTree = pStack.pop()

        # this is presume to be a number, want to set the current node to that number, then go back to the parent
        elif num not in ['+','-','*','/',')']:
            try:
                currentTree.setRootVal(int(num))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError(num,"is not a valid integer")
    return aTree

class Operator:
    def add(self,x,y):
        return x+y

    def sub(self,x,y):
        return x-y

    def mul(self,x,y):
        return x*y
    
    def div(self,x,y):
        return x/y
def to_int(astr):
    return int(astr)

def to_str(aint):
    return str(aint)

def evaluate(parseTree):
    Ope = Operator()
    left = parseTree.getLeftChild()
    right = parseTree.getRightChild()

    # if both exists
    if (right and left):
        if parseTree.getRootVal() == '+':
            return to_str(Ope.add(to_int(evaluate(left)),to_int(evaluate(right))))
        elif parseTree.getRootVal() == '-':
            return to_str(Ope.sub(to_int(evaluate(left)),to_int(evaluate(right))))
        elif parseTree.getRootVal() == '*':
            return to_str(Ope.mul(to_int(evaluate(left)),to_int(evaluate(right))))
        elif parseTree.getRootVal() == '/':
            return to_str(Ope.div(to_int(evaluate(left)),to_int(evaluate(right))))
    else:
        return parseTree.getRootVal()

def printexp(tree):
    output = ""
    if tree!=None:
        output = "("+printexp(tree.getLeftChild())
        output += str(tree.getRootVal())
        output += (str(printexp(tree.getRightChild()))+')')
    return output


def inorder(tree):
    if tree!=None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())



# expression needs to be of form "((5+2)*3)", only uses (),+,-,/,*, and integer numbers
math1=buildParseTree("( ( 10 + 5 ) * 3 )")
print(inorder(math1))
print(printexp(math1))
print('=',evaluate(math1))