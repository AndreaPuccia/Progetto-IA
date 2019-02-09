def TestData(tree, data):
    error = 0
    for i in range(data.__len__()):
        query = data.iloc[i]
        if query['Y'] != TestQuery(tree.root, query):
            error = error+1
    return error


def TestQuery(node, query):
    if node.leaf == False:
        a = node.getAttribute()
        child = node.getChild(query[a])
        return TestQuery(child, query)
    else:
        return node.getY()
