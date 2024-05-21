def Solucion(strs: [str]) -> str:
	Resultado = ""
	Orden = sorted(strs)
	Primero = Orden[0]
	Ultimo =  Orden[-1]

	for i in range(min(len(Primero),len(Ultimo))):
		print(Primero[i],Ultimo[i],Orden[i],i)
		if Primero[i] != Ultimo[i]:
			return Resultado

		Resultado += Primero[i]

	return Resultado

Prueba = [["flower","flow","floght","flight","fly"],["dog","racecar","car"]]
#,
for i in range(0,len(Prueba),1):
	Activo = Solucion(Prueba[i])
	print(Activo)