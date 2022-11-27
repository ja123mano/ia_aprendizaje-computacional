from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier as KNC
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.neural_network import MLPClassifier as MLP

from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.metrics import confusion_matrix

import numpy as np
import pickle
import os

def datos():
    file = "images_descriptors.obj"
    descriptors_dict = dict()
    biomas_id = {"Agua":0, "Bosque":1, "Ciudad":2, "Cultivo":3, "Desierto":4, "Montaña":5}

    with open("images_descriptors.obj", "rb") as file:
        descriptors_dict = pickle.load(file)

    lista_llaves = sorted(list(descriptors_dict.keys()))
    y = np.array([biomas_id.get(etiqueta.split("_")[0]) for etiqueta in lista_llaves])
    x = np.array([descriptors_dict.get(bioma) for bioma in lista_llaves])

    return x, y

def classifier(x : np.array, y : np.array, cl : str="linear", k : int=5, knn : int=3, n_neurons : int=100, n_layers : int=3, iterations : int=1000, saveCLF : bool=False, nameCLF : str=None, verbose : bool=True):
    """
    Función que evalúa los el clasificador seleccionado 'cl' con los datos seleccionados.
    Imprime a consola el accuracy general y recall por clase con kfold y
    el accuracy y recall con cross-validation generales para el modelo clasificador.

    Parámetros
    ----------
    x : np.array
        Matriz con vectores de entrada para el clasificador.
    
    y : np.array
        Arreglo con las etiquetas correspondientes de cada vector en la matriz x.

    cl : str ["linear", "rbf", "knn", "tree", "NN"] - default linear
        El modelo del clasificador a usar

    k : int - default 5
        Número de splits a realizar por la validación cruzada.
    
    knn : int - default 3
        Si cl = knn, este representa la cantidad de vecinos.

    n_neurons : int - default 100
        Si cl = NN, establece el número de neuronas por capa para la red neuronal.

    n_layers : int - default 3
        Si cl = NN, establece el número de capas internas de la red neuronal.

    iterations : int - default 1000
        Si cl = NN, establece el número máximo de iteraciones para converger de la red neuronal.

    saveCLF : bool - default False
        Establece si quieres guardar el modelo clasificador dentro de un archivo serializado.
        El archivo se guardará en el working directory.
    
    nameCLF : str - default None
        Si saveCLF = True, establece el nombre del archivo en el cual se guardará el modelo clasificador.
        Si se deja como None, el nombre será el tipo del clasificador + str("Classifier.clf").
    
    verbose : bool - default True
        True para que la salida a consola describa al clasificador y arroje los resultados por cross validate.

    Regresa
    -------
    clf : sklearn.classifier
        Regresa el objeto del modelo clasificador de la librería sklearn.
    """

    kf = StratifiedKFold(n_splits=k, shuffle = True)
    clf = None

    if cl == "knn":
        clf = KNC(n_neighbors=knn)
    elif cl == "tree":
        clf = DTC()
    elif cl == "NN":
        layers = tuple([n_neurons for _ in range(n_layers)])
        clf = MLP(hidden_layer_sizes=layers, max_iter=iterations)
    elif cl == "linear" or cl == "rbf":
        clf = svm.SVC(kernel = cl)
    else:
        print("Porfavor selecciona un modelo dentro de las opciones\n")
        return -1

    if verbose:
        print("----------------------------------------------------------------")
        print(f"Clasificador {cl}")
        if cl == "knn":
            print(f"k = {knn}")
        elif cl == "NN":
            print(f"Neuronas = {n_neurons}\nCapas = {n_layers}")
        print()

    acc = 0

    recall = np.array([0.,0.,0.,0.,0.,0.])
    for train_index, test_index in kf.split(x, y):
        
        # Training phase
        x_train = x[train_index, :]
        y_train = y[train_index]
        clf.fit(x_train, y_train)

        # Test phase
        x_test = x[test_index, :]
        y_test = y[test_index]    
        y_pred = clf.predict(x_test)

        # Calculate confusion matrix and model performance
        cm = confusion_matrix(y_test, y_pred)
        # print('Confusion matrix\n', cm)
        
        acc += (cm[0,0]+cm[1,1]+cm[2,2]+cm[3,3]+cm[4,4]+cm[5,5])/len(y_test)
        recall[0] += cm[0,0]/(cm[0,0] + cm[0,1] + cm[0,2] + cm[0,3] + cm[0,4] + cm[0,5])
        recall[1] += cm[1,1]/(cm[1,0] + cm[1,1] + cm[1,2] + cm[1,3] + cm[1,4] + cm[1,5])
        recall[2] += cm[2,2]/(cm[2,0] + cm[2,1] + cm[2,2] + cm[2,3] + cm[2,4] + cm[2,5])
        recall[3] += cm[3,3]/(cm[3,0] + cm[3,1] + cm[3,2] + cm[3,3] + cm[3,4] + cm[3,5])
        recall[4] += cm[4,4]/(cm[4,0] + cm[4,1] + cm[4,2] + cm[4,3] + cm[4,4] + cm[4,5])
        recall[5] += cm[5,5]/(cm[5,0] + cm[5,1] + cm[5,2] + cm[5,3] + cm[5,4] + cm[5,5])

    # Print results
    acc = acc/k
    recall = recall/k
    print('Kfold\nAcc: ', acc)
    print('Recall: ', recall)

    if verbose:
        # 5-fold cross-validation using cross_validate
        cv_results = cross_validate(clf, x, y, cv=k, scoring = ('accuracy', 'recall_micro'))
        print("\nCross Validation")
        print('Acc: ', cv_results['test_accuracy'].sum()/k)
        print('Recall: ', cv_results['test_recall_micro'].sum()/k)
        print("----------------------------------------------------------------\n")

    if saveCLF:
        if nameCLF == None:
            with open(cl + "Classifier.clf", "wb") as CLFfile:
                pickle.dump(clf, CLFfile)
        else:
            with open(nameCLF + ".clf", "wb") as CLFfile:
                pickle.dump(clf, CLFfile)

    return clf

def main():
    modelos = ["linear", "rbf", "knn", "tree", "NN"]

    clasificador = input("""Seleccionar 1 tipo de clasificador (escribe el numero):
1. Lineal
2. RBF
3. KNN
4. Arbol
5. Red Neuronal

Selección: """)
    clasificador = int(clasificador)-1
    nombre = input("\nEscribe el nombre en el cual quieres guardar el modelo clasificador o dejalo en blanco si quieres el nombre por default: ")
    if nombre == "":
        nombre = None

    print()
    x, y = datos()
    classifier(x, y, modelos[clasificador], saveCLF=True, nameCLF=nombre, verbose=False)

if __name__ == "__main__":
    main()