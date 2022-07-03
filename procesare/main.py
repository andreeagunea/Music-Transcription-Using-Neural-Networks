import autocorelatie
import spectograma
import cepstrum
import knn
import kmeans
import os
#from cauta_csv import cauta_csv

def procesare(path_folder_note, path_rezultat):
    print("\nAti ales sa faceti procesare pe {} "
          "\nsi sa returnati {}.".format(path_folder_note, path_rezultat))

    tipuri = [None, 'autocorelatie', 'spectograma', 'cepstrum']
    raspuns = int(input("\nTip procesare dorit: autocorelatie(1), spectograma(2), cepstrum(3) sau skip procesare(0). "))

    if raspuns:
        print("\nPentru procesare, ati ales: {}.".format(tipuri[raspuns]) + "\nSe proceseaza...")

        functie = tipuri[raspuns] + '.procesare(path_folder_note, path_rezultat)'
        eval(functie)

    return 0


def recunoastere(path_rezultat):
    print("\nAti ales sa faceti recunoastere pe {}.".format(path_rezultat))

    tipuri = [None, 'knn', 'kmeans']
    raspuns = int(input("\nTip machine learning algorithm dorit: k-nn(1), k-means(2) sau skip ML(0). "))

    if raspuns:
        print("\nPentru recunoastere, ati ales: {}.".format(tipuri[raspuns]) + "\nSe clasifica...")

        functie = tipuri[raspuns] + '.recunoastere(path_rezultat)'
        eval(functie)

    return 0


if __name__ == '__main__':
    path_proiect = os.getcwd()

    # Rezultatul poate fi:
    #                       autocorelatie:  test1.csv      (ex.: autocor_test_filtrate.csv)
    #                       spectograma:    test1          (ex.: spectograme_train_filtrate)
    folder_note = 'note_trainsitest'
    rezultat_procesare = 'autocor_trainsitest.csv'

    path_folder_note = r'{}'.format(os.path.join(os.getcwd(), folder_note))
    path_rezultat = r'{}'.format(os.path.join(os.getcwd(), rezultat_procesare))

    procesare(path_folder_note, path_rezultat)
    recunoastere(path_rezultat)

    # 17 gresite in train + 14 gresite in test
    # 21 gresite in train_filtrate + 15 gresite in test
