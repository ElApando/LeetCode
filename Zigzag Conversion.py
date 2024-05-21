def convert( s: str, numRows: int) -> str:
	Cadena = s
	Renglones = numRows
	Lista = []
	Paralelo = []
	j = 0
	Conteo = 1

	if len(Cadena) < Renglones or Renglones == 1:
		return Cadena

	for i in range(0,Renglones,1): # Contenedores 
		Lista.append([])

	for i in range(0,len(Cadena),1): # Contenido
		# for j in range(1,Renglones+1,1):
		print(Cadena[i],i,j,Conteo,Lista)
		Lista[j].append(Cadena[i])

		if j == 0:
			Conteo = 1

		elif j == Renglones-1:
			Conteo = -1

		else:
			pass

		j += Conteo
			

	for i in range(0,Renglones,1):
		Lista[i] = "".join(Lista[i])

	return "".join(Lista)

Lista = ["PAYPALISHIRING","AB"]; Cantidad = [3,1]

for i in range(0,len(Lista),1):
	Activo = convert(Lista[i],Cantidad[i])
	print(Activo)

"""
P,A,Y,P,A,L,I,S,H,I,R ,I ,N ,G
0,1,2,3,4,5,6,7,8,9,10,11,12,13
1,2,3,2,1,2,3,2,1,2,3 ,2 ,1 ,2

P   A   H   N
A P L S I I G
Y   I   R"""


"""
P,A,Y,P,A,L,I,S,H,I,R ,I ,N ,G
0,1,2,3,4,5,6,7,8,9,10,11,12,13
1,2,3,4,3,2,1,2,3,4,3 ,2 ,1 ,2

P     I    N
A   L S  I G
Y A   H R
P     I
"""

