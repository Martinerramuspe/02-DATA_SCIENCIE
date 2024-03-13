
import streamlit as st
import joblib
import dill
import requests
from io import StringIO
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import cross_val_score as cv
from sklearn.model_selection import StratifiedKFold
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from sklearn.preprocessing import FunctionTransformer
from sklearn.impute import SimpleImputer
import sklearn

# Carga el modelo.
# GitHub raw content URL.
github_url = 'https://raw.githubusercontent.com/Martinerramuspe/02-DATA_SCIENCIE/main/01-TELECOM_CHURN_PROJECT/05-DESPLIEGUE/Model_prepro.pkl'
response = requests.get(github_url)
Model_prepro = dill.loads(response.content) # asignamos nombre

# Función para hacer la predicción.
def predict(data):
    prediction = Model_prepro.predict(data)
    return prediction[0]

# Creacion de titulos, subtitulos, he insercion de imagen.
st.title('MODELO PREDICTIVO')
st.image("https://github.com/Martinerramuspe/04-ADJUNTOS/raw/main/orange.png", use_column_width=True)
st.write('Con esta herramienta podemos saber si se va a dar de baja o no, un cliente en funcion a su historian dentro de la empresa.')

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

# Convertir los datos  recolectados en "X" a  un DataFrame, para poder meter en modelo.
X_df = pd.DataFrame([X])

# Realizar la predicción cuando se presiona el botón
if st.button('Predecir'):
    prediction = predict(X_df)
    st.write('La predicción es:', prediction)