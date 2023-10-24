import random


entrada = [random.randint(0, 20) for elemento in range(10)]
print("entrada aleatória: ", entrada)
soma, media = 0, 0
pares = []
for i in range(len(entrada)):
    if entrada[i] % 2 == 0:
        pares.append(entrada[i])
        soma += entrada[i]

media = soma/len(pares)
print(media)