class retta:
    def __init__(self, a, b, c, x):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__x = x
        self.__punti = []

        
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

    def eqEsplicita(self):
        if self.__b==0:
            return f"Equazione impossibile!"
        elif self.__c==0:
            return f"y={-self.__a}x/{self.__b}"
        elif self.__a==0:
            return f"y={-self.__c}/{self.__b}"
        else:
            return f"y={-self.__a/self.__b}x+{-self.__c/self.__b}"
        
    def trovaY(self):
        y = int(((self__.a*self.__x)+ self.__c)/ self.__b)
        return f"y={y}"

    def punti(self, N, M):
        self.__N = N
        self.__M= M

        for self.__N in range(self.__M):
            tupla = (x, (-self.__a * x) / self.__b + (-self.__c / self.__b))
            x = x+1
            self.__punti.append(tupla)
            return f"Coordinate: {self.__punti}"

   
