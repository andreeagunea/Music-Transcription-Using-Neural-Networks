import os

#script care gaseste csv-urile din folderul curent
def cauta_csv():
    fisiere = os.listdir(os.getcwd())
    indecsi_csv = []
    for i in range(len(fisiere)):
        extensie = os.path.splitext(fisiere[i])[1]
        if extensie == '.csv':
            indecsi_csv.append(i)

    fisiere_csv = [fisiere[i] for i in indecsi_csv]
    return fisiere_csv
