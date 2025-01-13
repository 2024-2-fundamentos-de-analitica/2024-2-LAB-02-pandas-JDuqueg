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
            'files/input/tbl2.tsv',
            header=0,
            delimiter="\t",
            names=None,
            index_col=None,
        )

    return dataframe

def merge_column(dataframe):
    dataframe['c5'] = dataframe['c5a'].map(str).str.cat(dataframe['c5b'].map(str), sep=':')
    dataframe.pop('c5a')
    dataframe.pop('c5b')

    return dataframe

def match_column(dataframe):
    dataframe['c5'] = dataframe.groupby('c0')['c5'].transform(lambda x: ','.join(sorted(map(str,x))))

    return dataframe.drop_duplicates(['c0','c5'],keep='first')

       
def pregunta_12():
    
    """
    Construya una tabla que contenga `c0` y una lista separada por ','
    de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
    tabla `tbl2.tsv`.

    Rta/
         c0                                   c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    dataframe = load_input('files\input')
    dataframe = merge_column(dataframe)
    dataframe = match_column(dataframe)

    return dataframe
print(pregunta_12())