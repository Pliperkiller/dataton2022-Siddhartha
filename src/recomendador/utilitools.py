import os
import pandas as pd
import numpy as np
import openpyxl


def crear_paths():
    bandera = 0
    local_path = os.path.abspath(os.getcwd())
    
    for file in os.listdir(local_path):
        if 'path' in file:
            bandera = 1
    
    
    if bandera == 0:
        os.chdir('../')
        parent_path = os.path.abspath(os.getcwd())
        os.chdir(local_path)
        paths = []
        folders = []
        for file in os.listdir(parent_path):
                    file_path = os.path.join(parent_path,file)
                    paths.append(file_path)
                    folders.append(file)
    
        ruta = dict(zip(folders, paths))
        ruta_df = pd.DataFrame([ruta])
        ruta_df.to_excel('path.xlsx', index=False)

    elif bandera == 1: pass        

paths = os.path.abspath(os.getcwd())

def leer_paths(key, paths=paths):
    
    crear_paths()
    
    for file in os.listdir(paths):
            file_path = os.path.join(paths,file)

            if 'path.xlsx' in file_path:
                df = pd.read_excel(file_path)
    
    return df[key][0]

def change_dict_keys(df,dict_path,filename = 'read_keys.xlsx'):

    diccionario = pd.read_excel(os.path.join(dict_path,filename), skiprows=0)
    diccionario.dropna(subset=['original keys', 'new keys'], inplace=True)
    
    old_keys = list(df['original keys'])
    new_keys = list(df['new keys'])

    translator = dict(zip(old_keys, new_keys))
    
    df.replace(translator, inplace= True)

    return df


