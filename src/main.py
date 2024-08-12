import matplotlib.pyplot as plt
import numpy as np


def beverton_holt(p_n, i, k, c):
    return (i * p_n) / (1 + (i - 1) * p_n / k) - c


def find_c_beverton_holt(p_0, i, k):
    c = 0
    while True:
        n_t = p_0
        for _ in range(generations):
            n_t = beverton_holt(n_t, i, k, c)
            if n_t < 0:
                return c - 1
        c += 1


def list_beverton_holt_population(p0, i, k, c):
    population_b_h = [p0]
    for _ in range(generations):
        n_next = beverton_holt(population_b_h[-1], i, k, c)
        population_b_h.append(n_next)
    return population_b_h


def hassell(n_t, i, k, c, e_0):
    return (i * n_t) / (1 + ((i - 1) / k) * n_t) ** e_0 - c


def find_c_hassell(n_t_initial, i, k, e_0):
    c = 0
    while True:
        n_t = n_t_initial
        for _ in range(generations):
            n_t = hassell(n_t, i, k, c, e_0)
            if n_t < 0:
                return c - 1
        c += 1


def list_hassell_population(p0, i, k, c, e_0):
    population_h = [p0]
    for _ in range(generations):
        n_next = hassell(population_h[-1], i, k, c, e_0)
        population_h.append(n_next)
    return population_h


def ricker(n_t, i, k, c):
    return n_t * np.exp(i * (1 - n_t / k)) - c


def list_ricker_population(p0, i, k, c):
    population_r = [p0]
    for _ in range(generations):
        n_next = ricker(population_r[-1], i, k, c)
        population_r.append(n_next)
    return population_r


# Función para encontrar el valor de c en el MSY para el modelo de Ricker
def find_c_ricker(n_t_initial, i, k):
    c = 0
    while True:
        n_t = n_t_initial
        for _ in range(generations):
            n_t = ricker(n_t, i, k, c)
            if n_t < 0:
                return c - 1
        c += 1


# Solicitar los valores de N_t, R_0, k, generaciones y e en una línea separados por espacios
input_values = input("Ingresa p inicial, t crecimiento, capacidad, periodos y c de linealidad separados por espacio: ")

# Dividir los valores ingresados y convertirlos a float
p, r, k0, generations, e = map(float, input_values.split())
generations = int(generations)

population_bh = list_beverton_holt_population(p, r, k0, 0)
population_bh2 = list_beverton_holt_population(p, r, k0, find_c_beverton_holt(p, r, k0))
population_bh3 = list_beverton_holt_population(p, r, k0, find_c_beverton_holt(p, r, k0) - 1)
population_bh4 = list_beverton_holt_population(p, r, k0, find_c_beverton_holt(p, r, k0) + 1)

c_beverton = find_c_beverton_holt(p, r, k0)
print(f'Con el modelo Beverton-Holt la máxima cantidad de pollos que puede vender sin que comprometa la regeneración es: {c_beverton}')

# Gráfica de la población
plt.plot(population_bh, label='Población sin ventas')
plt.plot(population_bh2, label='Población con ventas iguales al MSY')
plt.plot(population_bh3, label='Población con ventas iguales al MSY - 1')
plt.xlabel('Generaciones')
plt.ylabel('Población de pollos')
plt.legend()
plt.title('Modelo de Beverton-Holt para la Dinámica Poblacional Avícola')
plt.show()


plt.plot(population_bh, label='Población sin ventas')
plt.plot(population_bh2, label='Población con ventas iguales al MSY')
plt.plot(population_bh4, label='Población con ventas iguales al MSY + 1')
plt.xlabel('Generaciones')
plt.ylabel('Población de pollos')
plt.legend()
plt.title('Modelo de Beverton-Holt para la Dinámica Poblacional Avícola')
plt.show()

population_hassell = list_hassell_population(p, r, k0, 0, e)
population_hassell2 = list_hassell_population(p, r, k0, find_c_hassell(p, r, k0, e), e)
population_hassell3 = list_hassell_population(p, r, k0, find_c_hassell(p, r, k0, e) - 1, e)
population_hassell4 = list_hassell_population(p, r, k0, find_c_hassell(p, r, k0, e) + 1, e)

c_hassell = find_c_hassell(p, r, k0, e)
print(f'Con el modelo Hassell la máxima cantidad de pollos que puede vender sin que comprometa la regeneración es: {c_hassell}')

plt.plot(population_hassell, label='Población sin ventas')
plt.plot(population_hassell2, label='Población con ventas iguales al MSY')
plt.plot(population_hassell3, label='Población con ventas iguales al MSY - 1')
plt.xlabel('Generaciones')
plt.ylabel('Población de pollos')
plt.legend()
plt.title('Modelo de Hassell para la Dinámica Poblacional Avícola')
plt.show()


plt.plot(population_hassell, label='Población sin ventas')
plt.plot(population_hassell2, label='Población con ventas iguales al MSY')
plt.plot(population_hassell4, label='Población con ventas iguales al MSY + 1')
plt.xlabel('Generaciones')
plt.ylabel('Población de pollos')
plt.legend()
plt.title('Modelo de Hassell para la Dinámica Poblacional Avícola')
plt.show()

population_ricker = list_ricker_population(p, r, k0, 0)
population_ricker2 = list_ricker_population(p, r, k0, find_c_ricker(p, r, k0))
population_ricker3 = list_ricker_population(p, r, k0, find_c_ricker(p, r, k0) - 1)
population_ricker4 = list_ricker_population(p, r, k0, find_c_ricker(p, r, k0) + 1)

c_ricker = find_c_ricker(p, r, k0)
print(f'Con el modelo de Ricker la máxima cantidad de pollos que puede vender sin que comprometa la regeneración es: {c_ricker}')

plt.plot(population_ricker, label='Población sin ventas')
plt.plot(population_ricker2, label='Población con ventas iguales al MSY')
plt.plot(population_ricker3, label='Población con ventas iguales al MSY - 1')
plt.xlabel('Generaciones')
plt.ylabel('Población de pollos')
plt.legend()
plt.title('Modelo de Ricker para la Dinámica Poblacional Avícola')
plt.show()

plt.plot(population_ricker, label='Población sin ventas')
plt.plot(population_ricker2, label='Población con ventas iguales al MSY')
plt.plot(population_ricker4, label='Población con ventas iguales al MSY + 1')
plt.xlabel('Generaciones')
plt.ylabel('Población de pollos')
plt.legend()
plt.title('Modelo de Ricker para la Dinámica Poblacional Avícola')
plt.show()

# 600 1.4 800 200 1.2
