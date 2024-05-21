Palabra = "Juan"

for i in range(0,10,1):
	print(Palabra)

print("")

Edad = 29

for i in range(1,Edad+1,1):
	print(i)

print("")

Numero = int(456)
Guarda = ""

if Numero>0:
	for i in range(1,Numero+1,1):
		if i % 2 != 0:
			Guarda += str(i)+","

	print(Guarda)

print("")

Numero = int(20)
Guarda = ""

if Numero>0:
	for i in range(Numero,0,-1):
		print(i)
		Guarda += str(i)+","

	print(Guarda)

print("")

Cantidad = 1000
Interes = 10
Años = 5

for i in range(0,Años,1):
	print(f"Inversión con ganancias: {Cantidad*(1+(Interes/100))}") 
	Cantidad = Cantidad*(1+(Interes/100))

print("")

Numero = int(4)

for i in range(1,Numero+1,1):
	print("*"*i)

print("")

Numero = 5

for i in range(0,11,1):
	print(Numero,"*",i,"=",Numero*i)

print("")

numero = 11
Guarda = " "

for i in range(1,numero+1,1):
	if i % 2 != 0:
		Guarda = str(i)+ " " + Guarda 
		print(Guarda)

	# elif i % 2 == 0:
	# 	print(Guarda)
	# 	Guarda = str(i) + Guarda 

	else:
		pass

print("")

Contraseña = "Hola" 
Nueva_Contraseñas = "m"

# while Contraseña != Nueva_Contraseñas:

# 	Nueva_Contraseñas = str(input("Ingresa la nueva Contraseña: "))

print("")

Numero = 17
i = 2

while Numero % i != 0:
	i += 1

if i == Numero:
	print("primo")

else:
	print("no es primo")


print("")

Palabra = "Juan"

for i in range(len(Palabra),0,-1):
	print(Palabra[i-1])

print("")

Palabra = "Pronto se dan cuenta que estan encerrados"
Palabra = Palabra.lower()
Letra = "e"
Conteo = 0

for i in range(0,len(Palabra),1):
	if Palabra[i] == Letra:
		Conteo += 1

print(Conteo)

print("")

while True:
	Frase = input("Ingresa una palabra: ")
	if Frase == "salir":
		break
		
	print(Frase)

