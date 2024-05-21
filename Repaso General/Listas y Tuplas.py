Lista = ["Matemáticas","Física","Química","Historia","Lengua"]
print(Lista)

print("")

for Elemento in Lista:
	print(f"Yo estudio {Elemento}")

print("")

Guardar = []

# for Elemento in Lista:
# 	Calificacion = input(f"Ingresa la calificación de {Elemento}: ")
# 	print(f"En {Elemento} has obtenido {Calificacion}")

print("")

Lista = []

# for i in range(6):
# 	Numero = input("Ingresa el número ganador: ")
# 	Lista.append(Numero)

# Lista.sort()
# print(Lista)

print("")

Lista = []

for i in range(1,10+1,1):
	Lista.append(str(i))

Lista = Lista[::-1]
Lista = ",".join(Lista)

print(Lista)

print("")

Lista = ["Matemáticas","Física","Química","Historia","Lengua"]
Conteo = 0

# while True:
# 	Calificacion = int(input(f"Ingresa la calificación: "))
# 	Conteo = Conteo + 1
# 	if Calificacion > 6:
# 		Lista.pop()

# 	else:
# 		pass

# 	if Conteo == 5:
# 		break

print(Lista)

print("")

Letras = ['a', 'b', 'c', 'd', 'e', 
			'f', 'g', 'h', 'i', 'j', 
			'k', 'l', 'm', 'n', 'ñ',
			'o', 'p', 'q', 'r', 's', 
			't', 'u', 'v', 'w', 'x',
			'y', 'z']

Total = len(Letras)
Letras_Filtradas = []
Conteo = 1

for Elemento in Letras:

	if Conteo % 3 != 0:
		Letras_Filtradas.append(Elemento)
	Conteo = Conteo + 1 

print(Letras_Filtradas)

print("")

Palabra = "Ana"
Palabra = Palabra.lower()
Guarda = ""

for i in range(len(Palabra),0,-1):
	Guarda += Palabra[i-1]


if Palabra == Guarda:
	print("Es palindromo")

print("")

Palabra = "OJOJOJOJrewrewtreyfjisdfjdsjfjeiondvionenfvdjsfopwejidsc"
Diccionario = {}
Palabra = Palabra.lower()
Conteo = 0

for i in range(0,len(Palabra),1):
	if Palabra[i] not in Diccionario.keys():
		Diccionario[Palabra[i]] = 1

	elif Palabra[i] in Diccionario.keys():
		Diccionario[Palabra[i]] = Diccionario[Palabra[i]]+1

	else:
		pass
		
print(Diccionario)

print("")

Precios = [50, 75, 46, 22, 80, 65, 8]
Maximo = 0
Minimo = 100

for i in range(0,len(Precios),1):
	Maximo = max(Precios[i],Maximo) 
	Minimo = min(Precios[i],Minimo)

print(Maximo)
print(max(Precios),min(Precios))
print(Minimo)

print("")

Vector_A = (1,2,3)
Vector_B = (-1,0,2)

if len(Vector_A) >= len(Vector_B):
	Maximo = len(Vector_A)

else:
	Maximo = len(Vector_B)

Resultado = 0
for i in range(0,Maximo,1):
	Operacion = Vector_A[i]*Vector_B[i]
	print(Operacion,Vector_A[i],Vector_B[i])
	Resultado = Resultado+Operacion

print(Resultado)

print("")

A = [[1,2,3],[4,5,6]]
B = [[-1,0,1],[0,1,1]]

Guarda = [[] for i in range(len(A))]

Resultado = 0

for i in range(0,len(A),1):
	for j in range(0,len(A),1):
		for k in range(0,len(A[i]),1):
			# print(i,j,k,A[i],B[i],A[i][k],B[j][k])
			Resultado = Resultado + A[i][k]*B[j][k]

		Guarda[i].append(Resultado)
		Resultado = 0

print(Guarda)

print("")

Lista = [1,2,3,4,5]
Suma = 0

for i in range(0,len(Lista),1):
	Suma += Lista[i]

Media = Suma/len(Lista)

Suma_2 = 0
for i in range(0,len(Lista),1):
	X = abs(Lista[i]-Media)**2
	Suma_2 += X

Desviacion_Estadar = round((Suma_2/len(Lista))**(1/2),2)

print(Suma,Media,Suma_2,Desviacion_Estadar)