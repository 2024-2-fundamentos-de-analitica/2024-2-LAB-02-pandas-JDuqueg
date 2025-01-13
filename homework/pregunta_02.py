"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    dataframe = pd.read_csv(
            'files/input/tbl0.tsv',
            header=0,
            delimiter="\t",
            names=None,
            index_col=None,
        )
        
    return dataframe

def num_rows(dataframe):
    return dataframe.shape[1]


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    dataframe = load_input('files/input')
    dataframe = num_rows(dataframe)

    return dataframe
print(pregunta_02())