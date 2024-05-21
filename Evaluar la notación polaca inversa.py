def Solucion(tokens: []) -> int:
	Guarda = []
	Bandera = 0

	for Elemento in tokens:

		if Elemento.isdigit():
			Guarda.append(int(Elemento))

		else:
			try:
				Valor = int(Elemento)
				Guarda.append(Valor)
				Bandera = 1

			except ValueError:
				pass

			if Bandera == 0:

				numero1 = Guarda.pop()
				numero2 = Guarda.pop()

				print(numero1,numero2,Elemento)

				if Elemento == "+":
					Resultado = numero2 + numero1
				elif Elemento == "-":
					Resultado = numero2 - numero1
				elif Elemento == "*":
					Resultado = numero2 * numero1
				elif Elemento == "/":
					if numero1 != 0:
						Resultado = numero2 / numero1
					else:
						pass
				Guarda.append(int(Resultado))

				if len(tokens) == 1:
					return tokens.pop()
			else:
				Bandera = 0

	return Guarda[0]

Prueba = [["4","3","-"],["2","1","+","3","*"],["4","13","5","/","+"],["10","6","9","3","+","-11","*","/","*","17","+","5","+"]]

for i in range(0,len(Prueba),1):
	Activo = Solucion(Prueba[i])
	print(Activo)
