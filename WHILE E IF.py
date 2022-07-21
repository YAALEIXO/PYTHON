import pandas as pd
#-----------------------

Time = []


print('Bom dia', )
Nome = input('Qual é seu nome por favor?   ')
print('Olá', Nome, 'tudo bem?  ')
print('vamos montar nosso time')
resposta = input("Responda s/n ", )

while len(Time) < 5:

    if resposta in 'nN':
        print('Você decidiu não continuar!')
        break

    elif len(Time) < 5 and resposta in'sS':
        print('vamos continuar')
        jogador = input('nome  ')
        Time.append(jogador)
        print('faltam', 5 - len(Time))

    elif resposta != 'sS' or resposta != 'nN':
        resposta =input('Responda s/n')
        continue

if len(Time) == 0:
    print("")
else:
    print(Nome,'seus', len(Time),'jogadores são', Time)

dct1 = pd.DataFrame({'Id':[1,2,3,4,5],'Jogadores':Time})


print (dct1)







