import pandas as pd

# Importamos la tabla de propiedades de agua líquida comprimida
basedatos = pd.read_excel(r'C:\Users\LEON DARIO ACERO\Desktop\TATES.PY\H2O_TempComp.xlsx', sheet_name='H2O_TempComp')

# Definimos los valores de las variables iniciales
t = 25.0  # Temperatura
col_p2 = 'v'  # Columna de la tabla que contiene la propiedad 2
p2_val = 0.001  # Valor de la propiedad 2

# Buscamos coincidencias exactas en la tabla
k_c = -1  # Inicializamos la variable k_c en -1
for i in range(len(basedatos)):
    if basedatos.iloc[i, 0] == t and basedatos.iloc[i][col_p2] == p2_val:
        k_c = i  # Guardamos el número de fila en k_c
        break  # Terminamos el bucle

# Mostramos el resultado
if k_c != -1:
    print(f"Se encontró una coincidencia exacta en la fila {k_c} de la tabla.")
else:
    print("No se encontró una coincidencia exacta en la tabla.")
