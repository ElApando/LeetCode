# Mi solución

def Solucion(l1:[],l2:[]) -> list:
	Lista = []
	Acarreo = 0
	
	while l1 or l2 or Acarreo:
		
		numero1 = l1.pop() if l1 else 0
		numero2 = l2.pop() if l2 else 0
		suma = numero1+numero2+Acarreo
		print(numero1,numero2,suma,Acarreo,suma%10)
		Acarreo = suma // 10
		Lista.append(suma % 10)

	return Lista

Lista1 = [[2,4,3],[0],[9,9,9,9,9,9,9]]; Lista2 = [[5,6,4],[0],[9,9,9,9]]

for i in range(0,len(Lista1),1):
	Activo = Solucion(Lista1[i],Lista2[i])
	print(Activo)

# Solución LeetCode

# class Solution:
#     def addTwoNumbers(self, l1: [], l2: []) -> list:
#         Lista = ListNode()
#         Resultado = Lista

#         Total = Guarda = 0

#         while l1 or l2 or Guarda:
#             Total = Guarda

#             if l1:
#                 Total += l1.val
#                 l1 = l1.next
#             if l2:
#                 Total += l2.val
#                 l2 = l2.next
            
#             Guarda = Total // 10
#             Lista.next = ListNode(Total % 10)
#             Lista = Lista.next
        
#         return Resultado.next