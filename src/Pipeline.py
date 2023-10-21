# PIPELINE

import pandas as pd

### 1. Cargar la data 
df = pd.read_excel('data/Ventas_Videojuegos.xlsx')


### 2. Transformación de variables. La variable Año pasa de tipo Entero a variable categorica
df['Año'] = df['Año'].astype(str)

### 3. Eliminar la variable 'Ventas Global'
#df = df.drop('Ventas Global', axis=1)

### 4. Se reemplazan valores nulos de la variable Editorial por la Moda
columnas_categoricas = df.select_dtypes(include=['object']).columns

for columna in columnas_categoricas:
    moda = df[columna].mode()[0]  # Encuentra la moda de la columna actual
    df[columna].fillna(moda, inplace=True)

### 5. Se reemplazan valores nulos de la variables numericas por la media
columnas_numericas = df.select_dtypes(include=['int', 'float']).columns

for columna in columnas_numericas:
    if df[columna].isnull().sum() > 0:
        media = df[columna].mean()  # Puedes cambiar a df[columna].mean() si prefieres la media
        df[columna].fillna(media, inplace=True)

### 6. Guardamos el archivo
df.to_csv('dataclean/ventas_clean.csv',index=False)



