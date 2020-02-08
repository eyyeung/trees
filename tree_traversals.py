from binary_trees import BinaryTree

# preorder, visit root node then left subtree node, child, up, then right subtree node, child, up
# root, left, right
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder.(tree.getLeftChild())
        preorder.(tree.getRightChild())
# inorder, go down to bottom most left subtree child first, then up to parent, up to root node then go down to right most child first, then up to parent
# left, root, right
def inorder(tree):
    if tree!= None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())



# postorder, left and right subtree from bottom to up, with root node last
# left, right, root
def postorder(tree):
    if tree!= None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

