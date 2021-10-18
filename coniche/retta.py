class Retta:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__punti = []

   #Stiamo avendo difficoltà nella realizzazione di questo metodo
    def __init__(self, p1, p2):
        '''
        questo costruttore deve generare una retta a partire da due punti.
        p1 e p2 sono tuple che identificano le coordinate dei punti a partire
        dai quali vanno ricavati a,b e c ed inizializzati gli attributi di istanza
        '''
        
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c

    def eqImplicita(self):
        if self.__b==0:
            return f"{self.__a}x+{self.__c}=0"
        elif self.__c==0:
            return f"{self.__a}x+{self.__b}y=0"
        elif self.__a==0:
            return f"{self.__b}y+{self.__c}=0"

    def eqEsplicita(self, x):
        if self.__b==0:
            return f"x={-self.__c}/{self.__a}"
        elif self.__c==0:
            return f"y={-self.__a}x/{self.__b}"
        elif self.__a==0:
            return f"y={-self.__c}/{self.__b}"
        else:
            return f"y={-self.__a/self.__b}x+{-self.__c/self.__b}"
        
    def trovaY(self, x):
        return f"y={-self.__a*x/self.__b + (-self.__c/self.__b)}"

    def punti(self, N, M, x):
        self.__N = N
        self.__M = M

        for self.__N in range(self.__M, x):
            tupla = (x, (-self.__a * x) / self.__b + (-self.__c / self.__b))
            x = x+1
            self.__punti.append(tupla)
            return f"Coordinate dei punti: {self.__punti}"

    def m(self):
        if self.__b==0:
            return f"La retta è parallela all'asse delle ordinate"
        else:
            return f"m={-self.__a/self.__b}"

    def intersezione(self, a1, b1, c1, m1):
        self.__a1 = a1
        self.__b1 = b1
        self.__c1 = c1

        if m1 == self.m:
            return f"Le due rette non hanno un punto di intersezione perché sono parallele"

        elif m1 == self.m and (-self.__c/self.__b) == (-self.__c1/self.__b1):
            return f"Le due rette sono coincidenti e quindi hanno tutti i punti in comune"

        else:
            return f"Le due rette sono incidenti nel punto di coordinate: {((-self.__c / self.__b)+(self.__c1 / self.__b1))/((-self.__b / self.__a)+(self.__b1 / self.__a1))}, {((-self.__b / self.__c)+(self.__b1 / self.__c1))/((-self.__b / self.__a)+(self.__b1 / self.__a1))}"

   
