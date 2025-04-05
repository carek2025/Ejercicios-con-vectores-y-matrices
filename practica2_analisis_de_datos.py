import numpy as np
import matplotlib.pyplot as plt

# Datos de ventas
ventas = np.array([[100, 150, 200],  
                   [120, 130, 180],  
                   [80, 100, 140]])

# Total de ventas por producto
total_por_producto = np.sum(ventas, axis=1)

# Total de ventas por mes
total_por_mes = np.sum(ventas, axis=0)

# Porcentaje de ventas por producto respecto al total por mes
porcentaje_ventas = (ventas / total_por_mes) * 100

# Crear gráficos

# Gráfico de barras: Total de ventas por producto
productos = ['Producto A', 'Producto B', 'Producto C']
plt.bar(productos, total_por_producto, color='skyblue')
plt.title('Total de Ventas por Producto')
plt.xlabel('Productos')
plt.ylabel('Ventas Totales')
plt.show()

# Gráfico de líneas: Ventas por mes
meses = ['Enero', 'Febrero', 'Marzo']
plt.plot(meses, ventas[0], label='Producto A', marker='o')
plt.plot(meses, ventas[1], label='Producto B', marker='o')
plt.plot(meses, ventas[2], label='Producto C', marker='o')
plt.title('Ventas por Mes')
plt.xlabel('Meses')
plt.ylabel('Ventas')
plt.legend()
plt.show()

# Gráfico de barras apiladas: Porcentaje de ventas por producto y mes
plt.bar(meses, porcentaje_ventas[0], label='Producto A', color='lightcoral', alpha=0.7)
plt.bar(meses, porcentaje_ventas[1], bottom=porcentaje_ventas[0], label='Producto B', color='lightgreen', alpha=0.7)
plt.bar(meses, porcentaje_ventas[2], bottom=porcentaje_ventas[0] + porcentaje_ventas[1], label='Producto C', color='lightblue', alpha=0.7)
plt.title('Porcentaje de Ventas por Producto y Mes')
plt.xlabel('Meses')
plt.ylabel('Porcentaje de Ventas')
plt.legend()
plt.show()

# Gráfico de líneas: Total de ventas por mes
plt.plot(meses, total_por_mes, marker='o', color='purple', label='Total por Mes')
plt.title('Total de Ventas por Mes')
plt.xlabel('Meses')
plt.ylabel('Ventas Totales')
plt.legend()
plt.show()
