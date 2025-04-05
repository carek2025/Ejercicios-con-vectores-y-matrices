import numpy as np

ventas = np.array([[100, 150, 200],  
                   [120, 130, 180],  
                   [80, 100, 140]])

total_por_producto = np.sum(ventas, axis=1)  
print("Total de ventas por producto:", total_por_producto)

promedio_producto = np.mean(ventas, axis=1)  
print("Promedio de ventas mensual por producto:", promedio_producto)

total_por_mes = np.sum(ventas, axis=0)  
print("Total de ventas por mes:", total_por_mes)

porcentaje_ventas = (ventas / total_por_mes) * 100  
print("Porcentaje de ventas de cada producto por mes:\n", porcentaje_ventas)

desviacion_producto = np.std(ventas, axis=1)  
print("Desviación estándar de ventas por producto:", desviacion_producto)
