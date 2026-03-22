# 🚗 Análisis Exploratorio de Vehículos (USA)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://analisis-vehiculos-alexis-dehesa.onrender.com)

### 📊 Descripción del Proyecto
Esta plataforma interactiva de análisis de datos permite explorar un conjunto de datos masivo de anuncios de venta de coches en EE.UU. El objetivo es identificar patrones de mercado, distribuciones de kilometraje y la depreciación de los vehículos frente a su precio de venta.

Desarrollada como parte de mi formación en **Data Analytics**, la aplicación utiliza herramientas de visualización dinámica para transformar datos crudos en información accionable.

---

### 🚀 Funcionalidades Principales
* **Visualización Dinámica:** Generación de histogramas interactivos para analizar la distribución del odómetro (kilometraje).
* **Análisis de Correlación:** Gráficos de dispersión para entender la relación directa entre el kilometraje y el precio de venta.
* **Interfaz Intuitiva:** Implementación de casillas de verificación (checkboxes) que permiten al usuario controlar qué análisis desea visualizar en tiempo real.
* **Análisis de Modelos:** Identificación de los 10 modelos de vehículos más frecuentes en el mercado.

---

### 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.9
* **Librerías de Datos:** Pandas
* **Visualización:** Plotly Express
* **Framework Web:** Streamlit
* **Despliegue:** Render (Cloud Hosting)
* **Entorno:** Virtualenv / Git

---

### 📁 Estructura del Repositorio
* `app.py`: Archivo principal de la aplicación Streamlit.
* `notebooks/EDA.ipynb`: Análisis exploratorio profundo, limpieza de datos y tratamiento de valores nulos.
* `vehicles_us.csv`: Conjunto de datos original.
* `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.

---

### ⚡ Cómo ejecutar localmente
1. Clonar el repositorio: `git clone https://github.com/Alexisboop13/analisis-vehiculos-tripleten.git`
2. Crear un entorno virtual: `python -m venv vehicles_env`
3. Instalar dependencias: `pip install -r requirements.txt`
4. Ejecutar la app: `streamlit run app.py`

---

**Desarrollado por Alexis Dehesa Guzmán** *Impulsando decisiones basadas en datos.*