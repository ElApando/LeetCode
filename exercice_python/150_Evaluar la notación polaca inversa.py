""" 150. Evaluate Reverse Polish Notation

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

def solution(ls_tokens: list) -> int:
	""" Solución 

	Parameters:
		- ls_tokens *(list)* - Operación que se debe de realizar
	Returns:
		- *(int)* - Resultado de la operación 
	
	"""

	ls_save = []
	in_flag = 0

	for ii in ls_tokens:
		if ii.isdigit():
			ls_save.append(int(ii))

		else:
			try:
				Valor = int(ii)
				ls_save.append(Valor)
				in_flag = 1

			except ValueError:
				pass

			if in_flag == 0:
				in_num_1 = ls_save.pop()
				in_num_2 = ls_save.pop()

				if ii == "+":
					result = in_num_2 + in_num_1
				elif ii == "-":
					result = in_num_2 - in_num_1
				elif ii == "*":
					result = in_num_2 * in_num_1
				elif ii == "/":
					if in_num_1 != 0:
						result = in_num_2 / in_num_1
					else:
						pass
				ls_save.append(int(result))

				if len(ls_tokens) == 1:
					return ls_tokens.pop()
			else:
				in_flag = 0

	return ls_save[0]

ls_prove = [["4","3","-"],["2","1","+","3","*"],["4","13","5","/","+"],["10","6","9","3","+","-11","*","/","*","17","+","5","+"]]

for ii in range(0,len(ls_prove),1):
	print(solution(ls_prove[ii]))

# Finite Incantatem
