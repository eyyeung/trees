class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self,leftNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(leftNode)
        else:
            # if there is an exsisting child, we are pushing the existing child one down and have the new left be our direct child
            branch = BinaryTree(leftNode)
            branch.leftChild = self.leftChild
            self.leftChild = branch

    def insertRight(self,rightNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(rightNode)
        else:
            # if there is an exsisting child, we are pushing the existing child one down and have the new left be our direct child
            branch = BinaryTree(rightNode)
            branch.rightChild = self.rightChild
            self.rightChild = branch

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

def main():
    r = BinaryTree("A")
    print(r.getRootVal()) #A
    print(r.getLeftChild()) #None
    r.insertLeft("B")
    print(r.getLeftChild()) # BinaryTree object
    print(r.getLeftChild().getRootVal()) #C
    r.insertRight("C")
    print(r.getRightChild()) # BinaryTree object
    print(r.getRightChild().getRootVal()) # C
    r.getRightChild().setRootVal("D")
    print(r.getRightChild().getRootVal()) # D
    r.insertRight("E") # inserting another right child when one already exists(D) would push D downward to be E's child
    print(r.getRightChild().getRootVal()) # E
    print(r.getRightChild().getRightChild().getRootVal()) #D
#main()