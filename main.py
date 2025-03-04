# main.py
from tools.scraping import web_scraping


def main():

    # Llamamos a la función que está en tools/scraping.py

    carpeta_destino = "Patrimonio_Efectivo"
    start = 2020
    end = 2024
    list_cod_sbs = ['C-1257']

    web_scraping(carpeta_destino, start, end, list_cod_sbs)
    print(f"Datos extraídos en la carpeta", carpeta_destino)

if __name__ == "__main__":
    main()

