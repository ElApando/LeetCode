# def Solucion(s: [str]) -> bool:

# 	print(s)

# 	Guarda = ""

# 	Orden = s.replace("()","OK,").replace("[]","OK,").replace("{}","OK,")
# 	Orden = Orden.replace("(","OA,").replace(")","KOA,")
# 	Orden = Orden.replace("[","OB,").replace("]","KOB,")
# 	Orden = Orden.replace("{","OC,").replace("}","KOC,")
# 	Orden = Orden.split(",")
# 	Orden.pop(-1)
# 	Lista = []
# 	Mitad = int(round(len(Orden)-(len(Orden)/2),0))

# 	print(Orden,Mitad)

# 	for i in range(0,Mitad,1):
# 		print(Orden[i],Orden[-1-i])
# 		if Orden[i] in Orden[-1-i] and Orden[i] != Orden[-1-i]:
# 			print(1)
# 			Lista.append(True)
# 		elif Orden[-1-i] in Orden[i] and Orden[-1-i] != Orden[i] and "K" in Orden[-1-i]:
# 			print(2)
# 			Lista.append(True)

# 		else:
# 			print(4)
# 			Lista.append(False)

# 	if "OK" in Orden:
# 		print(3)
# 		Lista.append(True)

# 	if False in Lista:
# 		Resultado = False

# 	elif True in Lista:
# 		Resultado = True

# 	else:
# 		pass

# 	return Resultado

# Prueba = ["(}{)","()","()[]{}","(]","{[]}","(){}}{","(()(","({{{{}}}))"]
# #,
# for i in range(0,len(Prueba),1):
# 	Activo = Solucion(Prueba[i])
# 	print(Activo)

def Solucion(s: [str]) -> bool:
	Guarda = []
	Mapa = {")":"(","}":"{","]":"["}

	for Elemento in s:
		if Elemento in Mapa.values():
			Guarda.append(Elemento)

		elif Elemento in Mapa.keys(): 
			if not Guarda or Mapa[Elemento] != Guarda.pop():
				return False

		else:
			continue
	
	return not Guarda

Prueba = ["(}{)","()","()[]{}","(]","{[]}","(){}}{","(()(","({{{{}}}))"]

for i in range(0,len(Prueba),1):
	Activo = Solucion(Prueba[i])
	print(Activo,Prueba[i])

