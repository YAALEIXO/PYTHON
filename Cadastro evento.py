#-----------------VARIAVEIS----------#
import pandas as pd
Cod = []
Nome = []
Idade = []
Contato = []
Lista = {"Id": Cod, "Nome": Nome, "Idade": Idade, "Telefone": Contato}
cadastro =[]
#-----------CADASTRO-----------------#
seunome=(input("Olá qual seu nome"))
print( seunome, 'estamos prestes a iniciar o cadastro de sua lista:')
New = print('')
#---------1º CADASTRO---------------#
while New !='sS'or New !='nN':
    New = input('Deseja continuar cadstro? s ou n?  ' )

    if New =='N' or New=='n':
        break

    if New =='S' or New=='s':
        Cod.append(len(Cod)+1)
        Nome.append(str(input("qual seu nome")))
        Idade.append(int(input("qual sua idade")))
        Contato.append(str(input("Contato")))
    if len(Cod)==2:
        print ('Lista Completa')
        break
#------------Tabela de cadastro -------#
print('Finalizamos aqui!')
Tabela1 = pd.DataFrame (Lista)
#-------Tabela--------------
if len(Cod)!=0:
    print(Tabela1)









