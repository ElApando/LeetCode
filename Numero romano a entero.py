def Solucion(s: str) -> bool:
	Numero_Romano = {"I":1,
					 "V":5,
					 "X":10,
					 "L":50,
					 "C":100,
					 "D":500,
					 "M":1000}
	Operacion = 0

	for i in range(0,len(s),1): # Se recorre la cadena de texto 
		""" Se coloca la primera condicional indicando que si esta dentro de los limites y el
		numero en el que nos encontramos es menor al numero siguiente, entonces:"""
		if i < len(s)-1 and Numero_Romano[s[i]] < Numero_Romano[s[i+1]]: 
			Operacion -= Numero_Romano[s[i]] # Se resta
		else:
			Operacion += Numero_Romano[s[i]]

	return Operacion

Prueba = ["III","LVIII","MCMXCIV","IX"]
#,
for i in range(0,len(Prueba),1):
	Activo = Solucion(Prueba[i])
	print(Activo)
