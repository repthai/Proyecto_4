import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Proyecto 4: Dashboard autos")

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.checkbox('Construir histograma') # crear un botón

#Boton para realizar el histograma
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

#Boton para realizar el grafico de dispersión
disp_button = st.button('Construir grafica de dispersión') # crear un botón

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # crear el graf de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
