import librosa
import os
import math
import numpy as np
import csv
from scipy.signal import find_peaks


def returnare_cale(path_folder_note):
    fisiere = os.listdir(path_folder_note)               #lista cu toate fisierele
    path_fisiere = ['nimic'] * len(fisiere)              #prealocare lista cu path-uri fisiere
    for i in range(len(fisiere)):
        path_fisiere[i] = os.path.join(path_folder_note, fisiere[i])  # creare lista path-uri fisiere

    return path_fisiere


def nota_index_in_nota_octava(nota_index):
    note = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    nota = (nota_index - 1) % len(note)
    nota = note[nota]
    octava = (nota_index + 8) // len(note)

    return nota, octava


def frecv_in_nota_index(pitch):
    if not pitch:  # daca avem o valoare diferita de 0
        pitch += 1e-15
    # formula luata de pe https://en.wikipedia.org/wiki/Piano_key_frequencies
    nota_index = 12 * math.log2(pitch / 440) + 49
    offset_from_note = nota_index
    nota_index = round(nota_index)
    offset_from_note -= nota_index
    nota = nota_index_in_nota_octava(nota_index)

    return nota


def autocorelatie(path_fisier):
    y, sr = librosa.load(path_fisier)

    # plt.figure(figsize=(14, 5))
    # librosa.display.waveplot(y, sr=sr)

    corr = np.correlate(y, y, 'full')[len(y) - 1:]

    peaks, dics = find_peaks(corr, height=0)
    top = np.argsort(corr[peaks])[-2:]
    ind = top[-1]
    pitch = sr / peaks[ind]
    # print(pitch, "hz")
    #
    # plt.figure(figsize=(14,5))
    # plt.plot(corr[:10000])
    # plt.plot(peaks[top], corr[peaks[top]], "x")
    # plt.xlabel('Lag (samples)')
    # plt.xlim(0, 10000)
    # plt.show()

    nota = frecv_in_nota_index(pitch)
    nota = ''.join(map(str, nota))
    # print(nota, pitch)

    return nota, pitch


def returnare_csv(path_folder_note, path_csv):
    path_fisiere = returnare_cale(path_folder_note)         #lista cu path-urile tututor fisierelor.wav din folder
    lista = []
    with open(path_csv, 'a', newline='') as f:  # write results to file
        writer = csv.writer(f)
        writer.writerow(['fisier', 'pitch', 'nota'])
        for path_fisier in path_fisiere:  # execute for each file
            nota, pitch = autocorelatie(path_fisier)  # result is returned to nota, pitch
            fisier = os.path.basename(path_fisier)  # get the basename for writing to output file
            lista.append([fisier, pitch, nota])
        writer.writerows(lista)
        # csv creat


# END
#######################################################################################################################
