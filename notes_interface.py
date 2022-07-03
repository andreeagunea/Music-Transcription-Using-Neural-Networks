from music21 import *

note_corecte1= ['C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3','C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3',
     'C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3','C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3',
     'C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3']

note_prezise1 = ['D3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3','C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3',
     'C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3','C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3',
     'C3', 'D3', 'E3', 'F3', 'A3', 'A3', 'E3', 'D3', 'D3']

note_corecte = ['C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3']
note_prezise = ['C3', 'D3', 'E3', 'F3', 'F3#', 'F3', 'E3', 'D3', 'C3']

note_wiste_corecte = ['B3','B3','B3','C4','C4','A3','G3','C4','C4','A3','G3','C4','D4','D4','B3','B3','B3','C4','C4','A3',
                      'G3','C4','C4','A3','G3','C4','D4','D4','C4','C4','A4','A4','G4','G4','E4','E4','D4','C4','E4','G4',
                      'E4','B3','B3','B3','C4','C4','A3','G3','C4','C4','A3','G3','D4','B3','C4']

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