Cod = []
Nome = []
Idade = []
Contato = []
cadastro = {"Id": Cod, "Nome": Nome, "Idade": Idade, "Telefone": Contato}
print("Sejam bem vindo ao cadastro de eventos")

print("vamos começar")

Nome.append(input("qual seu nome"))
Idade.append(input("qual sua idade"))
Contato.append(input("Contato"))
New = input("Deseja realizar primeiro cadastro S ou N")
if New in "sS": Cod.append(len(Cod) + 1)

while New:
    if New != "sS" or New != 'nN':
        New = input("Deseja realizar outro cadastro? S ou N")
        if New in 'sS':
            break
            if New in "sS": Cod.append(len(Cod) + 1)
        elif New in 'nN':
            Cod.append(len(Cod) + 1)
            print('Fim')
            break

while len(Cod) < 3 and New in "sS":

    Nome.append(input("qual seu nome"))
    Idade.append(input("qual sua idade"))
    Contato.append(input("Contato"))
    New = input("Deseja realizar outro cadastro? S ou N")
    if New in "sS": Cod.append(len(Cod) + 1)
    if len(Cod) == 3:
        print("Lista completa")

    else:
        print("Sua Lista esta incompleta")
        break

else:

    print("")

print(cadastro)