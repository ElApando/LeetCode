def Solucion(x: int) -> bool:
	x = str(x)
	y = str(x[::-1])
	
	return x == y if True else False

Prueba = [121,-121,10]
#,
for i in range(0,len(Prueba),1):
	Activo = Solucion(Prueba[i])
	print(Activo)
