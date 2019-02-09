import pandas as pd
from Learning import DT_Learn
import sklearn.utils as sku
from Testing import TestData
from Pruning import Pruning
from Tree import tree
import numpy as np


print("Dataset Plant")
# preparo i dati li leggo dal file e li divido in training_set & validation_set & test_set
data = pd.read_csv('plant-classification.csv', names=['A', 'B', 'C', 'D', 'E', 'F', 'Y'])
data = sku.shuffle(data, random_state=967).reset_index(drop=True)
training_set = data.iloc[0:1400].reset_index(drop=True)
validation_set = data.iloc[1400:2000].reset_index(drop=True)
test_set = data.iloc[2000:].reset_index(drop=True)
# preparo i parametri da passare a DT_Learn
attr = {}
attr['A'] = np.unique(data['A'])
attr['B'] = np.unique(data['B'])
attr['C'] = np.unique(data['C'])
attr['D'] = np.unique(data['D'])
attr['E'] = np.unique(data['E'])
attr['F'] = np.unique(data['F'])
pData = []
# creo l'albero di decisione
# albero non potato
tree0 = tree(DT_Learn(training_set, attr, pData))
print("Albero Non Potato")
print("Nodi: ", end="")
tree0.countNodes()
print("")
# testo l'albero sul Training-Set
err = TestData(tree0, training_set)
print("Errori sul Training-Set: ", err)
print("Errore Percentuale sul Training-Set: ", (round((err/training_set.__len__())*100, 4)), "%")
print("")
# testo l'albero sul Test-Set
err = TestData(tree0, test_set)
print("Errori sul Test-Set: ", err)
print("Errore Percentuale sul Test-Set: ", (round((err/test_set.__len__())*100, 4)), "%")
print("")
# albero potato
pruningTree = Pruning(tree0, validation_set)
print("Albero Potato")
print("Nodi: ", end="")
pruningTree.countNodes()
print("")
# testo l'albero sul Training-Set
err = TestData(pruningTree, training_set)
print("Errori sul Training-Set: ", err)
print("Errore Percentuale sul Training-Set: ", (round((err/training_set.__len__())*100, 4)), "%")
print("")
# testo l'albero sul Test-Set
err = TestData(pruningTree, test_set)
print("Errori sul Test-Set: ", err)
print("Errore Percentuale sul Test-Set: ", (round((err/test_set.__len__())*100, 4)), "%")

# ****************************************************************************************

print("")
print("Dataset Cars")
# preparo i dati li leggo dal file e li divido in training_set & validation_set & test_set
data1 = pd.read_csv('cars.csv', names=['A', 'B', 'C', 'D', 'E', 'F', 'Y'])
data1 = sku.shuffle(data1, random_state=276).reset_index(drop=True)
training_set1 = data1.iloc[0:1000].reset_index(drop=True)
validation_set1 = data1.iloc[1000:1350].reset_index(drop=True)
test_set1 = data1.iloc[1350:].reset_index(drop=True)
# preparo i parametri da passare a DT_Learn
attr1 = {}
attr1['A'] = np.unique(data1['A'])
attr1['B'] = np.unique(data1['B'])
attr1['C'] = np.unique(data1['C'])
attr1['D'] = np.unique(data1['D'])
attr1['E'] = np.unique(data1['E'])
attr1['F'] = np.unique(data1['F'])
pData1 = []
# creo l'albero di decisione
# albero non potato
tree1 = tree(DT_Learn(training_set1, attr1, pData1))
print("ALbero Non Potato")
print("Nodi: ", end="")
tree1.countNodes()
print("")
# testo l'albero sul Training-Set
err1 = TestData(tree1, training_set1)
print("Errori sul Training-Set: ", err1)
print("Errore Percentuale sul Training-Set: ", (round((err1/training_set1.__len__())*100, 4)), "%")
print("")
# testo l'albero sul Test-Set
err1 = TestData(tree1, test_set1)
print("Errori sul Test-Set: ", err1)
print("Errore Percentuale sul Test-Set: ", (round((err1/test_set1.__len__())*100, 4)), "%")
print("")
# albero potato
pruningTree1 = Pruning(tree1, validation_set1)
print("Albero Potato")
print("Nodi: ", end="")
pruningTree1.countNodes()
print("")
# testo l'albero sul Training-Set
err1 = TestData(pruningTree1, training_set1)
print("Errori sul Training-Set: ", err1)
print("Errore Percentuale sul Training-Set: ", (round((err1/training_set1.__len__())*100, 4)), "%")
print("")
# testo l'albero sul Test-Set
err1 = TestData(pruningTree1, test_set1)
print("Errori sul Test-Set: ", err1)
print("Errore Percentuale sul Test-Set: ", (round((err1/test_set1.__len__())*100, 4)), "%")

# ****************************************************************************************

print("")
print("Dataset Nursery")
# preparo i dati li leggo dal file e li divido in training_set & validation_set & test_set 676 519
data2 = pd.read_csv("nursery.csv", names=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'Y'])
data2 = sku.shuffle(data2, random_state=519).reset_index(drop=True)
training_set2 = data2.iloc[0:6400].reset_index(drop=True)
validation_set2 = data2.iloc[6400:9100].reset_index(drop=True)
test_set2 = data2.iloc[9100:].reset_index(drop=True)
# preparo i parametri da passare a DT_Learn
attr2 = {}
attr2['A'] = np.unique(data2['A'])
attr2['B'] = np.unique(data2['B'])
attr2['C'] = np.unique(data2['C'])
attr2['D'] = np.unique(data2['D'])
attr2['E'] = np.unique(data2['E'])
attr2['F'] = np.unique(data2['F'])
attr2['G'] = np.unique(data2['G'])
attr2['H'] = np.unique(data2['H'])
pData2 = []
# creo l'albero di decisione
# albero non potato
tree2 = tree(DT_Learn(training_set2, attr2, pData2))
print("Albero Non Potato")
print("Nodi: ", end="")
tree2.countNodes()
print("")
# testo l'albero sul Training-Set
err2 = TestData(tree2, training_set2)
print("Errori: ", err2)
print("Errore Percentuale: ", (round((err2/training_set2.__len__())*100, 4)), "%")
print("")
# testo l'albero sul Test-Set
err2 = TestData(tree2, test_set2)
print("Errori sul Test-Set: ", err2)
print("Errore Percentuale sul Test-Set: ", (round((err2/test_set2.__len__())*100, 4)), "%")
print("")
# albero potato
pruningTree2 = Pruning(tree2, validation_set2)
print("Albero Potato")
print("Nodi: ", end="")
pruningTree2.countNodes()
print("")
# testo l'albero sul Training-Set
err2 = TestData(pruningTree2, training_set2)
print("Errori sul Training-Set: ", err2)
print("Errore Percentuale sul Training-Set: ", (round((err2/training_set2.__len__())*100, 4)), "%")
print("")
# testo l'albero sul Test-Set
err2 = TestData(pruningTree2, test_set2)
print("Errori sul Test-Set: ", err2)
print("Errore Percentuale sul Test-Set: ", (round((err2/test_set2.__len__())*100, 4)), "%")

