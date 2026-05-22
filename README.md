# 🌲 Árbol de Decisión ID3 con el Dataset Iris

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.2+-orange.svg)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-2.0+-darkblue.svg)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este proyecto implementa y documenta un ciclo de vida completo de Machine Learning (ML) aplicado a la clasificación de especies de flores utilizando el dataset **Iris** y un clasificador de **Árbol de Decisión ID3** (basado en la métrica de Entropía y Ganancia de Información). 

El proyecto incluye una aplicación web interactiva desarrollada en **Streamlit** para realizar predicciones en tiempo real y explorar el dataset, además de material de apoyo en formato HTML y Word (.docx) para fines educativos y de presentación de proyectos de Inteligencia Artificial en el programa **Talento Tech**.

---

## 📂 Estructura del Proyecto

*   [app.py](file:///c:/Users/Feibert/OneDrive/Documents/AGENTE/Arboles/app.py): Aplicación interactiva de Streamlit para el usuario final.
*   [requirements.txt](file:///c:/Users/Feibert/OneDrive/Documents/AGENTE/Arboles/requirements.txt): Listado de paquetes de Python necesarios para correr la aplicación.
*   [index.html](file:///c:/Users/Feibert/OneDrive/Documents/AGENTE/Arboles/index.html): Documentación de diseño premium en formato web con el desglose del proyecto y visualizaciones.
*   [tutorial.md](file:///c:/Users/Feibert/OneDrive/Documents/AGENTE/Arboles/tutorial.md): Tutorial paso a paso que describe todo el desarrollo técnico del pipeline.
*   `image/`: Directorio que almacena los diagramas y gráficos generados del ciclo de vida de ML:
    *   [Infografia.png](file:///c:/Users/Feibert/OneDrive/Documents/AGENTE/Arboles/image/Infografia.png): Flujo del ciclo de vida del proyecto IA.
    *   [Arbol.png](file:///c:/Users/Feibert/OneDrive/Documents/AGENTE/Arboles/image/Arbol.png): Grafo visual de las decisiones del clasificador ID3.
    *   [Matriz Confusión.png](file:///c:/Users/Feibert/OneDrive/Documents/AGENTE/Arboles/image/Matriz%20Confusi%C3%B3n.png): Matriz de errores cuantitativos.
    *   [Comparación Valoras Predichos.png](file:///c:/Users/Feibert/OneDrive/Documents/AGENTE/Arboles/image/Comparaci%C3%B3n%20Valoras%20Predichos.png): Contraste de valores reales y predichos.
*   `Proyecto/`: Carpeta con los materiales del entregable:
    *   [Material_1_Proyecto_IA_Talento_Tech.docx](file:///c:/Users/Feibert/OneDrive/Documents/AGENTE/Arboles/Proyecto/Material_1_Proyecto_IA_Talento_Tech.docx): Documento oficial de la actividad completamente actualizado con la teoría del árbol ID3 y las imágenes cargadas correspondientes.

---

## 🔄 Fases del Ciclo de Vida del Machine Learning (ML)

El desarrollo del modelo se alinea rigurosamente con las siguientes etapas:

1.  **Ingesta de Datos (ETL - Extract):** Carga del dataset Iris desde un repositorio abierto de OpenML.
2.  **Preparación y Limpieza (ETL - Transform & Load):** Validación física de los atributos (`sepallength`, `sepalwidth`, `petallength`, `petalwidth`), separación de la variable predictiva `class` y partición estratificada de entrenamiento (80%) y prueba (20%).
3.  **Análisis Exploratorio (EDA):** Visualización interactiva y estadística de los datos morfológicos para comprender los límites de las especies.
4.  **Modelado (ID3):** Ajuste de un clasificador de árbol de decisión utilizando el criterio de **Entropía** para medir la ganancia de información en cada ramificación.
5.  **Evaluación:** Obtención de métricas cuantitativas sobre el conjunto de test:
    *   **Exactitud (Accuracy):** 96.67%
    *   **Métricas detalladas:** Precisión de 1.00 para *setosa* y *versicolor*, con un recall de 0.92 para *versicolor* debido a solapamiento físico.
6.  **Despliegue e Interfaz:** Despliegue en producción mediante la aplicación interactiva de Streamlit, lista para ingresar medidas y realizar inferencias de especie en tiempo real.

---

## 🛠️ Instrucciones de Configuración y Ejecución

Sigue estos sencillos pasos para levantar la aplicación en tu entorno local:

### 1. Clonar o acceder a la carpeta del proyecto
Asegúrate de que estás en la terminal posicionado en el directorio raíz del proyecto:
```bash
cd c:/Users/Feibert/OneDrive/Documents/AGENTE/Arboles
```

### 2. Instalar dependencias
Instala los paquetes necesarios utilizando el archivo de requerimientos:
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la Aplicación Streamlit
Inicia el servidor local de desarrollo:
```bash
streamlit run app.py
```
La aplicación se abrirá automáticamente en tu navegador web predeterminado (por defecto en `http://localhost:8501`).

### 4. Visualizar Documentación HTML
Puedes abrir el archivo [index.html](file:///c:/Users/Feibert/OneDrive/Documents/AGENTE/Arboles/index.html) directamente en cualquier navegador web haciendo doble clic sobre el archivo o arrastrándolo a una pestaña activa.

---

## 📝 Autoría y Créditos
*   **Proyecto:** Árbol de Decisión ID3 - Dataset Iris
*   **Marco Académico:** Programa de IA / Aprendizaje Inteligente, Talento Tech.
*   **Desarrollador:** Feibert Alirio Guzmán Pérez, 2026.
