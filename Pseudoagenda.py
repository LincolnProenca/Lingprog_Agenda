import os
path = os.sys.path[0] + '\\'

def Inserir():
    nome = input("Me diga seu nome: ")
    end = input("Me diga seu endereco: ")
    tel = input("Me diga seu telefone: ")
    dados = nome + ', ' + end + ', ' + tel + ', ' + '\n'
    print("Seus dados sao: ", dados)
    arquivo = open(path + "contatos.txt","a")
    arquivo.writelines(dados)

def buscar():
    nome = input("Quem voce quer buscar?\n")
    arquivo = open(path + "contatos.txt","r")
    for linha in arquivo:
        pessoas = linha.split(', ')
        if pessoas[0].upper().find(nome.upper()) != -1:
            print('\nNome:',pessoas[0] + '\n' + 'Endereco:',pessoas[1] + '\n' + 'Telefone:',pessoas[2])

def remover():
    nome = input("Quem voce quer Remover?\n")
    arquivo = open(path + "contatos.txt","r")
    dados = arquivo.readlines()
    a = 0
    for linha in dados:
        pessoas = linha.split(', ')
        if pessoas[0].upper().find(nome.upper()) != -1:
            print('\nNome:',pessoas[0] + '\n' + 'Endereco:',pessoas[1] + '\n' + 'Telefone:',pessoas[2])
            escolha = input('Deseja remover esse contato?\n'+'Sim/Nao\n')
            if escolha.upper() == 'SIM':
                dados[a] =  ''
                print("Contato Removido")
        a += 1
    arquivo = open(path + "contatos.txt","w")
    arquivo.writelines(dados)
    
def editar():
    nome = input("Quem voce quer Editar?\n")
    arquivo = open(path + "contatos.txt","r")
    dados = arquivo.readlines()
    a = 0
    for linha in dados:
        pessoas = linha.split(', ')
        if pessoas[0].upper().find(nome.upper()) != -1:
            print('\nNome:',pessoas[0] + '\n' + 'Endereco:',pessoas[1] + '\n' + 'Telefone:',pessoas[2])
            escolha = input('Deseja editar esse contato?\n'+'Sim/Nao\n')
            if escolha.upper() == 'SIM':
                n = input("Me diga seu nome: ")
                end = input("Me diga seu endereco: ")
                tel = input("Me diga seu telefone: ")
                dados[a] =  n + ', ' + end + ', ' + tel + ', ' + '\n'
                print("Seus dados sao: ", dados[a])
        a += 1
    arquivo = open(path + "contatos.txt","w")
    arquivo.writelines(dados)



a=''
while(a.upper() != "FIM"):
    print("\nBem vindo a minha proto agenda\n")
    print("O que vc deseja fazer?")
    a = input("Digite Inserir/Buscar/Remover/Editar/FIM \n")

    if (a.upper() == "INSERIR"):
        Inserir()
    elif(a.upper() == "BUSCAR"):
        buscar()
    elif(a.upper() == "REMOVER"):
        remover()
    elif(a.upper() == "EDITAR"):
        editar()
    elif(a.upper() == "FIM"):
        pass
    else:
        print("Essa opcao nao existe")