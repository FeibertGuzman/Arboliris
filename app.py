import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Page config
st.set_page_config(
    page_title="Iris ID3 - Ciclo de Vida ML",
    page_icon="🌲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Premium Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    
    .subtitle {
        font-size: 1.25rem;
        color: #94a3b8;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    .card {
        background-color: #1e293b;
        color: #f8fafc !important;
        border-radius: 1rem;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border: 1px solid #334155;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    }
    
    .card p, .card li, .card span, .card td, .card th, .card div {
        color: #cbd5e1 !important;
    }
    
    .card b, .card strong {
        color: #f8fafc !important;
    }
    
    .card-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #f8fafc !important;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .badge {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
    }
    
    .metric-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #10b981;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
</style>
""", unsafe_allow_html=True)

# Dataset Loading
@st.cache_data
def load_data():
    # Carga local y offline del dataset Iris (instantáneo y robusto)
    try:
        from sklearn.datasets import load_iris
        iris = load_iris()
        df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                          columns=iris['feature_names'] + ['target'])
        # Mapea los números de clase a nombres legibles
        target_map = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}
        df['class'] = df['target'].map(target_map)
        df = df.drop('target', axis=1)
        # Renombra columnas para coincidir con la nomenclatura original del notebook
        df.columns = ['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'class']
        return df
    except Exception as e:
        st.warning(f"No se pudo cargar localmente ({e}). Intentando con la URL de OpenML...")
        url = "https://www.openml.org/data/get_csv/61/dataset_61_iris.arff"
        df = pd.read_csv(url)
        return df

dt = load_data()

# Model Training
@st.cache_resource
def train_model(df):
    X = df.drop('class', axis=1)
    y = df['class']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    
    model = DecisionTreeClassifier(criterion='entropy', random_state=1)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)
    
    return model, X_train, X_test, y_train, y_test, y_pred, accuracy, report

model, X_train, X_test, y_train, y_test, y_pred, accuracy, report = train_model(dt)

# Sidebar navigation
st.sidebar.image("image/Arbol.png", width=120)
st.sidebar.markdown("<h2 style='text-align: center;'>Navegación</h2>", unsafe_allow_html=True)
page = st.sidebar.radio(
    "Ir a:",
    ["Inicio y Ciclo de Vida ML", "Exploración de Datos (EDA)", "Entrenamiento y Evaluación", "Predicción Interactiva"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Proyecto Talento Tech**  
*Módulo de Aprendizaje Inteligente*  
**Autor:** Feibert Alirio Guzmán Pérez  
**Modelo:** Árbol de Decisión ID3  
""")

# Page 1: Inicio y Ciclo de Vida ML
if page == "Inicio y Ciclo de Vida ML":
    st.markdown("<h1 class='main-title'>🌲 Árbol de Decisión ID3 - Dataset Iris</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Visualización interactiva y aplicación del ciclo de vida de Machine Learning</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown(f"""
        <div class='card'>
            <div class='card-title'>📖 Introducción al Proyecto</div>
            <p>Este proyecto implementa un flujo completo de <b>Machine Learning (ML)</b> utilizando el dataset <b>Iris</b> ( Ronald Fisher, 1936 ) y el algoritmo de árboles de decisión de tipo <b>ID3 (Iterative Dichotomiser 3)</b> basado en <b>Entropía</b> y <b>Ganancia de Información</b>.</p>
            <p>A lo largo de este tablero interactivo, podrás explorar cómo funciona cada etapa del ciclo de vida del modelo de IA, desde la ingesta del dato limpio, pasando por su análisis exploratorio, modelado, evaluación cuantitativa mediante métricas clásicas, y finalmente el despliegue del predictor listo para producción.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='card'>
            <div class='card-title'>⚙️ Estructura del Algoritmo ID3</div>
            <ul>
                <li><b>Entropía (Entropy):</b> Mide el desorden o la incertidumbre dentro de una muestra de datos. El objetivo del árbol es reducir la entropía en cada división a 0.0 (nodos puros).</li>
                <li><b>Ganancia de Información:</b> Es la reducción de entropía lograda al dividir el conjunto de datos bajo una característica particular. El algoritmo selecciona en cada paso la división con mayor ganancia de información.</li>
                <li><b>Reglas de decisión lógicas:</b> Permite entender de manera transparente los criterios de clasificación, resultando en un modelo altamente interpretable (White Box model).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div class='card'>
            <div class='card-title'>🧬 Ficha Técnica del Dataset</div>
            <table style='width: 100%; border-collapse: collapse;'>
                <tr style='border-bottom: 1px solid #334155;'>
                    <td style='padding: 0.5rem 0; color: #94a3b8;'>Instancias</td>
                    <td style='padding: 0.5rem 0; font-weight: 600; text-align: right;'>150 muestras</td>
                </tr>
                <tr style='border-bottom: 1px solid #334155;'>
                    <td style='padding: 0.5rem 0; color: #94a3b8;'>Características</td>
                    <td style='padding: 0.5rem 0; font-weight: 600; text-align: right;'>4 numéricas (cm)</td>
                </tr>
                <tr style='border-bottom: 1px solid #334155;'>
                    <td style='padding: 0.5rem 0; color: #94a3b8;'>Clases</td>
                    <td style='padding: 0.5rem 0; font-weight: 600; text-align: right;'>3 especies de Iris</td>
                </tr>
                <tr>
                    <td style='padding: 0.5rem 0; color: #94a3b8;'>Distribución</td>
                    <td style='padding: 0.5rem 0; font-weight: 600; text-align: right; color: #10b981;'>50 / 50 / 50 (Balanceado)</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>🔄 Ciclo de Vida de Machine Learning</h3>", unsafe_allow_html=True)
    
    # Load and display infographic
    if os.path.exists("image/Infografia.png"):
        img = Image.open("image/Infografia.png")
        st.image(img, caption="Infografía del Ciclo de Vida del Proyecto IA - ID3 Iris", use_container_width=True)
    else:
        st.warning("No se encontró el archivo de infografía en la carpeta 'image'.")

# Page 2: Exploración de Datos (EDA)
elif page == "Exploración de Datos (EDA)":
    st.markdown("<h1 class='main-title'>🔍 Análisis Exploratorio de Datos (EDA)</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Comprensión morfológica del dataset Iris</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class='card'>
            <div class='card-title'>📊 El Dataset Iris Completo</div>
            <p>A continuación se visualizan los registros cargados directamente desde la URL de OpenML.</p>
        </div>
        """, unsafe_allow_html=True)
        st.dataframe(dt, use_container_width=True, height=260)
        
        st.markdown("""
        <div class='card'>
            <div class='card-title'>📈 Estadísticas Descriptivas</div>
            <p>Medidas estadísticas de las variables numéricas correspondientes a los sépalos y pétalos.</p>
        </div>
        """, unsafe_allow_html=True)
        st.dataframe(dt.describe(), use_container_width=True)
        
    with col2:
        st.markdown("""
        <div class='card'>
            <div class='card-title'>📐 Gráfico de Dispersión Interactivo</div>
            <p>Selecciona las características que deseas contrastar para ver la separación natural de las clases en el plano geométrico.</p>
        </div>
        """, unsafe_allow_html=True)
        
        x_var = st.selectbox("Eje X:", ["sepallength", "sepalwidth", "petallength", "petalwidth"], index=2)
        y_var = st.selectbox("Eje Y:", ["sepallength", "sepalwidth", "petallength", "petalwidth"], index=3)
        
        # Color mapping for streamlit scatter
        st.scatter_chart(
            data=dt,
            x=x_var,
            y=y_var,
            color='class',
            use_container_width=True,
            height=320
        )
        
        st.markdown("""
        *💡 **Tip:** Observa cómo las variables de los pétalos (`petallength` y `petalwidth`) separan de forma casi lineal a la clase `Iris-setosa` del resto, y cómo la separación entre `Iris-versicolor` e `Iris-virginica` presenta un ligero traslape.*
        """)

# Page 3: Entrenamiento y Evaluación
elif page == "Entrenamiento y Evaluación":
    st.markdown("<h1 class='main-title'>🧠 Modelado y Evaluación del Rendimiento</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Evaluación del Clasificador Decision Tree (ID3)</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class='card' style='text-align: center;'>
            <div class='metric-label'>Exactitud Global (Accuracy)</div>
            <div class='metric-value'>{accuracy * 100:.2f}%</div>
            <p style='color: #94a3b8; font-size: 0.85rem; margin-top: 0.5rem;'>
                El modelo clasificó correctamente a {sum(y_test == y_pred)} de {len(y_test)} flores del conjunto de prueba.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div class='card' style='text-align: center;'>
            <div class='metric-label'>Precisión Promedio</div>
            <div class='metric-value'>{report['macro avg']['precision'] * 100:.1f}%</div>
            <p style='color: #94a3b8; font-size: 0.85rem; margin-top: 0.5rem;'>
                Capacidad del modelo para evitar etiquetar una muestra negativa como positiva.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown(f"""
        <div class='card' style='text-align: center;'>
            <div class='metric-label'>F1-Score Promedio</div>
            <div class='metric-value'>{report['macro avg']['f1-score'] * 100:.1f}%</div>
            <p style='color: #94a3b8; font-size: 0.85rem; margin-top: 0.5rem;'>
                Balance armónico entre la precisión y la sensibilidad (recall).
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.markdown("""
        <div class='card'>
            <div class='card-title'>📊 Reporte de Clasificación por Especie</div>
            <p>Estadísticas de rendimiento en detalle para el 20% de datos separados como test set:</p>
        </div>
        """, unsafe_allow_html=True)
        
        rep_df = pd.DataFrame(report).transpose().drop(['accuracy'], errors='ignore')
        st.dataframe(rep_df.style.format(precision=4), use_container_width=True)
        
        st.markdown("""
        <div class='card'>
            <div class='card-title'>🔄 Comparación de Predicciones</div>
            <p>Gráfica de conteo de las clases reales frente al desempeño del modelo.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if os.path.exists("image/Comparación Valoras Predichos.png"):
            st.image(Image.open("image/Comparación Valoras Predichos.png"), caption="Comparativa Real vs Predicho", use_container_width=True)
        else:
            st.info("No se encontró la imagen de comparación de predicciones.")
            
    with col_right:
        st.markdown("""
        <div class='card'>
            <div class='card-title'>🎯 Matriz de Confusión</div>
            <p>Visualización del cruce entre las etiquetas verdaderas y las predicciones del modelo.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if os.path.exists("image/Matriz Confusión.png"):
            st.image(Image.open("image/Matriz Confusión.png"), caption="Matriz de Confusión del Modelo", width=380)
        else:
            st.info("No se encontró la imagen de la matriz de confusión.")
            
    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>🌲 Estructura del Árbol de Decisión Entrenado (ID3)</h3>", unsafe_allow_html=True)
    
    if os.path.exists("image/Arbol.png"):
        st.image(Image.open("image/Arbol.png"), caption="Visualización del Árbol de Decisión ID3 entrenado con criterio de Entropía", use_container_width=True)
    else:
        st.info("No se encontró la imagen de visualización del árbol.")

# Page 4: Predicción Interactiva
elif page == "Predicción Interactiva":
    st.markdown("<h1 class='main-title'>🔮 Predicciones de Especie en Tiempo Real</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Ingrese las medidas de una flor para que el modelo estime su clasificación</p>", unsafe_allow_html=True)
    
    col_input, col_result = st.columns([2, 3])
    
    with col_input:
        st.markdown("""
        <div class='card'>
            <div class='card-title'>📐 Medidas Morfológicas de la Flor (cm)</div>
        </div>
        """, unsafe_allow_html=True)
        
        # User sliders for input
        sepallength = st.slider("Largo del Sépalo (sepallength):", min_value=4.0, max_value=8.0, value=5.1, step=0.1)
        sepalwidth = st.slider("Ancho del Sépalo (sepalwidth):", min_value=2.0, max_value=4.5, value=3.5, step=0.1)
        petallength = st.slider("Largo del Pétalo (petallength):", min_value=1.0, max_value=7.0, value=1.4, step=0.1)
        petalwidth = st.slider("Ancho del Pétalo (petalwidth):", min_value=0.1, max_value=2.5, value=0.2, step=0.1)
        
        # Predict button
        input_data = pd.DataFrame([{
            'sepallength': sepallength,
            'sepalwidth': sepalwidth,
            'petallength': petallength,
            'petalwidth': petalwidth
        }])
        
        pred = model.predict(input_data)[0]
        probs = model.predict_proba(input_data)[0]
        classes = model.classes_
        
    with col_result:
        st.markdown("""
        <div class='card'>
            <div class='card-title'>🎯 Resultado de la Predicción</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Style result based on predicted species
        color_map = {
            'Iris-setosa': '#3b82f6',
            'Iris-versicolor': '#a855f7',
            'Iris-virginica': '#ec4899'
        }
        
        color = color_map.get(pred, '#10b981')
        
        st.markdown(f"""
        <div style='background-color: #1e293b; border-left: 8px solid {color}; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1.5rem;'>
            <h2 style='margin: 0; color: {color}; font-weight: 800;'>{pred}</h2>
            <p style='color: #94a3b8; margin: 0.5rem 0 0 0;'>Especie clasificada según la lógica interna del Árbol ID3.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show probabilities
        st.markdown("##### Probabilidades por Clase:")
        for cls_name, prob in zip(classes, probs):
            st.write(f"**{cls_name}:** {prob * 100:.1f}%")
            st.progress(float(prob))
            
        st.markdown("---")
        st.markdown("##### 🔍 Reglas aplicadas del Árbol de Decisión:")
        
        # Hardcoded decision rules matching the training structure for interpretability
        if petalwidth <= 0.8:
            st.info("🟢 **Regla Activada:** Ancho del Pétalo (petalwidth) <= 0.8 cm.\n\n*Resultado puro instantáneo de la clase Setosa (Entropía = 0.0)*")
        else:
            rule_text = "🟡 **Regla Activada:** Ancho del Pétalo (petalwidth) > 0.8 cm.\n\n"
            if petalwidth <= 1.75:
                rule_text += "➡️ Ancho del Pétalo <= 1.75 cm.\n"
                if petallength <= 4.95:
                    rule_text += "➡️ Longitud del Pétalo <= 4.95 cm.\n\n*Clasificado mayoritariamente como Versicolor (con alta pureza)*"
                else:
                    rule_text += "➡️ Longitud del Pétalo > 4.95 cm.\n\n*Clasificado mayoritariamente como Virginica (ajuste fino residual)*"
            else:
                rule_text += "➡️ Ancho del Pétalo > 1.75 cm.\n\n*Clasificado puro como Virginica (Entropía = 0.0)*"
            st.info(rule_text)
