import numpy as np
from Node import node

# implementazione algoritmo DT-Learn
def DT_Learn(data, attrs, pData):
    if data.__len__() == 0:
        return mostCommon(pData)
    else:
        if Control_1(data):
            return mostCommon(data)
        else:
            if((attrs.__len__()) == 0):
                return mostCommon(data)
            else:
                # calcolo il guadagno e scelgo l'attribbuto che realizza il massimo guadagno
                earning = gain(data, attrs)
                i = np.argmax(earning)
                A = attrs[i]
                # calcolo la classe del nodo cioè la classe più presente nel dataset corrente
                classe, num = np.unique(data['Y'], return_counts=True)
                i = np.argmax(num)
                y = classe[i]
                # creo il nuovo nodo
                newNode = node()
                newNode.setAttribute(A)
                newNode.setY(y)
                val = np.unique(data[A])
                attrs.remove(A)
                for i in range(val.__len__()):
                    data2 = data.where(data[A] == val[i]).dropna()
                    nodo = DT_Learn(data2, attrs, data)
                    newNode.setChild(nodo, val[i])
                attrs.append(A)
                return newNode

# calcolo l'entropia
def entropy(data):
    val, num = np.unique(data['Y'], return_counts=True)
    entropy = np.sum([- num[i]/ np.sum(num) * np.log2(num[i]/ np.sum(num)) for i in range(len(val))])
    return entropy
# calcolo l'entropia relaztiva aciascun attributo
def attribute_entropy(data, attr):
    a_entropy = 0
    val, num = np.unique(data[attr], return_counts=True)
    for i in range(val.__len__()):
        data2 = data.where(data[attr] == val[i]).dropna()
        a_entropy += (num[i] / data.__len__()) * entropy(data2)
    return np.sum(a_entropy)

# calcolo il guadagno
def gain(data, attribute):
    # calcolo l'entropia dell'intero dataset
    total_entropy = entropy(data)

    attr_entropy = []
    for i in range(0, attribute.__len__()):
        attr_entropy.append(attribute_entropy(data, attribute[i]))
    return total_entropy-attr_entropy

# ritorno un nodo contenente l'informazione sulla classe più frequente
def mostCommon(data):
    NewNode = node()
    val, num = np.unique(data['Y'], return_counts=True)
    i = np.argmax(num)
    NewNode.setY(val[i])
    NewNode.leaf = True
    return NewNode

# controllo che tutti i dati di un dataset siano della stessa classe
def Control_1(data):
    val, num = np.unique(data['Y'], return_counts=True)
    if np.count_nonzero(num) == 1:
        return True
    else:
        return False
