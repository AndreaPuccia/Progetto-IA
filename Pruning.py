# esegue il test sul validation test valutando un dato alla volta
def TestDataPruning(tree, data):
    for i in range(data.__len__()):
        query = data.iloc[i]
        TestQueryPruning(tree.root, query)


# testa l'albero su un dato
def TestQueryPruning(node, query):
    if node.getY() != query['Y']:
            node.incError()
    if node.leaf == False:
        a = node.getAttribute()
        child = node.getChild(query[a])
        return TestQueryPruning(child, query)


# effettua il pruning elimina un nodo
# se i figli sono delle foglie & se la somma degli errori dei figli è maggiore degli errori del nodo
def pruneWalk(node):
    if node.leaf == False:
        for i in node.children:
            pruneWalk(node.getChild(i))
        if node.childrenLeaf() == True:
            errchild = node.childrenError()
            if errchild > node.error:
                node.children = {}
                node.leaf = True


def Pruning(tree, validation_set):
    TestDataPruning(tree, validation_set)
    pruneWalk(tree.root)
    return tree
