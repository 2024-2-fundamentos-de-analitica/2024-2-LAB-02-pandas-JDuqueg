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
            'files/input/tbl1.tsv',
            header=0,
            delimiter="\t",
            names=None,
            index_col=None,
        )
    return dataframe

def column_match(dataframe):
     dataframe['c4'] = dataframe.groupby('c0')['c4'].transform(lambda x: ','.join(x))

     return dataframe

def filter(dataframe):
    return dataframe.drop_duplicates(['c0','c4'],keep='first')

def sort_column(dataframe):
    dataframe['c4'] = dataframe['c4'].apply(lambda x: ','.join(sorted(x.split(','))))

    return dataframe.reset_index(drop=True)

def pregunta_11():
    
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    dataframe = load_input('files\input')
    dataframe = column_match(dataframe)
    dataframe = filter(dataframe)
    dataframe = sort_column(dataframe)

    return dataframe
print(pregunta_11())