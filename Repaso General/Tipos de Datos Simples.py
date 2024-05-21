print("¡Hola Mundo!")

print("")

Cadena = "¡Hola Mundo!"
print(Cadena)

print("")	

Cadena = "¡Hola Mundo!"
print(Cadena)

print("")

Nombre = "Juan"#str(input())
print(f"¡Hola {Nombre}!")

print("")

Resultado = ((3+2)/(2*5))**2
print(Resultado)

print("")

Usuario = "Juan"
Horas = 8
Costo_Hora = 500
print(Horas*Costo_Hora)

print("")

Numero = 5
Guarda = 0

for i in range(1,Numero+1,1):
	Guarda = Guarda + i

print(Guarda) 

print("")

Masa = 90
Altura = 177

IMC = Masa/((Altura/100)**2)
print(f"Tu indice de masa corporal es {round(IMC,2)}")

print("")

Divisor = 4
Dividendo = 27
Operacion = Dividendo//Divisor
Resto = Dividendo%Divisor

print(f"{Dividendo} entre {Divisor} da un cociente {Operacion} y un resto de {Resto}")

print("")

Cantidad = 1000
Interes = 10
Años = 5

Anual = round(Cantidad*(Interes/100+1)**Años)
print(Anual)

print("")

Payasos = 1
Muñecas = 1
Payasos_Peso =  112
Muñecas_Peso =  75

print(f"Peso Payasos: {(Payasos_Peso*Payasos)/100}, Peso Muñecas: {(Muñecas_Peso*Muñecas)/100}, el Total es {(Payasos_Peso*Payasos)/100+(Muñecas_Peso*Muñecas)/100} kg")

print("")

Interes = 4
Cantidad = 10
Años = 3

Anual = round(Cantidad*(Interes/100+1)**Años,2)
print(Anual)

print("")

Costo_Barras = 3.49
No_Fresca = 2
Fresca = 3

print(f"Pan Fresco {Fresca}, Pan de Ayer {No_Fresca}, Total = {(Fresca*Costo_Barras)+(No_Fresca*Costo_Barras*0.6)}")

print("")