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
    dataframe1 =pd.read_csv(
            files[0],
            header=0,
            delimiter="\t",
            names=None,
            index_col=None,
        )
    dataframe2=pd.read_csv(
            files[2],
            header=0,
            delimiter="\t",
            names=None,
            index_col=None,
        )
    
    

    dataframe = pd.merge(dataframe1,dataframe2, on='c0',how='left')

    dataframe.pop('c2')
    dataframe.pop('c5a')
    dataframe.pop('c3')

    return dataframe

def sum_columns(df):
    return df.groupby('c1')['c5b'].sum()

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    df = load_input('files\input')
    df = sum_columns(df)

    return df
print(pregunta_13())
