Divisa = "Peso"
Diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

try:
	print(Diccionario[Divisa])

except KeyError:
	print("La divisa no se encuentra en e diccionario")

print("")

Nombre = "Juan"
Edad = "29"
Direccion = "CTM Aragón" 
Telefono = "5520031475"

Diccionario = {"Nombre":Nombre,"Edad":Edad,"Direccion":Direccion,"Telefono":Telefono}
print(f"{Nombre} tiene {Edad} años, vive en {Direccion} y su número de télefono es {Telefono}")

print("")

Diccionario = {"Platano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
Fruta = "Pera"
Kilo = 3.5

try:
	print(f"Fruta {Fruta}, kilo(s) {Kilo}, precio total {Diccionario[Fruta]*Kilo}")

except KeyError:
	print("La fruta no se encuentra en e diccionario")

print("")

Fecha = "03/05/2024"
Diccionario = {"01":"Enero",
			   "02":"Febrero",
			   "03":"Marzo",
			   "04":"Abril",
			   "05":"Mayo",
			   "06":"Junio",
			   "07":"Julio",
			   "08":"Agosto",
			   "09":"Septiembre",
			   "10":"Octubre",
			   "11":"Noviembre",
			   "12":"Diciembre"}

Fecha = Fecha.split("/")
Dia = Fecha[0]
Mes = Fecha[1]
Año = Fecha[2]

print(f"{Dia} de {Diccionario[Mes]} de {Año}")

print("")

Diccionario = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
Total = 0

for Asignaturas, Creditos in Diccionario.items():
	print(f"{Asignaturas} tiene {Creditos} Creditos")
	Total += Creditos

print(f"Creditos Totales {Total}")

print("")

Lista = ["Juan",28,"Masculino",5520031475,"jrbartoleo@gmail.com"]
Diccionario = {"Nombre":0,"Edad":0,"Sexo":0,"Telefono":0,"Correo":0}
Conteo = 0

for Llave, Objeto in Diccionario.items():
	Diccionario[Llave] = Lista[Conteo]
	Conteo = Conteo + 1
	print(Diccionario)

print("")

Lista_Articulo = ["Ar1","Ar2","Ar3","Ar4","Ar5","Ar6","Ar7","Ar8"]
Lista_Precio = ["Pr1","Pr2","Pr3","Pr4","Pr5","Pr6","Pr7","Pr8"]
Lista_Listo = [0,0,0,0,0,1,0,0,0]
Alto = 0
Conteo = 0 
Diccionario = {}

while Alto == 0:
	Diccionario[Lista_Articulo[Conteo]] = Lista_Precio[Conteo]
	Conteo = Conteo + 1
	Alto = Lista_Listo[Conteo]

print(Diccionario,Conteo)

print("")

Diccionario = {"hola":"hi","juan":"jhon","como":"how","estas":"are","tu":"you"}
Traduccion = "Hola Juan como estas tu"
Traduccion = Traduccion.lower()
Traduccion = Traduccion.split(" ")
Nuevo = ""

for i in range(0,len(Traduccion),1):
	Nuevo = Nuevo + Diccionario[Traduccion[i]]
	Nuevo = Nuevo + " "

print(Nuevo.capitalize())

print("")

Diccionario = {"QE-451":4568,"QE-453":24}
Factura =  "QE-453"
Costo = 1754
Total = 0
Accion = 1

Lista_Valores = list(Diccionario.values())

if Accion == 1:
	Diccionario[Factura] = Costo

elif Accion == 2:
	Diccionario.pop(Factura,0)

else:
	print("Esa factura no existe")

print("Total de facturas",sum(Lista_Valores))
print(Diccionario)

print("")

Clientes = {"01":"Juan/CMT Aragon/5520031475/jrbartoleo@gmail.com/True"
			"02":"Aldo/CMT Aragon/5520031475/jrbartoleo@gmail.com/False",
			"03":"Abraham/CMT Aragon/5520031475/jrbartoleo@gmail.com/True",
			"04":"Andrés/CMT Aragon/5520031475/jrbartoleo@gmail.com/False"}
Cliente = "01" 






print("")
