"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import glob
import pandas as pd  # type: ignore

def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    #
    files = glob.glob(f"{input_directory}/*")
    dataframes = [
        pd.read_csv(
            files[0],
            header=0,
            delimiter="\t",
            names=None,
            index_col=None,
        )
       
    ]

    dataframe = pd.concat(dataframes, ignore_index=True)

    return dataframe

def letter_count(dataframe, columna):
    return dataframe[columna].value_counts().sort_index()

def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """
    dataframe = load_input('files/input')
    dataframe = letter_count(dataframe, 'c1')

    return dataframe
pregunta_03()
