import pandas as pd
import streamlit as st
import codecs


#Config. de pagina
st.title('Netflix App')
name_link ='movies.csv'

st.text('Yareli Sugey Bravo Morales - ZS20006773')


@st.cache

def load_data(nrows):
    name_link = codecs.open("movies.csv",'r','latin1')
    data = pd.read_csv(name_link, nrows=nrows)
    return data


#Contenido del sidebar
sidebar = st.sidebar
st.sidebar.image("https://raw.githubusercontent.com/YareliB07/streamlit/master/credencial.jpeg")
sidebar.title("Filtro")

agree=sidebar.checkbox("¿Desea ver los films recuperados?")
if agree:
    data_load_state = st.text('cargando')
    data = load_data(500)
    data_load_state.text('netflix app!! (using st.cache)')
    st.dataframe(data)

sidebar.markdown("##")

title=sidebar.text_input("Ingresa el titulo de un pelicula:")
agree=sidebar.button