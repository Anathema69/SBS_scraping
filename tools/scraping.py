#LIBRERÍAS
#===========

import requests
import os

from tools import otras_utilidades


def download_file(url, dest_folder):
    """
    Descarga un archivo desde una URL y lo guarda en una carpeta de destino.

    Parámetros:
    url (str): La URL del archivo que se desea descargar.
    dest_folder (str): La ruta de la carpeta donde se guardará el archivo descargado.

    Retorna:
    str: Un mensaje de error si la descarga falla, de lo contrario no retorna nada.
    """
    response = requests.get(url)
    if response.status_code == 200:
        file_name = os.path.join(dest_folder, url.split('/')[-1])

        with open(file_name, 'wb') as file:
            file.write(response.content)
    else:
        return f"Error: {response.status_code}"



def web_scraping(carpeta_destino, start, end,list_cod_sbs):
    """

    :param carpeta_destino:
    :param start:
    :param end:
    :param list_cod_sbs:
    :return:
    """

    # Crea el directorio si no existe
    # subir un nivel fuera de la carpeta tools y guardar dentro de la carpeta ''
    carpeta_destino = os.path.join('./', 'descargas',carpeta_destino)

    os.makedirs(carpeta_destino, exist_ok=True)

    #listar archivos que están en la carpeta
    list_archivos_existentes = os.listdir(carpeta_destino)

    for cod_sbs in list_cod_sbs:
        for year in range(start, end + 1):
            for month in range(1, 13):
                full_month = otras_utilidades.get_mes_inverso(month, 0)
                sort_month = otras_utilidades.get_mes_inverso(month, 1)
                archivo = f"{cod_sbs}-{sort_month}{year}.XLS"

                if not archivo in list_archivos_existentes:
                    url = f'https://intranet2.sbs.gob.pe/estadistica/financiera/{year}/{full_month}/{cod_sbs}-{sort_month}{year}.XLS'
                    try:
                        download_file(url, carpeta_destino) #intentamos descargar
                    except:
                        pass #en caso de error intentar con el siguiente

