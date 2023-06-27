# En 2022 el pa´ıs A tendr´a una poblaci´on de 25 millones de habitantes
# y el pa´ıs B de 18.9 millones. Las tasas de crecimiento anual de la
# poblaci´on ser´an de 2% y 3% respectivamente. Desarrollar un
# programa que imprima el a˜no en que la poblaci´on del pa´ıs B superar´a
# a la de A

poblacion_a = 25  # Población del país A en millones
poblacion_b = 18.9  # Población del país B en millones
tasa_crecimiento_a = 0.02  # Tasa de crecimiento anual del país A (2%)
tasa_crecimiento_b = 0.03  # Tasa de crecimiento anual del país B (3%)

anio = 2022  # Año inicial

while poblacion_a >= poblacion_b:
    poblacion_a += poblacion_a * tasa_crecimiento_a
    poblacion_b += poblacion_b * tasa_crecimiento_b
    anio += 1

print(f"La población del país B superará a la del país A en el año: {anio}")
