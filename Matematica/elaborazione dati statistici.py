import matplotlib.pyplot as plt 
import numpy as np
import csv
with open("DatiStatistici-2018.csv", "r") as filecsv:
    lettore=csv.reader(filecsv, delimiter=";")
    grandezza

    for riga in filecsv:
        valori = str(filecsv.readline())
        Nval = len(valori)
        valori = valori.strip('\n')
        valori = valori.split(',')
        valori = list(valori)
        print(valori)
        grandezza.append(valori[0])
        coordY.append(valori[1])
    
    
    

    








