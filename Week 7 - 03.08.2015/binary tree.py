class binaryTree(object):
    def __init__(self, value):
        self.value=value
        self.leftBranch=None
        self.rightBranch=None
        self.parent=None
    def setLeftBranch(self, node):
        self.leftBranch=node
    def setRightBranch(self, node):
        self.rightBranch=node
    def setParent(self, parent):
        self.parent=parent

    def getValue(self):
        return self.value
    def getLeftBranch(self):
        return self.rightBranch
    def getRightBranch(self):
        return self.parent
    def __str__(self):
        return self.value
    # and other methods

n5 = binaryTree(5)
n2 = binaryTree(2)
n1 = binaryTree(1)
n4 = binaryTree(4)
n8 = binaryTree(8)
n6 = binaryTree(6)
n7 = binaryTree(7)
n3 = binaryTree(3)

n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)
n4.setLeftBranch(n3)
n3.setParent(n4)
