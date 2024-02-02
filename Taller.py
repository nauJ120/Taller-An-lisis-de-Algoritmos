import random
import pandas as pd
import time
import matplotlib.pyplot as plt


def generar_registros(numRegistros):
  registros = []

  for i in range(1, numRegistros + 1):
    id = i
    cadena = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    edad = random.randint(18, 99)
    buleano = random.choice([True, False])
    registros.append([id, cadena, edad,
                      buleano])  #se agregan los registros a la lista
  return registros


def buscarPorId(lista, valor):  #busqueda binaria
  izq = 0
  der = len(lista) - 1
  encontrado = False
  while izq <= der and not encontrado:
    medio = (izq + der) // 2
    if lista[medio][0] == valor:
      encontrado = True
    else:
      if valor < lista[medio][0]:
        der = medio - 1
      else:
        izq = medio + 1
  return encontrado, medio


def buscarPorNombre(lista, valor):
  posicion = 0
  encontrado = False
  while posicion < len(lista) and not encontrado:
    if lista[posicion][1] == valor:
      encontrado = True
    else:
      posicion += 1
  return encontrado, posicion


numRegistros = 155  # Puedes ajustar según sea necesario
lista_registros = generar_registros(numRegistros)

while True:
  print("\nMenú:")
  print("1. Buscar por Id")
  print("2. Buscar por nombre")
  print("3. Salir")

  opcion = input("Seleccione una opción (1, 2, o 3): ")

  if opcion == "1":
    valor = int(input("Ingrese el valor a buscar: "))
    encontrado, posicion = buscarPorId(lista_registros, valor)
    if encontrado:
      print(f"El Id {valor} se encuentra en la posición {posicion}.")
      registro_encontrado = lista_registros[posicion]
      print("ID:", registro_encontrado[0])
      print("Nombre:", registro_encontrado[1])
      print("Edad:", registro_encontrado[2])
      print("Paga impuesto:", registro_encontrado[3])
    else:
      print(f"Este id {valor} no se encuentra en la lista.")

  elif opcion == "2":
    valor = input("Ingrese el nombre a buscar: ")
    encontrado, posicion = buscarPorNombre(lista_registros, valor)
    if encontrado:
      print(f"El nombre {valor} se encuentra en la posición {posicion}.")
      registro_encontrado = lista_registros[posicion]
      print("ID:", registro_encontrado[0])
      print("Nombre:", registro_encontrado[1])
      print("Edad:", registro_encontrado[2])
      print("Paga impuesto:", registro_encontrado[3])
    else:
      print(f"Este nombre {valor} no se encuentra en la lista.")
  elif opcion == "3":
    print("Saliendo del programa. ¡Hasta luego!")
    break
  else:
    print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

tiempos = {'buscarPorId': [], 'buscarPorNombre': []}

# Medir tiempos
for i in range(1, numRegistros + 1):
  inicio = time.perf_counter()
  buscarPorId(lista_registros, i)
  fin = time.perf_counter()
  diferencia = fin - inicio
  tiempos['buscarPorId'].append(diferencia)

  inicio = time.perf_counter()
  buscarPorNombre(lista_registros, lista_registros[i - 1][1])
  fin = time.perf_counter()
  diferencia = fin - inicio
  tiempos['buscarPorNombre'].append(diferencia)

#crear un dataframe
df = pd.DataFrame(tiempos)
df.index.name = 'n'
df.reset_index(inplace=True)

#Se grafica el tiempo de ejecucion
plt.plot(df['n'], df['buscarPorId'], label='buscarPorId')
plt.plot(df['n'], df['buscarPorNombre'], label='buscarPorNombre')

plt.legend()
plt.xlabel('Valores')
plt.ylabel('Tiempos')
plt.title('Tiempos de ejecución')
plt.savefig('TallerClase.png')
plt.show()
##BUENAS NOCHEEEEEES :)
