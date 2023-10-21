import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from st_btn_select import st_btn_select

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Ventas Mundiales Video Juegos')

DATE_COLUMN = 'date/time'
DATA_URL = ('dataclean/ventas_clean.csv')

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

col1, col2 = st.columns([1, 4])


data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache)")

var=data['Año'].unique().tolist()
var = [None] + var

with col1:    
    option = st.selectbox(
        'Filtro Por Año',
        (var)
        )

        
    if st.button("Limpiar Filtros"):
        option =None    
with col2:
    
    if option:
        filtered_data = data[data['Año'] == option]
    else:
        filtered_data =data

    st.write('Ventas Por Región')
    comp_genre = filtered_data[['Genero', 'Ventas NA', 'Ventas EU', 'Ventas JP', 'Ventas Otros']]
    comp_map = comp_genre.groupby(by=['Genero']).sum()
    plt.figure(figsize=(10, 5))
    sns.set(font_scale=1)
    sns.heatmap(comp_map, annot=True, fmt='.1f')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    st.pyplot()
    
    st.write('Genero Mayores $Ventas')
    data_Genero = filtered_data.groupby(by=['Genero'])['Ventas Global'].sum()
    data_Genero = data_Genero.reset_index()
    data_Genero = data_Genero.sort_values(by=['Ventas Global'], ascending=False)
    plt.figure(figsize=(10, 5));
    sns.barplot(x="Genero", y="Ventas Global", data=data_Genero);
    plt.xticks(rotation=90);    
    st.pyplot()

    st.write('Ventas por año')
    data_Año = filtered_data.groupby(by=['Año'])['Ventas Global'].sum()
    data_Año = data_Año.reset_index()
    plt.figure(figsize=(10, 5));
    sns.barplot(x="Año", y="Ventas Global", data=data_Año);
    plt.xticks(rotation=90);
    st.pyplot()

    if st.checkbox('Mostrar Contenido Información'):
        st.subheader('Game Sales')                                  
        st.write(filtered_data)

