import requests
from io import StringIO
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import FunctionTransformer, MinMaxScaler
from sklearn.pipeline import Pipeline
import numpy as np
from Prepro01 import filtrar_columnas, mapear_international_plan, mapear_voice_mail_plan, eliminar_outliers, norma_variables
from joblib import load  # Importar la función load

# Cargar el preprocesador desde el archivo .joblib
preprocesador = load('Prepro01.joblib')

# Cargar el modelo desde el archivo .joblib
modelo = load('RandomForestClassifier.joblib')

# Función para hacer la predicción
def predecir(data):
    # Preprocesar los datos
    data_preprocesada = preprocesador.transform(data)
    # Realizar la predicción con el modelo
    prediction = modelo.predict(data_preprocesada)
    return prediction[0]

# Creacion de titulos, subtitulos, e insercion de imagen.
st.title('MODELO PREDICTIVO')
st.image("https://github.com/Martinerramuspe/04-ADJUNTOS/raw/main/orange.png", use_column_width=True)
st.write('Con esta herramienta podemos saber si se va a dar de baja o no un cliente en función a su historia dentro de la empresa.')

# Definir los datos de entrada.
X = {
    'State': 'NY', # valor fijo.
    'Account length': 150,# valor fijo.
    'Area code': 212,# valor fijo.
    'International plan': 'Yes',
    'Voice mail plan': 'No',
    'Number vmail messages': 0,
    'Total day minutes': 300.5,
    'Total day calls': 120,# valor fijo.
    'Total day charge': 50.75,
    'Total eve minutes': 250.3,
    'Total eve calls': 80,# valor fijo.
    'Total eve charge': 21.15,
    'Total night minutes': 200.2,
    'Total night calls': 100,# valor fijo.
    'Total night charge': 9.01,
    'Total intl minutes': 15.5,
    'Total intl calls': 4,
    'Total intl charge': 4.2,# valor fijo.
    'Customer service calls': 2,# valor fijo.
    'Churn': False# valor fijo.
}

# Creamos sliders para los inputs.
input_Number_vmail_messages = st.slider('Number vmail messages', min_value=0, max_value=70, value=X['Number vmail messages'])
input_Total_day_minutes = st.slider('Total day minutes', min_value=0.0, max_value=400.0, value=float(X['Total day minutes']))
input_Total_day_charge = st.slider('Total day charge', min_value=0.0, max_value=80.0, value=float(X['Total day charge']))
input_Total_eve_minutes = st.slider('Total eve minutes', min_value=0.0, max_value=400.0, value=X['Total eve minutes'])
input_Total_eve_charge = st.slider('Total eve charge', min_value=0.0, max_value=40.0, value=X['Total eve charge'])
input_Total_night_minutes = st.slider('Total night minutes', min_value=0.0, max_value=450.0, value=X['Total night minutes'])
input_Total_night_charge = st.slider('Total night charge', min_value=0.0, max_value=20.0, value=X['Total night charge'])
input_Total_intl_minutes = st.slider('Total intl minutes', min_value=0.0, max_value=30.0, value=X['Total intl minutes'])
input_Total_intl_calls = st.slider('Total intl calls', min_value=0, max_value=30, value=X['Total intl calls'])

# Actualizar los valores de entrada.
X.update({
    'Number vmail messages': input_Number_vmail_messages,
    'Total day minutes': input_Total_day_minutes,
    'Total day charge': input_Total_day_charge,
    'Total eve minutes': input_Total_eve_minutes,
    'Total eve charge': input_Total_eve_charge,
    'Total night minutes': input_Total_night_minutes,
    'Total night charge': input_Total_night_charge,
    'Total intl minutes': input_Total_intl_minutes,
    'Total intl calls': input_Total_intl_calls
})

# Creamos radio para 'International plan' y 'Voice mail plan'.
input_international_plan = st.radio('International plan', ['Yes', 'No'], index=0 if X['International plan'] == 'Yes' else 1)
input_voice_mail_plan = st.radio('Voice mail plan', ['Yes', 'No'], index=0 if X['Voice mail plan'] == 'Yes' else 1)

# Actualizar los valores de 'International plan' y 'Voice mail plan'
X.update({
    'International plan': input_international_plan,
    'Voice mail plan': input_voice_mail_plan
})

# Convertir los datos recolectados en "X" a un DataFrame para poder meter en modelo.
X_df = pd.DataFrame([X])

# Realizar la predicción cuando se presiona el botón
if st.button('Predecir'):
    X_df_preprocesado = preprocesador.transform(X_df)  # Preprocesar los datos de entrada
    prediction = predecir(X_df_preprocesado)  # Realizar la predicción con el modelo
    st.write('La predicción es:', prediction)
