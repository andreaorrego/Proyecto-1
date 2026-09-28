import pandas as pd
from sodapy import Socrata

def limpiar_texto(serie: pd.Series) -> pd.Series:
    return (
        serie.astype(str)
        .str.strip()
        .str.lower()
        .str.replace("á", "a", regex=False)
        .str.replace("é", "e", regex=False)
        .str.replace("í", "i", regex=False)
        .str.replace("ó", "o", regex=False)
        .str.replace("ú", "u", regex=False)
        .str.replace("ñ", "n", regex=False)
    )

client = Socrata("www.datos.gov.co", None)

def cargar_datos(limite_registros, nombre_departamento):
    depto = nombre_departamento.strip().upper()
    
    results = client.get(
        "gt2j-8ykr",
        limit=limite_registros,
        where=f"departamento_nom = '{depto}'"
    )

    if not results:
        print("No se encontraron registros para ese departamento.")
        return pd.DataFrame()

    df = pd.DataFrame.from_records(results)

    columnas_necesarias = [
        "ciudad_municipio_nom",
        "departamento_nom",
        "edad",
        "fuente_tipo_contagio",
        "estado",
        "pais_viajo_1_nom"
    ]

    for col in columnas_necesarias:
        if col not in df.columns:
            df[col] = None

    renombrar = {
        "departamento_nom": "nombre_departamento",
        "ciudad_municipio_nom": "nombre_municipio",
        "fuente_tipo_contagio": "tipo_contagio",
        "pais_viajo_1_nom": "pais_procedencia"
    }

    df_limpio = df[columnas_necesarias].rename(columns=renombrar)
    df_limpio.columns = df_limpio.columns.str.strip()

    return df_limpio