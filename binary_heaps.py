# uses a complete binary tree.
# node at n, parent at n/2, parent at p, left child 2p, right child 2p+1
# want the value at p to be less than or equal to the value of the child
# the root of the tree is the smallest item of the tree
class BinaryHeap:
    def __init__(self):
        self.heaparray = [0]
        self.size = 0

    def insert(self,item):
        self.heaparray.append(item)
        self.size += 1 # this would be the index
        self.perUp(self.size)

    def delMin(self):
        retval = self.heaparray[1]
        self.heaparray[1] = self.heaparray[self.size]
        self.size -= 1
        self.heaparray.pop()
        self.perDown(1)
        return retval

    def buildHeap(self, vec):
        i = len(vec)//2
        self.size = len(vec)
        self.heaparray = [0] + vec[:]
        while (i>0):
            self.perDown(i)
            i -= 1
        
    # want to maintain order, percolate an itme up
    def perUp(self,i):
        while ((i//2)>0):
            # if the value is less than the value of the parent, then want to make the parent the new value and make the old parent a child
            if (self.heaparray[i] < self.heaparray[i//2]):
                self.heaparray[i//2], self.heaparray[i] = self.heaparray[i], self.heaparray[i/2]
            i = i//2

    def perDown(self,i):
        while ((i*2) <= self.size):
            mc = self.minChild(i)
            if (self.heaparray[i] > self.heaparray[mc]):
                self.heaparray[i], self.heaparray[mc] = self.heaparray[mc], self.heaparray[i]
            i = mc

    # find the mininum child
    def minChild(self, i):
        # if the right child > this node
        if (i*2+1) > self.size:
            return i*2 # return the left child
        else:
            if (self.heaparray[2*i] < self.heaparray[2*i+1]):
                return i*2
            else:
                return 2*i+1


def main():
    bh = BinaryHeap()
    bh.buildHeap([9,5,6,2,3])
    print(bh.heaparray) 

    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())

main()