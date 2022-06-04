import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt
import scipy as sp

#Se incarca semnalul
file = r'D:\Licenta finala\B5_2_s.wav'
y, sr = librosa.load(file)
#Se afiseaza semnalul
# plt.figure(figsize=(14, 5))
# librosa.display.waveplot(y, sr=sr)

#Filtru de mediere - scoate zgomotul
semnal_med = sp.signal.medfilt(y, 21)
#Afisare semnal dupa filtrare
# plt.figure(figsize=(14, 5))
# librosa.display.waveplot(med, sr=sr)


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

def cepstrum_f0_detection(semnal, frecv_esant):
    #se creaza cepstrumul
    quefrency_vector, cepstrum = creare_cepstrum(semnal, frecv_esant)
    
    # se extrage pitch-ul din cepstrum dintr-o regiune valida
    valid = (quefrency_vector > 1/1200) & (quefrency_vector <= 1/100) #avem doar frecvente intre 200 si 1100 Hz
    max_quefrency_index = np.argmax(np.abs(cepstrum)[valid]) #se extrage valoarea maxima din cepstrum
    f0 = 1/quefrency_vector[valid][max_quefrency_index]  #pitch-ul este egal 1 supra valoarea maxima din vectorul de valori valide
    return f0

pitch = cepstrum_f0_detection(semnal_med, sr)  #se apeleaza functia
print(pitch)  #se afiseaza pitch-ul



####Plot Cepstrum####
# dims = semnal_med.shape
# dims[0]

# frame_size = dims[0]
# time_vector = np.arange(frame_size) / sr

# windowed_signal = np.hamming(frame_size) * semnal_med
# dt = 1/sr
# freq_vector = np.fft.rfftfreq(frame_size, d=dt)
# X = np.fft.rfft(windowed_signal)
# log_X = np.log(np.abs(X))

# cepstrum = np.fft.rfft(log_X)
# df = freq_vector[1] - freq_vector[0]
# quefrency_vector = np.fft.rfftfreq(log_X.size, df)

# fig, ax = plt.subplots()
# ax.plot(quefrency_vector, np.abs(cepstrum))
# ax.set_ylim([0,4000])
# ax.set_xlim([0,0.05])
# ax.set_xlabel('quefrency (s)')
# ax.set_title('cepstrum')
