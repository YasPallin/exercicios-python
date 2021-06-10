print ("Tabuadora")
nome = input ("Qual o seu nome? ")
num1 = input ( nome + ", você quer saber a tabuada de qual número? ")
num1 = int(num1)
operador = input ("E qual será o operador? Digite + para adição, - para subtração, / para divisão e * para multiplicação: ")
num2 = 1
limite = 10

print ("A tabuada é: ")

while num2 <= limite:

	if operador == "+":
		tabuada = num1 + num2
		print ("{0} + {1} = {2}".format(num1, num2, tabuada))
		num2 = num2 + 1

	if operador == "-":
		tabuada = num1 - num2
		print ("{0} - {1} = {2}".format(num1, num2, tabuada))
		num2 = num2 + 1

	if operador == "/":
		tabuada = num1 / num2
		print ("{0} / {1} = {2:.3g}".format(num1, num2, tabuada))
		num2 = num2 + 1

	if operador == "*":
		tabuada = num1 * num2
		print ("{0} x {1} = {2}".format(num1, num2, tabuada))
		num2 = num2 + 1