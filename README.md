# Trees
## Description
Different kinds of trees and how to traverse / search / organize them
## Content
* binary_trees.py:
    * BinaryTree class
* binary_heaps.py
    * BinaryHeap class
* parse_trees.py
    * buildParseTree(math_exp) : parse a simple mathematical expression
* tree_traversals.py
    * preorder(tree)
    * inorder(tree)
    * postorder(tree)

## Testing
* binary_trees.
```python
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
```
* binary_heaps
```python
def main():
    bh = BinaryHeap()
    bh.buildHeap([9,5,6,2,3])
    print(bh.heaparray) 

    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
```
* parse_tree
```python
# expression needs to be of form "((5+2)*3)", only uses (),+,-,/,*, and integer numbers
math1=buildParseTree("( ( 10 + 5 ) * 3 )")
print(inorder(math1))
print(printexp(math1))
print('=',evaluate(math1))
```