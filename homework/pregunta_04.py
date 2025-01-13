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

def letter_mean(dataframe):
    dataframe.pop('c0')
    dataframe.pop('c3')
    mean_letter = dataframe.groupby("c1")['c2'].mean()

    return mean_letter

def pregunta_04():
    """
    Calcule el promedio de `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: c2, dtype: float64
    """
    dataframe = load_input('files/input')
    dataframe = letter_mean(dataframe)

    return dataframe
print(pregunta_04())