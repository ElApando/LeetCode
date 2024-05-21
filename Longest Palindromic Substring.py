def longestPalindrome(s: str) -> str:
	Cadena = s
	Lista = []
	Revision = ""
	Bandera = 0

	if len(Cadena) == 1:
	    return Cadena

	for i in range(0,len(Cadena),1):
		for j in range(0,len(Cadena[Bandera:]),1):
			Revision = Revision + Cadena[j+Bandera]

			if Revision == Revision[::-1]:
				Lista.append(Revision)

				if len(Revision) == len(Cadena[Bandera:]):
					Maximo = 0
					Cadena_Larga = ""

					for Elemento in Lista:
						Tamaño = len(Elemento)
						
						if Tamaño > Maximo:
							Cadena_Larga = Elemento
							Maximo = Tamaño

					Lista = Cadena_Larga

					if Lista == "":
						Lista = Cadena[0]

					return Lista
 
			elif len(Revision) == len(Cadena[Bandera:]):
				Bandera = Bandera+1
				Revision = ""

			else:
				pass

	# try:			
	# 	Maximo = 0
	# 	Cadena_Larga = ""

	# 	for Elemento in Lista:
	# 		Tamaño = len(Elemento)
			
	# 		if Tamaño > Maximo:
	# 			Cadena_Larga = Elemento
	# 			Maximo = Tamaño

	# 	Lista = Cadena_Larga

	# 	if Lista == "":
	# 		Lista = Cadena[0]

	# except ValueError:
	# 	Lista = Cadena[0]

	return Lista

Lista = ["babad","cbbd","bb","qweewq","a","ac","abb","abadd","babadada"]#["cbcdcbedcbc"]#

# def longestPalindrome( s: str) -> str:
# 	if len(s) <= 1:
# 		return s

# 	Max_Len=1
# 	Max_Str=s[0]
# 	for i in range(len(s)-1):
# 		for j in range(i+1,len(s)):
# 			print(s[i:j+1],s[i:j+1][::-1])
# 			if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
# 				Max_Len = j-i+1
# 				Max_Str = s[i:j+1]

# 	return Max_Str

for i in range(0,len(Lista),1):
	Activo = longestPalindrome(Lista[i])
	print(Activo)


ista = ["aba","dd","a","aaa"]


