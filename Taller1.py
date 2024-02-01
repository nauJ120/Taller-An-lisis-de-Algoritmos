import random


def generar_registros(numRegistros):
  
  registros = []

  for i in range(1, numRegistros+1):
    id = i
    cadena = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    edad = random.randint(18, 99)
    buleano = random.choice([True, False])
    registros.append([id, cadena, edad, buleano])
  
  return registros


print(generar_registros(10))
