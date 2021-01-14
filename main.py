import art
#Add
def add(n1, n2):
	return n1 + n2

#Subtract
def subtract(n1, n2):
	return n1 - n2

#Mutiply
def multiply(n1, n2):
	return n1 * n2

#Divide
def divide(n1, n2):
	return n1 / n2


#Recursion Function, which call itself inside the Function
def calculator():
	print(art.logo)
	operations = {'+': add, '-': subtract, '*': multiply, '/':divide}
	num1 = float(input("What's the first number?: "))
	for keys in operations:
		print(keys)

	end = False

	while not end:
		operation_symbol = input("Pick another operation: ")
		num2 = float(input("Whats the next number?: "))
		calculation_function = operations[operation_symbol]
		answer = calculation_function(num1, num2)
		print(f"{num1} {operation_symbol} {num2} = {answer}")


		do_more = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
		if do_more == 'y':
			num1 = answer
		else:
			end = True
			calculator()

calculator()
