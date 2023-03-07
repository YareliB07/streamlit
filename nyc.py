import streamlit as st
import pandas as pd
import numpy as np

st.title('Cicle Rides in NYC')
st.text('Yareli Sugey Bravo Morales - zS20006773 - zS20006784@estudiantes.uv.mx')

DATE_COLUMN = 'started_at'
DATA_URL = ('citibike-tripdata.csv')

@st.cache_resource
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading cicle nyc data...')
data = load_data(1000)
data_load_state.text("Done! (using st.cache)")

sidebar = st.sidebar
st.sidebar.image("https://raw.githubusercontent.com/YareliB07/streamlit/master/credencial.jpeg")

if st.sidebar.checkbox('Mostrar data'):
    st.subheader('Raw data')
    st.write(data)

if st.sidebar.checkbox('Recorridos por hora'):
    st.subheader('Numero de recorridos por hora')

    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)


hour_to_filter = st.sidebar.slider('Hora', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Mapa de recorridos iniciados a las %s:00' % hour_to_filter)
st.map(filtered_data)