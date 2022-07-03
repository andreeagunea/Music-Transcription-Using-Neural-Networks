import librosa
import soundfile as sf
import os


def filtrare_liniste(folder, folder_out, prag):

    for i in range(len(path_fisiere)):
        path_fisier = r'{}'.format(path_fisiere[i])
        y, sr = librosa.load(path_fisier, sr=8000, mono=True)

        clip = librosa.effects.trim(y, top_db=prag)       #elimina semnalul cu o putere sub 10db, fiind considerat liniste

        path_fisier_out = r'{}'.format(path_fisiere_out[i])
        sf.write(path_fisier_out, clip[0], sr)          #se salveaza noul semnal audio

