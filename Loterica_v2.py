import random

def cartela_nova():
    cartela = []
    loop = 0
    while loop < 13:
        numero_proposto = random.randrange(1,26)
        if numero_proposto in cartela:
            continue
        cartela.append(numero_proposto)
        loop += 1
    return cartela

lista_de_cartelas = []import random

def cartela_nova():
    cartela = []
    loop = 0
    while loop < 13:
        numero_proposto = random.randrange(1,26)
        if numero_proposto in cartela:
            continue
        cartela.append(numero_proposto)
        loop += 1
    return cartela

lista_de_cartelas = []


print("\n")
print('\t\t\tGERADOR DE JODOS\n1. JOGOS de 13 NUMEROS ALEATORIOS ENTRE 1-25.\n2. NENHUM JOGO SE REPETE.\n\n')
print('Será criado um arquivo com nome de loteria.txt com todos jogos.\n')
val = input("Gerar quantos jogos?: ")
print(val)
qtd_cartelas = int(val)
print("\n")


loop = 0
while loop < qtd_cartelas:
    cartela_proposta = cartela_nova()
    if cartela_proposta in lista_de_cartelas:
        print("Ops, repetiu...")
        continue
    lista_de_cartelas.append(cartela_proposta)
    loop += 1

f = open("loteria.txt", "w")

loop = 1
for cartela in lista_de_cartelas:
    cartela_str =  ', '.join( map(str, sorted(cartela) ))
    linha = f'JOGO {loop:03}: [{cartela_str}]'
    print(linha)
    f.write(linha + "\n\n")
    loop += 1

f.close()


qtd_cartelas = 250

loop = 0
while loop < qtd_cartelas:
    cartela_proposta = cartela_nova()
    if cartela_proposta in lista_de_cartelas:
        print("Ops, repetiu...")
        continue
    lista_de_cartelas.append(cartela_proposta)
    loop += 1

f = open("loteria.txt", "w")

loop = 1
for cartela in lista_de_cartelas:
    cartela_str =  ', '.join( map(str, sorted(cartela) ))
    linha = f'JOGO {loop:03}: [{cartela_str}]'
    print(linha)
    f.write(linha + "\n")
    loop += 1

f.close()