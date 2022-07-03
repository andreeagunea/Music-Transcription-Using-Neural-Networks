import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import math
import csv
import os
import scipy as sp
from scipy import signal


def creare_cepstrum(semnal, frecv_esant):
    cadru_size = semnal.size  #dimensiunea ferestrei este agala cu numarul de elemente ale semnalului
    fereastra_semnal = np.hamming(cadru_size) * semnal  #semnalul se inmulteste cu o fereastra hamming de aceeasi marime
    dt = 1/frecv_esant  
    freq_vector = np.fft.rfftfreq(cadru_size, d=dt)
    X = np.fft.rfft(fereastra_semnal)
    log_X = np.log(np.abs(X))
    cepstrum = np.fft.rfft(log_X)
    df = freq_vector[1] - freq_vector[0]
    quefrency_vector = np.fft.rfftfreq(log_X.size, df)
    
    return quefrency_vector, cepstrum

def cepstrum_f0_detectie(semnal, frecv_esant):
    #se creaza cepstrumul
    quefrency_vector, cepstrum = creare_cepstrum(semnal, frecv_esant)
    
    # se extrage pitch-ul din cepstrum dintr-o regiune valida
    valid = (quefrency_vector > 1/1200) & (quefrency_vector <= 1/100) #avem doar frecvente intre 200 si 1100 Hz
    max_quefrency_index = np.argmax(np.abs(cepstrum)[valid]) #se extrage valoarea maxima din cepstrum
    f0 = 1/quefrency_vector[valid][max_quefrency_index]  #pitch-ul este egal 1 supra valoarea maxima din vectorul de valori valide
    return f0


def get_file_paths(dirname):
    file_paths = []  
    for root, directories, files in os.walk(dirname):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  
    return file_paths

def note_index_to_note_octave(note_index):
        notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

        note = (note_index - 1) % len(notes)
        note = notes[note]

        octave = (note_index + 8) // len(notes)

        return note, octave
        
def freq_to_note_index(freq):
        if not freq:  # no log value for 0
            freq += 1e-15
        # formula taken from https://en.wikipedia.org/wiki/Piano_key_frequencies
        note_index = 12 * math.log2(freq / 440) + 49
        offset_from_note = note_index
        note_index = round(note_index)
        offset_from_note -= note_index
        nota = note_index_to_note_octave(note_index)
        return nota

def process_file(file):
    y, sr = librosa.load(file)
    med = sp.signal.medfilt(y, 21) #am aplicat filtru de mediere
    # plt.figure(figsize=(14, 5))
    # librosa.display.waveplot(y, sr=sr)

    pitch = cepstrum_f0_detectie(med, sr)
    print(pitch)
    # print(pitch, "hz")
    #
    # plt.figure(figsize=(14,5))
    # plt.plot(corr[:10000])
    # plt.plot(peaks[top], corr[peaks[top]], "x")
    # plt.xlabel('Lag (samples)')
    # plt.xlim(0, 10000)
    # plt.show()
        
    nota = freq_to_note_index(pitch)
    nota = ''.join(map(str, nota))

    # print(nota, pitch)
    
    return nota, pitch

# def main():
#     files = get_file_paths(DIRNAME)                 # get all file-paths of all files in dirname and subdirectories
#     for file in files:                              # execute for each file
#         (filepath, ext) = os.path.splitext(file)    # get the file extension
#         file_name = os.path.basename(file)          # get the basename for writing to output file
#         if ext == '.wav':                           # only interested if extension is '.wav'
#             nota, pitch = process_file(file)                  # result is returned to nota, pitch
#             with open(OUTPUTFILE, 'a') as f:        # write results to file
#                 writer = csv.writer(f)
#                 writer.writerow(['file_name','note_name', 'note_freq'])
#                 writer.writerow([file_name, nota, pitch])

def main():
    files = get_file_paths(path_folder_note)  # get all file-paths of all files in dirname and subdirectories
    with open(path_rezultat, 'a', newline='') as f:  # write results to file
        writer = csv.writer(f)
        writer.writerow(['fisier', 'pitch', 'nota'])
        for file in files:  # execute for each file
            fisier = os.path.basename(file)  # get the basename for writing to output file
            nota, pitch = process_file(file)  # result is returned to nota, pitch
            writer.writerow([fisier, pitch, nota])

if __name__ == '__main__':
    folder_note = 'note_trainsitest_filtrate_prag11db'
    path_folder_note = r'{}'.format(os.path.join(os.getcwd(), folder_note))
    rezultat = 'autocor_note_trainsitest_filtrate_prag11db.csv'
    path_rezultat = r'{}'.format(os.path.join(os.getcwd(), rezultat))
    main()