def lengthOfLastWord(s: str) -> int:

    Palabra = s
    Palabra_Separada = Palabra.split(" ")
    Bandera = True

    while Bandera == True:
        if Palabra_Separada[-1] == "":
            Palabra_Separada.pop(-1)
        elif Palabra_Separada[-1] != "":
            Bandera = False

        else:
            print(123) 

    Numero = len(Palabra_Separada[-1])

    return Numero

Palabra = ["Hello World","   fly me   to   the moon  ","luffy is still joyboy"]

for i in range(0,len(Palabra),1):
    Activo = lengthOfLastWord(Palabra[i])
    print(Activo)