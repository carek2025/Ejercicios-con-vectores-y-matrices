import numpy as np


vec1 = np.array([2, 3])
vec2 = np.array([4, 1])
suma = np.add(vec1, vec2)  # Sumé 2+4 y 3+1, me dió [6 4]
print("Suma con np.add:", suma)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
multi_elemento = np.multiply(a, b)  # Multipliqué 1x4, 2x5 y 3x6 → salio [4 10 18]
print("Multiplicación elemento a elemento:", multi_elemento)

div = np.divide(b, a)  # 4/1, 5/2, 6/3 → [4. 2.5 2.]
print("División:", div)


matriz_diag = np.diag([7, 8, 9])  # Cree una matriz con esos números en la diagonal → lo demás queda en cero
print("Matriz diagonal:\n", matriz_diag)


diagonal = np.diag(matriz_diag)  # Saqué solo los valores de la diagonal → [7 8 9]
print("Diagonal extraída:", diagonal)


ceros = np.zeros((3, 3))  # Generé una matriz 3x3 con puritos ceros
print("Matriz de ceros:\n", ceros)


unos = np.ones((2, 4))  # Cree una matriz de 2 filas y 4 columnas llena de puros unos
print("Matriz de unos:\n", unos)


aleatoria = np.random.rand(2, 2)  # Generé una matriz 2x2 con valores random entre 0 y 1
print("Matriz aleatoria:\n", aleatoria)

redondeada = np.round(aleatoria, 2)  # La redondié a 2 decimales pa que no se vea tan fea
print("Matriz redondeada:\n", redondeada)


original = np.array([1, 2, 3, 4, 5, 6])
reformada = original.reshape((2, 3))  # La acomode en 2 filas y 3 columnas → [[1 2 3], [4 5 6]]
print("Matriz con reshape:\n", reformada)


m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
concat = np.concatenate((m1, m2), axis=0)  # Pegue m1 y m2 una debajo de otra
print("Concatenación vertical:\n", concat)

mat = np.array([[3, 7], [1, 9]])
max_val = np.max(mat)  # El mayor de todos es 9
min_val = np.min(mat)  # El menor de todos es 1
print("Máximo:", max_val)
print("Mínimo:", min_val)


media = np.mean(mat)  # Sume todos y dividí entre la cantidad → promedio
suma_total = np.sum(mat)  # Sume toditos los valores 3+7+1+9 = 20
print("Media:", media)
print("Suma total:", suma_total)
