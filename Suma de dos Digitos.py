def Solu(Datos, Objetivo):

	for i in range(0,len(Datos),1):
		for j in range(0,len(Datos),1):

			if Datos[i] == Datos[j]:
				if i == j:
					pass

				else:
					Suma = Datos[i] + Datos[j]

					if Suma == Objetivo:
						print(f"Objetivo: {Suma} , {Datos[i]} , {Datos[j]} , {i} , {j}")
						return True

					else:
						pass

			elif Datos[i] != Datos[j]:
				Suma = Datos[i] + Datos[j]
				if Suma == Objetivo:
					print(f"Objetivo: {Suma} , {Datos[i]} , {Datos[j]} , {i} , {j}")
					return True
				else:
					pass

			else:
				pass

	return False

Pruebas = [[2,7,11,15],[3,2,4],[3,3]]; Numero = [9,6,6]

for i in range(0,len(Pruebas),1):
	Activo = Solu(Pruebas[i],Numero[i])
