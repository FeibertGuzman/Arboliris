# 📝 Tutorial Paso a Paso: Árbol de Decisión ID3 con Dataset Iris

Este tutorial describe el proceso detallado paso a paso para construir, evaluar y desplegar un clasificador de Árbol de Decisión ID3 utilizando Python, scikit-learn y Streamlit.

---

## 🧭 Tabla de Contenidos
1. [Ingesta e Instalación de Dependencias](#1-ingesta-e-instalación-de-dependencias)
2. [Carga del Dataset (Fase ETL: Extract)](#2-carga-del-dataset-fase-etl-extract)
3. [Preparación de Datos (Fase ETL: Transform & Load)](#3-preparación-de-datos-fase-etl-transform--load)
4. [Teoría y Matemáticas del Algoritmo ID3](#4-teoría-y-matemáticas-del-algoritmo-id3)
5. [Entrenamiento del Modelo (Fase de Modelado)](#5-entrenamiento-del-modelo-fase-de-modelado)
6. [Evaluación Cuantitativa y Cualitativa](#6-evaluación-cuantitativa-y-cualitativa)
7. [Despliegue Interactivo con Streamlit](#7-despliegue-interactivo-con-streamlit)

---

## 1. Ingesta e Instalación de Dependencias
Para comenzar, definimos los paquetes necesarios en un archivo `requirements.txt` e instalamos el entorno virtual.

### Comando de Instalación:
```bash
pip install -r requirements.txt
```
Las librerías principales utilizadas son:
*   `pandas`: Para la carga y manipulación tabular.
*   `numpy`: Para operaciones vectoriales.
*   `scikit-learn`: Para la división de datos, modelado de árbol y cálculo de métricas.
*   `streamlit`: Para crear la aplicación web interactiva.
*   `python-docx`: Para la automatización del reporte físico de la actividad.

---

## 2. Carga del Dataset (Fase ETL: Extract)
El dataset **Iris** se extrae de manera dinámica de una fuente abierta en formato CSV.

```python
import pandas as pd

# URL del dataset en OpenML
url = "https://www.openml.org/data/get_csv/61/dataset_61_iris.arff"

# Carga de datos
dt = pd.read_csv(url)

# Verificar dimensiones
print(f"Dimensiones del DataFrame: {dt.shape}")
# Salida esperada: (150, 5)
```

---

## 3. Preparación de Datos (Fase ETL: Transform & Load)
La etapa de transformación implica separar los atributos independientes de la variable objetivo y partir el dataset en entrenamiento y prueba.

```python
from sklearn.model_selection import train_test_split

# Separar características (X) y variable objetivo (y)
X = dt.drop('class', axis=1)  # Características: sepallength, sepalwidth, petallength, petalwidth
y = dt['class']               # Target: Iris-setosa, Iris-versicolor, Iris-virginica

# Partición 80/20 estratificada (para mantener balance de clases)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=1, 
    stratify=y  # Asegura una división proporcional de especies
)
```

---

## 4. Teoría y Matemáticas del Algoritmo ID3
El clasificador de scikit-learn `DecisionTreeClassifier` permite emular el comportamiento del algoritmo original **ID3** configurando el parámetro `criterion='entropy'`.

### Entropía ($H(S)$):
Mide el grado de desorden e incertidumbre en el nodo. Su fórmula matemática es:
$$H(S) = - \sum_{i=1}^{C} p_i \log_2(p_i)$$
Donde $p_i$ es la probabilidad de que una instancia pertenezca a la especie $i$ dentro de ese nodo.

### Ganancia de Información ($IG$):
Es el criterio de selección del atributo divisor:
$$IG(S, A) = H(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} H(S_v)$$
El algoritmo calcula recursivamente la $IG$ para cada variable y selecciona la característica que proporcione la mayor reducción de entropía.

---

## 5. Entrenamiento del Modelo (Fase de Modelado)
Entrenamos la estructura del árbol alimentando el algoritmo con los datos de entrenamiento preparados.

```python
from sklearn.tree import DecisionTreeClassifier

# Crear instancia del modelo con criterio de entropía (ID3)
algorithm = DecisionTreeClassifier(criterion='entropy', random_state=1)

# Ajustar / entrenar el clasificador
algorithm.fit(X_train, y_train)
```

---

## 6. Evaluación Cuantitativa y Cualitativa
Evaluamos el modelo pasándole datos que no ha visto durante el entrenamiento (`X_test`) y calculamos las métricas clásicas.

```python
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Realizar predicciones
y_pred = algorithm.predict(X_test)

# 1. Exactitud (Accuracy)
acc = accuracy_score(y_test, y_pred)
print(f"Exactitud del modelo: {acc * 100:.2f}%")
# Salida esperada: 96.67%

# 2. Reporte detallado por clase
print(classification_report(y_test, y_pred))

# 3. Matriz de confusión
print("Matriz de Confusión:")
print(confusion_matrix(y_test, y_pred))
```

---

## 7. Despliegue Interactivo con Streamlit
Finalmente, para el despliegue del modelo, empaquetamos el entrenamiento y construimos controles interactivos tipo "sliders" para recibir las dimensiones florales del usuario y predecir en tiempo real.

### Estructura de Inferencias en `app.py`:
```python
# Controles de interfaz en Streamlit
sepallength = st.slider("Largo del Sépalo:", 4.0, 8.0, 5.1)
sepalwidth = st.slider("Ancho del Sépalo:", 2.0, 4.5, 3.5)
petallength = st.slider("Largo del Pétalo:", 1.0, 7.0, 1.4)
petalwidth = st.slider("Ancho del Pétalo:", 0.1, 2.5, 0.2)

# Crear DataFrame para el modelo
input_data = pd.DataFrame([{
    'sepallength': sepallength,
    'sepalwidth': sepalwidth,
    'petallength': petallength,
    'petalwidth': petalwidth
}])

# Realizar inferencia
pred = model.predict(input_data)[0]
st.success(f"La especie clasificada es: {pred}")
```
Para levantar la interfaz, ejecuta en la consola:
```bash
streamlit run app.py
```
El navegador abrirá de inmediato la aplicación interactiva donde se pueden visualizar las métricas y simular predicciones.
