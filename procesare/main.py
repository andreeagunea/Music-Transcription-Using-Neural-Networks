import os
import autocorelatie
import spectograma
import cepstrum
import knn
import kmeans
#from cauta_csv import cauta_csv

def notes_translate():
    ans_proc = int(input("Tip procesare dorit: autocorelatie(1), spectograma(2), cepstrum(3) sau skip procesare(0). "))
    if ans_proc == 1:
        print("\nPentru procesare, ati ales: autocorelatie.\n")

        path_proiect = os.getcwd()                 #asa nu mai trb sa schimbi path-ul bogdan cu andreea

        path_folder_note = r'{}'.format(os.path.join(path_proiect, 'note_train&test'))
        path_csv = r'{}'.format(os.path.join(path_proiect, 'autocor_train&test.csv'))

        # path_folder_note = r'{}'.format(os.path.join(path_proiect, 'note_train'))
        # path_csv = r'{}'.format(os.path.join(path_proiect, 'autocor_train.csv'))

        # path_folder_note = r'{}'.format(os.path.join(path_proiect, 'note_test'))
        # path_csv = r'{}'.format(os.path.join(path_proiect, 'autocor_test.csv'))

        print("\nAti ales sa faceti procesarea pe *{}* "
              "\nsi sa returnati *{}*.".format(path_folder_note, path_csv))

        print("\nSe proceseaza...")

        autocorelatie.returnare_csv(path_folder_note, path_csv)     # se returneaza CSV cu frecv si nota din *toate* fisiere.wav
        print("\nProcesare finalizata, CSV creat.")

    elif ans_proc == 2:
        print("\nPentru procesare, ati ales: spectograma.\n")
        spectograma.procesare()
        print("\nProcesare finalizata.")


    ans_ml = int(input("\nTip machine learning algorithm dorit: k-nn(1), k-means(2) sau skip ML(0). "))
    if ans_ml == 1:
        print("\nPentru clasificare, ati ales: k-nn.\n")
        csv_ales = 'autocor_train&test.csv'
        # csv_ales = 'autocor_train.csv'
        # csv_ales = 'autocor_test.csv'

        print("\nAti ales sa faceti ML pe *{}*.\n".format(csv_ales))
        print("\nSe face ML...")

        knn.clasificare(csv_ales)

    elif ans_ml == 2:
        print("\nPentru clasificare, ati ales: k-means.\n")
        kmeans.clasificare()


if __name__ == '__main__':
    notes_translate()

#bibliografie:
#https://www.analyticsvidhya.com/blog/2021/01/a-quick-introduction-to-k-nearest-neighbor-knn-classification-using-python/
