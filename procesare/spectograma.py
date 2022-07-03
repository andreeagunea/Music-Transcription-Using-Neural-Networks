import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt
import os


def spectograma(path_fisier, path_fisier_out):
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

    plt.close(fig)

def procesare(path_folder_note, path_rezultat):
    fisiere = os.listdir(path_folder_note)
    path_fisiere = [os.path.join(path_folder_note, i) for i in fisiere]

    fisiere_out = [os.path.splitext(i)[0] + '.jpg' for i in fisiere]
    path_fisiere_out = [os.path.join(path_rezultat, i) for i in fisiere_out]

    for i, j in zip(path_fisiere, path_fisiere_out):
        spectograma(i, j)

    return 0

path = os.getcwd()
folder_out = 'spectograme_semnal'                                   # folderul de output
path_folder_out = os.path.join(path, folder_out)                    # se afla in proiect
fisier_out = str(1) + '.jpg'                                        # splitext ia numele fisierului fara extensie
path_fisier_out = os.path.join(path_folder_out, fisier_out)         # calea fisierului de out