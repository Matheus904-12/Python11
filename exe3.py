import os
os .system("cls")

print("3)Desenvolva um programa que cadastra alunos.")

#lista = [cód; desc; preço]
#ranger para buscar a seqência de id criado conforme o cadastro criado
#cód inicia em 100 e adicionar um mising
#

#Variáveis

confirm = "s"
confirmar = "s"

#Funções

def menu(): #Menu, ele será a primeira coisa a ser chamada, retorna um input
    print("1) Administrador")
    print("2) Operador")
    print("3) Sair")
    option = str(input("Digite qual opção deseja (escreva um número de 1 a 3).")).strip()
    while option == "" and option != "1" and option != "2" and option != "3":
        option = str(input("Por favor, digite um número correto (de 1 a 3): "))

    return option


def menuADM():
    print("1) Administrador")
    print("2) Operador")
    print("3) Sair")
    print("4) Excluir")
    print("5) Voltar")
    optionadm = str(input("Digite qual opção deseja (escreva um número de 1 a 5).")).strip()
    while optionadm == "" and optionadm != "1" and optionadm != "2" and optionadm != "3" and optionadm != "4" and optionadm != "5":
        optionadm = str(input("Por favor, digite um número correto (de 1 a 5): "))

    return optionadm

def cadastro(): #Abre arquivo, pega nome, coloca no arquivo, repita.
    arquivo = open("exe3/cadastro.txt", "a")
    nome = str(input("Digite o nome do aluno a ser cadastrado: "))
    arquivo.write(str("nome:" + nome + " "))
    email = str(input("Digite o e-mail do aluno a ser cadastrado: "))
    arquivo.write(str("e-mail:" + email + " "))
    curso = str(input("Digite o curso do aluno: "))
    arquivo.write(str("curso:" + curso + " ") + "\n")
    arquivo.close()
    print("\nArquivo gerado com sucesso!")

def listar(): #Essa foi complicada.
    arquivo = open("exe3/cadastro.txt", "r")
    listar = arquivo.readlines() #Irá ler linha por linha
    arquivo.close()

    if len(listar) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for linha in listar: #Ponteiro para a repetição
            start_fulano = linha.find("nome:") + len("nome:") #Acha a palavra nome, tem indice 0, por isso coloquei + len("nome"), quero saber o nome do aluno, não "nome:fulano". Poderia ter colocado só 5 também, mas ficaria menos escalavel.
            end_fulano = linha.find("e-mail:") #Vai achar o índice do email, ou seja, quando ele começa
            name = linha[start_fulano:end_fulano].strip() #O professor ensinou esse método em sala da aula, ele vai do ponto A até o B da lista, no caso, onde começa o nome e onde começa o email. Eu não sei se o professor ensinou o strip em sala de aula, mas eu vi isso naquele desafio da Erika junto com o Luigi :D
            print(name) #Vai retornar o nome do aluno



def editar():
    print("editar")

def buscar():
    arquivo = open("exe3/cadastro.txt", "r")
    listar = arquivo.readlines() #Vai ler o arquivo todo
    arquivo.close()

    searchFulano = str(input("Digite o nome do aluno que quer buscar: ")).strip() #input
    encontrado = False #A priori, falso, o código vai falar se é verdadeiro

    for linha in listar: #Vai procurar na linha toda
        if f"nome:{searchFulano}" in linha: #Se o nome estiver em linha: encontrado
            print("Aluno encontrado! \n")
            print(linha)
            encontrado = True #Se verdadeiro, o encontrado se torna True e passa direto pelo if not
            break

    if not encontrado: #inverte o valor da condição, aqui seria verdadeiro, pois o aluno não foi encontrado, então inverti para que se o código for verdadeiro, ele passa direto, se for falso ele vai pra cá, estava colando isso no for, estava errado.
        print("Aluno não encontrado.")

def remove():
    arquivo = open("exe3/cadastro.txt", "r")
    listar = arquivo.readlines()
    delete = str(input("Digite o nome do aluno que você quer deletar: ")).strip()
    encontrado = False 
    nova_linhas = []

    for linha in listar:
        if f"nome:{delete}" in linha:
            print("Aluno encontrado! \n")
            sure = str(input("Você tem certeza que deseja apagar o usuário? (s/n): ")).strip().lower()
            if sure == "s":
                print("aluno removido com sucesso \n")
                encontrado = True
            else:
                print("Compreensível, tenha um bom dia. \n")
                nova_linhas.append(linha)

        else:
            nova_linhas.append(linha)

    if not encontrado:
        print("Aluno não encontrado. \n")

    arquivo = open("exe3/cadastro.txt", "w")
    arquivo.writelines(nova_linhas)

    arquivo.close()

#Main

while confirm == "s":

    escolha = menu() # mostrará o menu, e o resultado virará uma variável

    if escolha == "1": #dependendo da escolha o comando irá fazer algo
        escolhaADM = menuADM()
        print("A opção desejada foi de Administrador \n")
        while confirmar == "s":
            if escolhaADM == "1":
                #cadastro()
                print("funcionou")
                confirmar = "n"

            elif escolhaADM == "2":
                #listar()
                print("funcionoiu")
                confirmar = "n"

            elif escolhaADM == "3":
                #editar()
                print("funcionoiu")
                confirmar = "n"

            elif escolhaADM == "4":
                #remove()
                print("funcionoiu")
                confirmar = "n"

            elif escolhaADM == "5":
                confirmar = "n"
                #escolha()
                print("funcionou")
                confirmar = "n"
            else:
                print("[ERRO] Dígito inválido \n")
                confirmar = "n"

    elif escolha == "2":
        print("A opção desejada foi de Operador \n")
    elif escolha == "3":
        print("Fim da execução")
    else:
        print("[ERRO] Dígito inválido \n")


    