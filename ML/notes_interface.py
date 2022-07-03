from music21 import *

note_corecte = ['C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3','C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3',
     'C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3','C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3',
     'C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3']

note_prezise = ['D3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3','C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3',
     'C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3','C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3',
     'C3', 'D3', 'E3', 'F3', 'A3', 'A3', 'E3', 'D3', 'D3']

s = stream.Stream()
for i, j in zip(note_prezise, note_corecte):
        if i[0] != j[0]:
            n = note.Note(i[0], quarterLength = 1)
            n.style.color='red'
            s.append([n])
        else:
            n = note.Note(i[0], quarterLength = 1)
            s.append([n])
    
s.show()

#s.write('midi', fp='my_melody.midi')  #se salveaza audio-ul notelor