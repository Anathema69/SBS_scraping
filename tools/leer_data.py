import pandas as pd
import os
import  re

#leer_data y retornar un df csv

carpeta_lectura = 'Patrimonio_Efectivo'
carpeta_destino = os.path.join('../', 'descargas',carpeta_lectura)
libros = os.listdir(carpeta_destino)

df_total = pd.DataFrame()

for libro in libros:
    df = pd.read_excel(os.path.join(carpeta_destino, libro))
    df_total = pd.concat([df_total, df])
    break

carpeta_salida = os.path.join(carpeta_destino, "_consolidado")
os.makedirs(carpeta_salida, exist_ok=True)

archivo_salida = os.path.join(carpeta_salida, "consolidado.xlsx")

print(archivo_salida)



