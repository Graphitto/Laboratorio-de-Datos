# Clase 1 - Teorica -- Labo de Datos (15/08)

# IMPORTs
'''
import random
print(random.random()) # '''

# ABRIR ARCHIVOS 
'''
# Forma 1 de abrir archivos
f = open('Clase 02/datame.txt', 'rt' ) # r == 'read', t == 'text'
data = f.read()
f.close()

data
print(data)

# Forma 2 de abrir archivos
with open('Clase 02/datame.txt', 'rt') as file:
    # for line in file: # esto lee linea a linea
    data = file.read()
    # Al salir se cierra el archivo solo

data # data sigue viviendo afuera del with open as file (!!!)
print(data) # '''

# Agregar info creando un nuevo archivo
'''
new_data = '2024 seguimos con DATAME\n\n' + data
new_data = new_data + 'Direccion de carrera LCD'

datame = open('datame_2024.txt', 'w') # solo write
datame.write(new_data)
datame.close() # '''

# ARCHIVOS CSV

# Ejemplo de como mostrar la primera columna
'''
path_relativo = 'Clase 02/'
nombre_archivo = 'cronograma_sugerido.csv'
lista_de_materias = []
with open(path_relativo + nombre_archivo, 'rt') as file:
    for linea in file:
        datos_linea = linea.split(',')
        lista_de_materias += [datos_linea[1]]
        # print(datos_linea[1])

for x in lista_de_materias:
    print(x) # El print corrije formato del primer nivel (si hiciéramos print(lista_de_materias), imprime la lista de strings, pero los strings salen mal si tienen tildes)
# print(lista_de_materias) # sale mal con las tildes # '''

# Ejemplo de importar modulo CSV (no se usa tanto... mejor Pandas)
'''
import csv
path_relativo = 'Clase 02/'
nombre_archivo = 'cronograma_sugerido.csv'

f = open(path_relativo + nombre_archivo)
filas = csv.reader(f)
# encabezado = next(filas) # En caso que la primera fila sea un encabezado (los nombres de las columnas)
for fila in filas:
    print(fila)
f.close # '''

# PANDAS

# Ejemplo de creacion de DataFrame
import pandas as pd

'''
d = {
    'nombre' : ['Antonio', 'Brenda', 'Camila', 'Rodrigo'],
    'apellido' : ['Restrepo', 'Saenz', 'Torres', 'Urondo'],
    'lu' : ['78/23', '449/22', '111/24', '1/21']
}

df = pd.DataFrame(data = d)
df.set_index('lu', inplace = True)

from IPython.display import display
display(df)

print('')

from tabulate import tabulate
print(tabulate(df, headers = 'keys', tablefmt = 'psql')) # '''


# Abrir CSV con Pandas
# '''
path_relativo = 'Clase 02/'
nombre_archivo = 'cronograma_sugerido.csv'
df = pd.read_csv(path_relativo + nombre_archivo)

# df = pd.read_csv(path_relativo + nombre_archivo, index_col = 0) # especificar la columna id
# df = pd.read_csv(path_relativo + nombre_archivo, header = 0) # especificar fila con nombres de columnas
# '''