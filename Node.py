class node:
    nodi = 0

    def __init__(self):
        self.Y = None
        self.attribute = " "
        self.children = {}
        self.leaf = False
        self.error = 0

    def countNodes(self):
        node.nodi = 0
        self.count()
        return node.nodi

    def count(self):
        node.nodi = node.nodi + 1
        for i in self.children:
            self.children[i].count()

    def getChild(self, value):
        nodo = self.children[value]
        return nodo

    def getAttribute(self):
        return self.attribute

    def getY(self):
        return self.Y

    def setY(self, y):
        self.Y = y

    def setAttribute(self, attr):
        self.attribute = attr

    def setChild(self, child, val):
        self.children[val] = child

    def incError(self):
        self.error = self.error+1

    # controlla se i figli di un nodo passato come parametro sono foglie
    def childrenLeaf(self):
        r = True
        for i in self.children:
            r = r and self.children[i].leaf
        return r

    # calcola il numero di errori dei figli di un nodo
    def childrenError(self):
        error = 0
        for i in self.children:
            error = error+self.children[i].error
        return error
