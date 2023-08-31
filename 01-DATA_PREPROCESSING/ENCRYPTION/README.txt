
Este MODELO realiza una serie de pasos para encriptar y cargar datos de manera segura. Comienza importando bibliotecas como pandas para el manejo de datos, cryptography para encriptación y PyGithub para interactuar con GitHub. Luego, define una función para encriptar valores y una clave de encriptación. Carga un archivo CSV desde una URL en un DataFrame y encripta valores en columnas específicas. Después de encriptar los datos, los muestra y convierte el DataFrame encriptado a formato CSV. Utiliza un token de acceso personal para autenticarse en GitHub y especifica detalles del repositorio. Con PyGithub, crea un archivo encriptado en el repositorio, lo que garantiza que los datos encriptados se almacenen en GitHub de manera segura. Este proceso garantiza que los datos confidenciales estén protegidos mediante encriptación antes de cargarlos en un repositorio remoto.

PROCESO:

1-Se instalan las bibliotecas necesarias: pandas, cryptography y PyGithub.

2-Se importan las bibliotecas requeridas.

3-Se define una función llamada encriptar_valor que toma un valor y una clave de encriptación. Esta función encripta el valor utilizando la clave.

4-Se define una clave de encriptación.

5-Se carga un archivo CSV desde una URL en un DataFrame de pandas.

6-Se itera a través de las columnas especificadas en columnas_encriptar.

7-Para cada valor en las columnas a encriptar, se aplica la función de encriptación definida previamente.

8-Se muestra en la consola el DataFrame con los valores encriptados.

9-Se convierte el DataFrame encriptado a formato CSV en memoria utilizando io.StringIO.

10-Se autentica en GitHub utilizando un token de acceso personal.

11-Se especifican detalles del repositorio, como el nombre de usuario, el nombre del repositorio, el nombre del archivo en GitHub y la rama.

12-Se crea un objeto de repositorio usando PyGithub.

13-Se utiliza el método create_file para subir el archivo encriptado al repositorio en GitHub.