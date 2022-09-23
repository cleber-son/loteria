import random
from typing import Counter
count = 0
jogos = 250
cartelas = []
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
saida = open("JOGOS.txt", "w")

while count != jogos:
    count = count+1 

    random.shuffle(numeros)
    sorteio = (numeros[0], numeros[1], numeros[2], numeros[3], numeros[4], numeros[5], numeros[6], numeros[7], numeros[8], numeros[9], numeros[10], numeros[11], numeros[12])
    cartelas.append(sorted(sorteio))
    

jogosfinais = []
x = 0
for i in cartelas:
    if i not in jogosfinais:
        x = x+1
        jogosfinais.append(i)
        print("JOGO", x,"-> ",i)
    else: 
        cartelas.append(sorted(sorteio))
        








    







