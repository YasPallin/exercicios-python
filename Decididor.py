#jogo para grandes decisões

import random
desistir = False

print ("Estou aqui para te ajudar a tomar grandes decisões.")

while desistir == False:

	teste = input ("Faça a sua pergunta: ")
	print (random.choice(["Se é o que seu coração manda, vai!", "Não. Apenas não.", "Sim, você deveria fazer isso!", "Não, acho uma péssima escolha.", "Claro! O que poderia dar errado?", "Melhor não.", "Creio que sim.", "Não seria minha primeira escolha.", "Sim, acho justo."]))

	more = input ("Ajudo em algo mais? (s ou n): ")
	while more != "s" and more != "n":
		print ("Caractere inválido.")
		more = input ("s ou n? ")
		
	if more == "n":
		desistir = True
		print ("Espero ter ajudado. Obrigada e volte sempre.")


