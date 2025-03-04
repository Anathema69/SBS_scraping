import pandas as pd
import  re

# Función para transformar el periodo a formato fecha
def transformar_periodo(periodo):
    # Diccionario para mapear los códigos de mes a números de mes
    meses = {
        'en': '01',
        'fe': '02',
        'ma': '03',
        'ab': '04',
        'my': '05',
        'jn': '06',
        'jl': '07',
        'ag': '08',
        'se': '09',
        'oc': '10',
        'no': '11',
        'di': '12',
    }
    mes_codigo = periodo[:2]
    anio = periodo[2:]
    mes = meses.get(mes_codigo, '01')  # Por defecto enero si no se encuentra el mes
    return pd.to_datetime(f'01/{mes}/{anio}', format='%d/%m/%Y')


def get_mes_inverso(num_mes: int, cod_mes: int):
    # Diccionario inverso para mapear números de mes a nombres y códigos de mes
    meses_inverso = {
        1: ['enero', 'en'],
        2: ['febrero', 'fe'],
        3: ['marzo', 'ma'],
        4: ['abril', 'ab'],
        5: ['mayo', 'my'],
        6: ['junio', 'jn'],
        7: ['julio', 'jl'],
        8: ['agosto', 'ag'],
        9: ['setiembre', 'se'],
        10: ['octubre', 'oc'],
        11: ['noviembre', 'no'],
        12: ['diciembre', 'di']
    }

    try:
        return meses_inverso[num_mes][cod_mes]
    except (KeyError, IndexError):
        return None

def get_name_by_cod(codigo):
    """
    :param codigo: Código único que indica si pertenece a Banca Múltiple, Empresas financieras, CMAC, CRAC, etcd
    :return: El nombre respectivo a dónde pertenece el código
    """

    # Diccionario simplificado para mapear los códigos a sus equivalentes
    codigos_equivalentes_simplificado = {
        'Banca Múltiple': ['B-2201', 'B-2362', 'B-2358'],  # 1
        'Empresas Financieras': ['B-3101', 'B-3257', 'B-3241'],  # 2
        'Cajas Municipales': ['C-1101', 'C-1242', 'C-1234', 'C-1257'],  # 3
        'Cajas Rurales': ['C-2101', 'C-2247', 'C-2234'],  # 4
        'Empresas de Créditos': ['C4103', 'C-4234', 'C-4228']  # 5
    }

    for key, value in codigos_equivalentes_simplificado.items():
        if codigo in value:
            return key
    return None


def limpiar_texto(texto):
    texto = texto.replace('*', '').replace(',', '').strip()
    return re.sub(r' +', ' ', texto)