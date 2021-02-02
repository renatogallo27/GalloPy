#Gli autori sono Gallo e Corbo
import numpy as np
import matplotlib.pyplot as plt
from guizero import *


def mostra_grafico():
    f=a.value
    f = open(f, 'r')
    coordX = []
    coordY = []

    for riga in f:
        valori = str(f.readline())  
        Nval = len(valori)          
        valori = valori.strip('\n') 
        valori = valori.split(',')  
        valori = list(valori)       
        print(valori)
        coordX.append(int(valori[0])) 
        coordY.append(int(valori[1])) 

    f.close()  

    print ("X: ",coordX)
    print ("Y: ",coordY)


    coordX.sort()
    coordY.sort()


    print(type(coordX))
    print(type(coordY))

    plt.scatter(coordX,coordY)
    plt.title("Grafico a dispersione")
    plt.savefig("grafico.png", dpi=105, facecolor = "#f1f1f1")
    grafico= Picture(app, image="grafico.png")

app = App(title="Prodotto intermedio")
intro = Text(app, text="Benvenuto su Prodotto intermedio!")


a=TextBox(app, text="File da leggere")
bottone = PushButton(app, text = "Mostra grafico", command=mostra_grafico)
app.display()
