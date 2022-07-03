import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np

y, sr = librosa.load("procesare\piano.wav")

o_env = librosa.onset.onset_strength(y=y, sr=sr)
times = librosa.times_like(o_env, sr=sr)
onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)

print(onset_frames) # frame numbers of estimated onsets

onset_times = librosa.frames_to_time(onset_frames)
print(onset_times)

y_db = 10.0 * np.log10(y)

plt.figure(figsize=(10,5))
librosa.display.waveplot(y, sr=sr)
plt.vlines(onset_times, -1, 1, color = 'r')
if y_db.any()<16:
    plt.vlines(y, -0.5, 0.5, color='y', alpha = 0.003)
            

