"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd  # type: ignore

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

def letter_sum(dataframe):
    sum_letter = dataframe.groupby("c1")['c2'].sum()

    return sum_letter

def pregunta_07():
    """
    Calcule la suma de la `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: c2, dtype: int64
    """
    dataframe = load_input('files/input')
    dataframe = letter_sum(dataframe)

    return dataframe
print(pregunta_07())