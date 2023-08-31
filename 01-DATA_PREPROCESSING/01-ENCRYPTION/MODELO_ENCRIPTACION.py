# Instalación de las bibliotecas requeridas
# pip install pandas cryptography PyGithub
import pandas as pd
from cryptography.fernet import Fernet
import base64  # Importamos la biblioteca base64
from github import Github
import io

# Definir la función para encriptar un valor usando Fernet
def encriptar_valor(valor, fernet):
    if isinstance(valor, (int, float)):
        valor = str(valor)
    return fernet.encrypt(valor.encode())

# Generar una clave Fernet y convertirla a base64
clave = Fernet.generate_key()
clave_base64 = base64.urlsafe_b64encode(clave)
print("Clave generada en base64:", clave_base64)

# Crear un objeto Fernet con la clave generada
fernet = Fernet(clave)

# URL del archivo CSV original
url_csv = 'https://raw.githubusercontent.com/Martinerramuspe/05-DATA_CSV/main/ejemplo.csv'
# Nombres de las columnas a encriptar
columnas_encriptar = ['col1', 'col2', 'col3']  # Cambia esto a los nombres de las columnas que deseas encriptar

# Cargar el archivo CSV desde la URL en un DataFrame
df = pd.read_csv(url_csv)

# Encriptar el DataFrame
df_encriptado = df.copy()
for columna in columnas_encriptar:
    df_encriptado[columna] = df_encriptado[columna].apply(lambda x: encriptar_valor(x, fernet))

# Mostrar el DataFrame encriptado
print("DataFrame Encriptado:")
print(df_encriptado)

# Convertir el DataFrame encriptado a formato CSV en memoria
csv_buffer = io.StringIO()
df_encriptado.to_csv(csv_buffer, index=False)
csv_content = csv_buffer.getvalue()

# Autenticación utilizando un token de acceso personal de GitHub
access_token = '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'
g = Github(access_token)

# Detalles del repositorio y el archivo en GitHub
repo_username = 'Martinerramuspe'
repo_name = '05-DATA_CSV'
github_file_name = 'encriptado.csv'
branch_name = 'main'

# Construir la ruta completa al repositorio
repo_path = f'{repo_username}/{repo_name}'

# Obtener una referencia al repositorio en GitHub
repo = g.get_repo(repo_path)

# Subir el archivo CSV encriptado al repositorio
repo.create_file(
    path=github_file_name,
    message="Subiendo archivo CSV encriptado",
    content=csv_content,
    branch=branch_name
)

