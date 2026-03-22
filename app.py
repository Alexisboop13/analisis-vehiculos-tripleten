import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de anuncios de venta de coches')

# Casilla para histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos')
    fig = px.histogram(car_data, x="odometer")
    # Cambiamos use_container_width por width='stretch'
    st.plotly_chart(fig, width='stretch')

# Casilla para dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Relación entre Kilometraje y Precio')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # Cambiamos use_container_width por width='stretch'
    st.plotly_chart(fig_scatter, width='stretch')
