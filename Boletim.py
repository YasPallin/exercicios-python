#Verificando notas

print("Central de Verificação de Notas")

sair = False

while sair == False: 
	nome = input("Insira o nome do Aluno: ")

	nota1 = input("Insira a primeira nota semestral: ")
	nota1 = float(nota1)

	nota2 = input ("Insira a segunda nota semestral: ")
	nota2 = float(nota2)

	notafinal = (nota1 + nota2)/2
	notafinal = float(notafinal)

	if notafinal < 7:
		notafinal = str(notafinal)
		print(notafinal + ", " + nome + " está reprovado (a)")

	else: 
		notafinal = str(notafinal)
		print(notafinal + ", " + nome + " está aprovado (a)")

	teste = input ("Deseja verificar outro aluno? Utilize s para SIM e n para NÃO: ")

	if teste == "n":
		sair = True

print("Programa de verificação de notas encerrado.")