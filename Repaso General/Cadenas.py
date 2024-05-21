Nombre = "Juan"
Numero = 5

for i in range(Numero):
	print(Nombre)

print("")

Nombre = "Juan Rodrigo Villalpando González"

print(Nombre.lower())
print(Nombre.upper())
print(Nombre.capitalize())
print(Nombre.title())

print("")

Nombre = "Juan"
print(f"{Nombre} tiene {str(len(Nombre))} letras")

print("")

Numero = "+34-913724710-56"
Separcion = Numero.split("-")
Codigo = Separcion[0]
Numero = Separcion[1]
Extension = Separcion[2]
print(Numero)

print("")

Frase = "Juan en colapso"
print(Frase[::-1])

print("")

Frase = "Juan en colapso"
Vocal = "a"
Frase = Frase.replace(Vocal,Vocal.upper())
print(Frase)

print("")

Correo = "jrbartoleo@gmail.com"
Lugar = 0
for i in range(0,len(Correo),1):
	if Correo[i] == "@":
		Lugar = i

print(Correo[:Lugar+1]+"ceu.es")
print(Correo[:Correo.find("@")]+"@ceu.es")

print("")

Euros = str(12.23)
Numero = Euros[:Euros.find(".")]
Centimo = Euros[Euros.find(".")+1:]
print(Numero,Centimo)

print("")

Fecha = "21/04/1995"
Separacion = Fecha.split("/")
Dia = Separacion[0]
Mes = Separacion[1]
Año = Separacion[2]

print(Dia)
print(Mes)
print(Año)

print("")

Cosas = "Televisión,Hogar,Lugar,Foco,Juego"
Separacion = Cosas.split(",")

for elemento in Separacion:
	print(elemento)
 
print("")

Producto = "Tomates"
Cantidad = 200
Costo = 630.25 

print(f"Producto: {Producto}, Cantidad: {Cantidad}, Precio: {round(Costo,2)}, Costo: {round(Cantidad*Costo,2)}")