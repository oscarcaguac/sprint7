# Análisis de anuncios de venta de vehículos

Proyecto del Sprint 7 del bootcamp de ciencia de datos. Consiste en una
aplicación web desarrollada con Streamlit para explorar un conjunto de
datos de anuncios de venta de vehículos en Estados Unidos.

## Funcionalidades

- Construir un histograma interactivo del recorrido registrado de los vehículos.
- Construir un gráfico de dispersión interactivo que relaciona el recorrido
  con el precio de venta.

Los gráficos permiten explorar la distribución del recorrido y su relación
con los precios de los vehículos anunciados.

## Herramientas utilizadas

- Python
- Pandas
- Plotly Express
- Streamlit

## Archivos del proyecto

- `app.py`: código de la aplicación web.
- `vehicles_us.csv`: conjunto de datos utilizado.
- `notebooks/EDA.ipynb`: análisis exploratorio y pruebas de visualización.
- `requirements.txt`: dependencias de la aplicación.
- `.gitignore`: archivos y carpetas excluidos del control de versiones.

## Ejecución local

Desde la carpeta principal del repositorio y con un entorno de Python
activo, instala las dependencias:

```bash
python -m pip install -r requirements.txt
```

Inicia la aplicación:

```bash
streamlit run app.py
```

Abre en el navegador la dirección local que indique la terminal.

##Link de render para ver la página web
https://sprint7-7m3n.onrender.com 
