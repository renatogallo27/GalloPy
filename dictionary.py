stringa=(input("Scrivi la frase: "))
alfabeto={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","w","x","y","z"}
for lettera in alfabeto:
    if stringa.count(lettera)>0:
        print(lettera,"=",stringa.count(lettera))
