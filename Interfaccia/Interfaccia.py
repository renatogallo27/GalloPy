import numpy as np
import matplotlib.pyplot as plt
from guizero import App, Text, PushButton, TextBox


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
    plt.ylabel("Qualche numero")
    plt.show()

app = App(title="Prodotto intermedio")
intro = Text(app, text="Benvenuto su Prodotto intermedio!")


a=TextBox(app, text="File da leggere")
bottone = PushButton(app, text = "Mostra grafico", command=mostra_grafico)
app.display()













