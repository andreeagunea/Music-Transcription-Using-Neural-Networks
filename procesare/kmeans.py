import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans


#daca nota identificata nu corespunde cu numele fisierului, este identificata gresit
def identificate_gresit(nume_fisiere, y):
    linii = nume_fisiere.shape[0]                           #totalul liniilor
    # print(nume_fisier[:7])
    # print(X[:7])
    nr = 0                                                  #numarul de note gresite
    linii_gresite = []
    for i in range(linii-1):                                #index pentru fiecare linie (prima linie exclusa automat)
        nota = nume_fisiere[i][:2]                          #se extrage numele notei de pe linia curenta -> note fara #
        if nume_fisiere[i][2] == "#":
            nota = nume_fisiere[i][:3]                      #se extrage numele notei de pe linia curenta -> note cu #
        if sorted(y[i]) != sorted(nota):                    #cazul: nume = A5# , j = A#5 -> sunt egale
            nr += 1
            linii_gresite.append(i+2)
            print("Nota identificata gresit in Excel pe randul {}, nota adevarata {}, nota falsa {}.".format(i+2, nota, y[i]))
    print("\nNumar note identificate gresit: {}.".format(nr))
    return linii_gresite, nr


#se sterge greseala din fiecare variabila(nume_fisier, frecvente, note)
def stergere_gresite(nume_fisiere, X, y, linii_gresite):
    # randul din excel este cu 2 mai mare(1 pt randul de titlu + 1 pt ca index-ul incepe de la 0)
    nume_fisiere = np.delete(nume_fisiere, [i - 2 for i in linii_gresite], axis=0)
    X = np.delete(X, [i - 2 for i in linii_gresite], axis=0)
    y = np.delete(y, [i - 2 for i in linii_gresite], axis=0)
    return nume_fisiere, X, y

def clasificare():
    # se creeaza setul de date din csv-ul generat dupa procesare
    dataset = pd.read_csv('output1.csv')
    # print(dataset)
    # print(type(dataset))

    # datele se impart in coloane (coloana de titlu exclusa automat)
    # numele fisierelor
    nume_fisiere = dataset.iloc[:, 0].values
    # frecvente
    frecvente = dataset.iloc[:, 1].values
    # note identificate
    note = dataset.iloc[:, 2].values

    X = frecvente  # feature-uri, independente
    y = note  # label-uri/clase, dependente de feature-uri
    # print(X, y)
    # print(type(X), X.shape)
    # print(type(y), y.shape)

    # script detectie note gresite
    linii_gresite, nr = identificate_gresit(nume_fisiere, y)
    if nr:
        print("\nPuteti sterge liniile gresite. Nu vor fi sterse din Excel, ci doar din variabile")
        ans = int(input("\nDoriti sa stergeti notele gresite in antrenarea retelei? da(1), nu(0). "))
        if ans:
            # se sterg nota gresita, numele fisierului si frecventa ei
            nume_fisiere, X, y = stergere_gresite(nume_fisiere, X, y, linii_gresite)
            print('\nStergerea notelor gresite a avut loc cu succes! Antrenati reteaua cu note identificate corect.')
            # # print(X[:12])           ->  verificare stergere
            # # print(X.shape[0])       -> ex. Excel cu autocorelatie: 370 note, 29 greseli rezulta 341 note bune

            dataset_vechi = dataset
            concat = np.column_stack((nume_fisiere, X, y))
            # print(concat)

            # refacere dataset de note corecte
            column_values = ['file_name', 'note_freq', 'note_name']
            index_values = [i for i in range(int(X.shape[0]))]
            dataset = pd.DataFrame(data=concat,
                              index=index_values,
                              columns=column_values)
            # print(dataset)

        else:
            print("\nAntrenati reteaua cu note gresite.")
    else:
        print("\nToate notele au fost identificate corect. Antrenati reteaua cu note identificate corect.\n")

    # Plot cu frecvente(indici).
    indici = np.arange(1, len(X) + 1)
    plt.figure(1)
    plt.scatter(indici, X)

    X = X.reshape(-1,1)
    kmeans = KMeans(n_clusters=37)
    kmeans.fit(X)

    identified_cluters = kmeans.fit_predict(X)
    # print(identified_cluters)

    data_with_clusters = dataset.copy()
    data_with_clusters['Clusters'] = identified_cluters
    # print(data_with_clusters)
    print(data_with_clusters['Clusters'])

    # Plot cu clusterele pentru frecvente(indici).
    plt.figure(2)
    plt.scatter(indici, data_with_clusters['note_freq'],
                c=data_with_clusters['Clusters'], cmap='rainbow')
    plt.show()


# Bibliografie:
# https://www.analyticsvidhya.com/blog/2021/04/k-means-clustering-simplified-in-python/
