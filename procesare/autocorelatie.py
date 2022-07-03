import librosa
import os
import math
import numpy as np
import csv
from scipy.signal import find_peaks


def nota_index_in_nota_octava(nota_index):
    note = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    nota = (nota_index - 1) % len(note)
    nota = note[nota]
    octava = (nota_index + 8) // len(note)

    return nota, octava


def frecv_in_nota_index(pitch):
    if not pitch:
        pitch += 1e-15

    nota_index = 12 * math.log2(pitch / 440) + 49
    offset_from_note = nota_index
    nota_index = round(nota_index)
    offset_from_note -= nota_index
    nota = nota_index_in_nota_octava(nota_index)

    return nota


def autocorelatie(path_fisier):
    y, sr = librosa.load(path_fisier)

    corr = np.correlate(y, y, 'full')[len(y) - 1:]
    peaks, dics = find_peaks(corr, height=0)
    top = np.argsort(corr[peaks])[-2:]
    ind = top[-1]
    pitch = sr / peaks[ind]

    nota = frecv_in_nota_index(pitch)
    nota = ''.join(map(str, nota))

    return nota, pitch


def procesare(path_folder_note, path_rezultat):
    fisiere = os.listdir(path_folder_note)
    path_fisiere = [os.path.join(path_folder_note, i) for i in fisiere]
    randuri = []
    with open(path_rezultat, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['fisier', 'pitch', 'nota'])
        for path_fisier in path_fisiere:
            nota, pitch = autocorelatie(path_fisier)
            fisier = os.path.basename(path_fisier)
            randuri.append([fisier, pitch, nota])
        writer.writerows(randuri)

    return 0

folder_note = 'note_trainsitest_filtrate_prag11db'
path_folder_note = r'{}'.format(os.path.join(os.getcwd(), folder_note))
rezultat = 'autocor_note_trainsitest_filtrate_prag11db.csv'
path_rezultat = r'{}'.format(os.path.join(os.getcwd(), rezultat))

procesare(path_folder_note, path_rezultat)
