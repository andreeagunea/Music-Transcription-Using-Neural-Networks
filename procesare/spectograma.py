import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt
from pathlib import Path
import os


def create_spectrogram_train(path_fisier, path_fisier_out):
    y, sr = librosa.load(path_fisier)

    plt.interactive(False)
    fig = plt.figure(figsize=[0.72, 0.72])
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)

    S = librosa.feature.melspectrogram(y=y, sr=sr)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))

    fig.savefig(path_fisier_out, dpi=400, bbox_inches='tight', pad_inches=0)

    # plt.show()         #pentru a vizualiza o spectograma, nu se decomenteaza la o rulare pt. toate fisierele

    plt.close(fig)

def procesare():
    path = os.getcwd()                                      # calea proiectului

    folder = 'audio'                                        # folderul 'audio' cu fisiere .wavs
    path_folder = os.path.join(path, folder)                # asta in cazul in care folderul 'audio' este in proiect
    fisier = 'A4#_10.wav'                                   # fisierul dorit
    path_fisier= os.path.join(path_folder, fisier)          # calea lui

    folder_out = 'spectograme'                                          # folderul de output
    path_folder_out = os.path.join(path, folder_out)                    # se afla in proiect
    fisier_out = os.path.splitext(fisier)[0] + '.jpg'                   # splitext ia numele fisierului fara extensie
    path_fisier_out = os.path.join(path_folder_out, fisier_out)         # calea fisierului de out

    ans = int(input("Spectograma doar pentru {} (apasa 1) sau pentru toate fisierele (apasa 0)? ".format(fisier)))
    if ans:
        create_spectrogram_train(path_fisier, path_fisier_out)

    else:
        fisiere = os.listdir(path_folder)                       #lista cu toate fisierele
        path_fisiere = ['nimic'] * len(fisiere)                 #prealocare lista cu path-uri fisiere
        fisiere_out = ['nimic'] * len(fisiere)                  #prealocare lista fisiere_out, nu merge fara
        path_fisiere_out = ['nimic'] * len(fisiere)             #prealocare lista path-uri fisiere_out

        for i in range(len(fisiere)):
            path_fisiere[i] = os.path.join(path_folder, fisiere[i])                 #creare lista path-uri fisiere

            fisiere_out[i] = os.path.splitext(fisiere[i])[0] + '.jpg'               #creare lista fisiere_out

            path_fisiere_out[i] = os.path.join(path_folder_out, fisiere_out[i])     #creare lista path-uri fisiere_out

        for i in range(len(fisiere)):                           #se genereaza 'x' spectograme.jpg pt 'x' fisiere.wav
            create_spectrogram_train(path_fisiere[i], path_fisiere_out[i])

if __name__ == '__main__':
    procesare()
