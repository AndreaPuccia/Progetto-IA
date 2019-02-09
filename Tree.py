class tree:

    def __init__(self, root):
        self.root = root
        self.nodes = 0

    def countNodes(self):
        self.nodes = self.root.countNodes()
        print(self.nodes)
