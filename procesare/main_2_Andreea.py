import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt
from scipy.signal import hamming
import autocorelatie
import spectograma
import cepstrum
import knn
import kmeans

y, sr = librosa.load("Note pian\C3.wav")
print(sr)  #rata de esnationare
print(len(y))  #y = duratata semnal in secunde * rata de esantionare sr
#durata = len(y)/sr

plt.figure(figsize=(14,5))
librosa.display.waveplot(y, sr=sr)

#Esantionare semnal
fereastra = int(80*1e-3*sr)
print(fereastra)

#Ferestre suprapuse
p=0.2  #Factorul de suprapunere

#Numar cadre suprapuse
numar_cadre_p = int(len(y)/(fereastra*(1-p)))
print("Numarul de cadre este %d" %numar_cadre_p)

#Creare variabila timp pentru axa Ox
time_axis = np.arange(0, fereastra)*1/sr #utilizata la plot-uri

def procesare_semnal():
    for k in range(numar_cadre_p):

        cadru_curent_p = y[int(fereastra*k*(1-p)):int(fereastra*(k*(1-p)+1))] 

        #Plot ferestre
        #plt.figure(figsize=(14,5))
        #plt.plot(time_axis, cadru_curent_p)
        #plt.title("Cadru de analiza: %d" %(k+1))
        #plt.xlabel("Time [sec]")
        #plt.xlim((0, time_axis[-1]))
        #plt.ylim((-1,1))
        
        #Generare fereastra Hamming pentru a elimina efectul de alisiang
        fereastra_hamming = hamming(fereastra)
        #Inmultesc fereastra hamming cu fiecare cadru in parte
        cadru_hamming = np.multiply(fereastra_hamming, cadru_curent_p)

        #Plot fereastra Hamming
        #plt.figure(figsize=(14,5))
        #plt.plot(time_axis, cadru_hamming, 'y')
        #plt.title('Cadru Hamming')
        #plt.xlabel("Time [sec]")
        #plt.xlim((0, time_axis[-1]))
        #plt.ylim((-1,1))
        
        #Aplicare autocorelatie/spectograma/cepstrum
        cadru_procesare = cadru_hamming
        if ans_proc == 1:
            cadru_procasare = autocorelatie(cadru_hamming)
        elif ans_proc == 2:
            cadru_procasare = spectograma(cadru_hamming)
        elif ans_proc == 3:
            cadru_procasare = cepstrum(cadru_hamming)
        else:
            return None
        
        if ans_ml == 1:
            knn.clasificare(cadru_procesare)
        elif ans_ml == 2:
            kmeans.clasificare(cadru_procesare)
        else:
            return None
        
        #asta trebuie introdusa tot in main, pt ca alegerea procesarii se faca doar o data
