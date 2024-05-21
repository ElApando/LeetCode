Edad = 18 

if Edad >= 18:
	print("Es mayor de Edad")

else:
	print("Es menor de Edad")

print("")

Contraseña = "123.132"
Intorudccion = "13.235"

if Contraseña == Intorudccion:
	print("Bienvenido")

else:
	print("Contraseña erronea")

print("")

Numero_1 = 456
Numero_2 = 789

if Numero_2 == 0:
	print("Error")

else:
	Operacion = Numero_1 / Numero_2
	print(Operacion)

print("")

Numero = 5 

if Numero % 1 == 0:
	print("Impar")

elif Numero % 2 == 0:
	print("Par") 

else:
	print("Sabe")

print("")

Edad = 16
Ingreso = 456

if Edad > 16 or Ingreso >= 1000:
	print("Paga impuestos")

else:
	print("No paga impuestos")

print("")

Nombre = "Roberto"
Sexo = "Masculino"

if Nombre[0].lower() < "m" and Sexo == "Femenino":
	print("A") 

elif Nombre[0].lower() > "n" and Sexo == "Masculino":
	print("A") 

else:
	print("B")

print("")

Renta = 10000

if Renta <= 10000:
	Impuesto = 5

elif 10000 <= Renta and  Renta <= 20000:
	Impuesto = 15

elif 20000 <= Renta and  Renta <= 35000:
	Impuesto = 20

elif 350000 <= Renta and  Renta <= 60000:
	Impuesto = 30

elif Renta >= 60000:
	Impuesto = 45

else:
	print("Error")

print("Impuesto",Renta*(Impuesto/100))

print("")

Puntos = 0.7

if  Puntos == 0.0:
	print(f"Veneficio economico: {2400*Puntos}, Inaceptable")

elif Puntos == 0.4:
	print(f"Veneficio economico: {2400*Puntos}, Aceptable")

elif Puntos >= 0.6:
	print(f"Veneficio economico: {2400*Puntos}, Meritorio")

else:
	print("Los puntos no son correctos")

print("")

Edad = 28

if Edad <= 4:
	print("Gratis")

elif 4 < Edad and Edad < 18:
	print("Paga 5")

elif 18 <= Edad:
	print("Paga 10")

else:
	pass

print("")

Tipo = "Vegetariana"

if Tipo == "Vegetariana":
	print("Ingredientes vegetarianos: Pimiento y tofu")
	Extra = "Pimiento"
	
	if  Extra == "Pimiento":
		print("Ingredientes: mozzarella, tomate, pimiento")

	elif  Extra == "Tofu":
		print("Ingredientes: mozzarella, tomate, tofu")

	else:
		("Ese ingrediente no se enecuentra disponible")

elif Tipo == "No Vegetariana":
	print("Ingredientes no vegetarianos: Peperoni, Jamón y Salmón")
	Extra = "Peperoni"
	
	if  Extra == "Peperoni":
		print("Ingredientes: mozzarella, tomate, Peperoni")

	elif  Extra == "Jamón":
		print("Ingredientes: mozzarella, tomate, Jamón")

	elif  Extra == "Salmón":
		print("Ingredientes: mozzarella, tomate, Salmón")

	else:
		("Ese ingrediente no se enecuentra disponible")

