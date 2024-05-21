def Solucion(height: list) -> int:
	Datos = height
	Izquierda = [] # Vector que se lee de Izquierda a Derecha
	Derecha = [] # Vector que se lee de Derecha a Izquierda
	Resultado = 0  
	Izquierda_Maximo = 0  
	Derecha_Maximo = 0 

	for i in range(len(Datos)):
		if i == 0: # Se obtiene a frontera izquierda
			Izquierda.append(0)
			Izquierda_Maximo = max(Izquierda_Maximo, Datos[i])

		else: # Se obtiene el máximo de cada nodo, haciendo una comparación entre el nodo y el máximo anterior
			Izquierda.append(Izquierda_Maximo)
			Izquierda_Maximo = max(Izquierda_Maximo, Datos[i]) 

	Sotad = Datos[::-1] # Se debe de voltear los datos para poder leer los de derecha a izquierda 

	for i in range(0,len(Sotad),1):
		if i == len(Sotad)-1: # Se obtiene la frontera derecha
			Derecha.append(0)
			Derecha_Maximo = max(Derecha_Maximo, Sotad[i])

		else: # Se obtiene el máximo de cada nodo, haciendo una comparación entre el nodo y el máximo anterior 
			Derecha.append(Derecha_Maximo)
			Derecha_Maximo = max(Derecha_Maximo, Sotad[i]) 

	Derecha = Derecha[::-1] # Se deben de regresar los datos al sentido original para poder hacer la resta

	for i in range(len(Izquierda)):
		Valor = min(Izquierda[i], Derecha[i]) - Datos[i] # Se obtienen los minimos de cada lista y se restan los datos 

		if Valor > 0: # Con ello se logra e valor faltante, sólo queda sumar el valor positivo
			Resultado += Valor

		else:
			pass

	return Resultado

Lista = [[0,1,0,2,1,0,1,3,2,1,2,1],[0,1,5,2,0,1,3,2,1,4],[4,2,0,3,2,5]]

for i in range(0,len(Lista),1):
	Activo = Solucion(Lista[i])
	print(Activo)
