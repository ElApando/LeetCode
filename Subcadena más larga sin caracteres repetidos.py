# def Solucion(s: str) -> int:
# 	Cadena = s.lower()
# 	Lista = set()
# 	Longitd = 0
# 	Conteo = 0
	
# 	for i in range(0,len(Cadena),1):
# 		while Cadena[i] in Lista:
# 			Lista.remove(Cadena[i])
# 			Conteo += 1
# 		Lista.add(Cadena[i])
# 		Longitd = max(Longitd,i-Conteo+1)

# 	return Longitd

# Prueba = ["AbcabCBB","BBBBB","PWWKEW"]

# for i in range(0,len(Prueba),1):
# 	Activo = Solucion(Prueba[i])
# 	print(Activo,Prueba[i])

# print(dir(str))

def Solucion(s: str) -> int:

	Cadena = s.lower()
	Guarda = ""
	Longitud,Conteo = 0,0
	Diccionario = {}

	while Conteo < len(s):
	    Caracater = s[Conteo]
	    if Caracater not in Diccionario:
	        Diccionario[Caracater] = Conteo  
	    else:
	        if Diccionario[Caracater]+ 1 > Longitud:
	            Longitud = Diccionario[Caracater]+1
	        Diccionario[Caracater] = Conteo
	    
	    if len(Guarda) < Conteo-Longitud+1:
	        Guarda = s[Longitud:Conteo+1]

	    Conteo += 1
	
	if len(Guarda) < Conteo-Longitud:
	    Guarda = s[Longitud:Conteo]   
	
	return len(Guarda)
	# Guarda = ""
	# Diccionario = {}
	# Longitud = 0
	# Conteo = 0

	# while Conteo < len(Cadena): # Mientras el conteo es menor al tamaño de la cadena 
	# 	Caracater = Cadena[Conteo] # Se recorre a cadena 
		
	# 	if Caracater not in Diccionario: # Sí caracter no esta en el diccionario,
	# 		Diccionario[Caracater] = Conteo  # Se agrega el caracter como llave y como valor se coloca la posición
			
	# 	else: #Caso contrario, Ya se encentra en el dccionario... 	
	# 		if Diccionario[Caracater] + 1 > 1: # Si la posicion más 1 es mayor a 1
	# 			Longitud = Diccionario[Caracater] + 1 # Longitud Toma el valor más 1
	# 		Diccionario[Caracater] = Conteo # Se contina con la secencia 

	# 	if len(Guarda) < Conteo-Longitud+1:
	# 		Guarda = Cadena[Longitud:Conteo+1]

	# 	Conteo += 1

	# if len(Cadena) < Conteo-1:
	# 	Guarda = Cadena[Longitud:Conteo]

	# return len(Guarda)

Prueba = ["AbcabCBB","BBBBB","PWWKEW"]

for i in range(0,len(Prueba),1):
	Activo = Solucion(Prueba[i])
	print(Activo,Prueba[i])

        # ls = ""
        # l,r = 0,0
        # ci = {}

        # while r < len(s):
        #     c = s[r]
        #     if c not in ci:
        #         ci[c] = r  
        #     else:
        #         if ci[c]+ 1 > l:
        #             l = ci[c]+1
        #         ci[c] = r
            
        #     if len(ls) < r-l+1:
        #         ls = s[l:r+1]

        #     r += 1
        
        # if len(ls) < r-l:
        #     ls = s[l:r]   
        
        # return len(ls)