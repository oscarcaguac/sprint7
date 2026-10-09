import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos.
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación.
st.header('Análisis de anuncios de venta de vehículos')

st.write(
    'Explora el recorrido y el precio de los vehículos '
    'mediante gráficos interactivos.'
)

# Botón para construir el histograma.
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Distribución del recorrido registrado de los vehículos.')

    fig_hist = px.histogram(
        car_data,
        x='odometer',
        nbins=50,
        title='Distribución del recorrido de los vehículos',
        labels={'odometer': 'Recorrido registrado (millas)'}
    )

    fig_hist.update_layout(yaxis_title='Cantidad de anuncios')

    st.plotly_chart(fig_hist)

# Botón para construir el gráfico de dispersión.
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Relación entre el recorrido del vehículo y su precio.')

    fig_scatter = px.scatter(
        car_data,
        x='odometer',
        y='price',
        opacity=0.5,
        title='Precio frente al recorrido del vehículo',
        labels={
            'odometer': 'Recorrido registrado (millas)',
            'price': 'Precio (USD)'
        }
    )

    st.plotly_chart(fig_scatter)
