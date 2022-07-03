#
#
#  KNN *doar* pentru autocorelatie (fisier.csv)


import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score


#daca nota identificata nu corespunde cu numele fisierului, este identificata gresit
def identificate_gresit(nume_fisiere, y):
    linii = nume_fisiere.shape[0]                           #totalul liniilor
    # print(nume_fisier[:7])
    # print(X[:7])
    nr = 0                                                  #numarul de note gresite
    linii_gresite = []
    for i in range(linii-1):                                #index pentru fiecare linie (prima linie exclusa automat)
        if nume_fisiere[i][2] == "#":
            nota = nume_fisiere[i][:3]                      #se extrage numele notei de pe linia curenta -> note cu #
        else:
            nota = nume_fisiere[i][:2]                      #se extrage numele notei de pe linia curenta -> note fara #
        if sorted(y[i]) != sorted(nota):                    #cazul: nume = A5# , j = A#5 -> sunt egale
            nr += 1
            linii_gresite.append(i+2)
            print("Nota identificata gresit in Excel pe randul {}, nota adevarata {}, nota falsa {}.".format(i+2, nota, y[i]))
    print("\nNumar note identificate gresit: {}.".format(nr))
    return linii_gresite, nr, y


#se sterge greseala din fiecare variabila(nume_fisier, frecvente, note)
def stergere_gresite(nume_fisiere, X, y, linii_gresite):
    # randul din excel este cu 2 mai mare(1 pt randul de titlu + 1 pt ca index-ul incepe de la 0)
    nume_fisiere = np.delete(nume_fisiere, [i - 2 for i in linii_gresite], axis=0)
    X = np.delete(X, [i - 2 for i in linii_gresite], axis=0)
    y = np.delete(y, [i - 2 for i in linii_gresite], axis=0)
    return nume_fisiere, X, y


#label-urile identificate gresit se schimba cu cele date de numele fisierului
def schimbare_label(linii_gresite, nume_fisiere, y):
    for i in linii_gresite:
        if nume_fisiere[i-2][2] == "#":
            y[i-2] = nume_fisiere[i-2][:3]
        else:
            y[i-2] = nume_fisiere[i-2][:2]
    print("\nS-au schimbat label-urile. Verificam daca mai sunt label-uri gresite...")

    print("\nLabel-uri dupa schimbare:\n", y)

    return identificate_gresit(nume_fisiere, y)


def recunoastere(path_rezultat):
    # se creeaza setul de date din csv-ul generat dupa procesare
    dataset = pd.read_csv(path_rezultat)
    # print(dataset)
    # print(type(dataset))

    # datele se impart in coloane (coloana de titlu exclusa automat)
    # numele fisierelor
    nume_fisiere = dataset.iloc[:, 0].values
    # frecvente
    frecvente = dataset.iloc[:, 1].values
    # note identificate
    note = dataset.iloc[:, 2].values

    X = frecvente           #feature-uri, independente
    y = note                #label-uri/clase, dependente de feature-uri
    # print(X, y)
    # print(type(X), X.shape)
    # print(type(y), y.shape)

    # script detectie note gresite
    linii_gresite, nr, y = identificate_gresit(nume_fisiere, y)
    if nr:
        print("\nPuteti sterge liniile gresite sau sa puneti fortat label-ul corect. Excel-ul nu se va modifica.")
        ans = int(input("\nDorti sa: stergeti liniile gresite (1), puneti label-ul corect (2), lasati asa (3) "
                        "sau exit (4)? "))
        if ans == 1:
            # se sterg nota gresita, numele fisierului si frecventa ei
            nume_fisiere, X, y = stergere_gresite(nume_fisiere, X, y, linii_gresite)
            print('\nStergerea liniilor gresite a avut loc cu succes! Antrenati reteaua doar cu note identificate corect.')
            # # print(X[:12])           ->  verificare stergere
            # # print(X.shape[0])       -> ex. Excel cu autocorelatie: 370 note, 29 greseli rezulta 341 note bune
        elif ans == 2:
            linii_gresite, nr, y = schimbare_label(linii_gresite, nume_fisiere, y)
        elif ans == 3:
            print("\nAntrenati reteaua cu note identificate gresit.")
        elif ans == 4:
            return 0
    else:
        print("\nToate notele au fost identificate corect. Antrenati reteaua cu note identificate corect.\n")



    # impartire date in set de train si set de testare
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
    print('\n\n', 'X_train=\n', X_train, '\n\n', 'X_test=\n', X_test, '\n\n', 'y_train=\n', y_train,
          '\n\n', 'y_test=\n', y_test)


    # K Nearest Neighbor
    # 3 parameters in the model creation:
    # 1. n_neighbors = 5 neighborhood point required for classifying a point
    # 2. distance metric = Minkowski, check equation
    # 3. p = 2, Euclidean distance, parameter in Minkowski equation
    classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
    classifier.fit(X_train.reshape(-1, 1), y_train)

    y_pred = classifier.predict(X_test.reshape(-1, 1))
    print('\n', 'y_pred=\n', y_pred)

    cm = confusion_matrix(y_test, y_pred)
    ac = accuracy_score(y_test, y_pred)
    print('\n', 'cm=\n', cm, 'ac= ', ac)
