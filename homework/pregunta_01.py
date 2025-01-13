"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd
import glob

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

def num_rows(dataframe):
    return dataframe.shape[0]

def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    dataframe = load_input('files\input')
    dataframe = num_rows(dataframe)

    return dataframe
pregunta_01()