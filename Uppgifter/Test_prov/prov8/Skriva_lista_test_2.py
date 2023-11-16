import random

lista = []

tal = random.randint(1,6)

for i in range(20):
    lista.append(random.randint(1,6))
print(lista)
print("antal treor", lista.count(3))