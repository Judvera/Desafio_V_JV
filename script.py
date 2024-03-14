import json
from usuario import Usuario

# Definir la ruta de los archivos
archivo_usuarios = "usuarios.txt"
archivo_error_log = "error.log"

# Función para manejar las excepciones y escribir en el archivo de registro de errores
def manejar_excepcion(excepcion):
    with open(archivo_error_log, "a") as file:
        file.write(f"Error: {str(excepcion)}\n")

# Lista para almacenar las instancias de Usuario creadas correctamente
usuarios = []

# Abrir el archivo de usuarios y procesar cada línea
with open(archivo_usuarios, "r") as file:
    for linea in file:
        try:
            # Parsear el JSON de la línea y crear una instancia de Usuario
            datos_usuario = json.loads(linea)
            nuevo_usuario = Usuario(datos_usuario["nombre"], datos_usuario["apellido"], datos_usuario["email"], datos_usuario["genero"])
            usuarios.append(nuevo_usuario)
        except Exception as e:
            # Manejar la excepción y escribir en el archivo de registro de errores
            manejar_excepcion(e)

# Imprimir la lista de usuarios creados correctamente
print("Usuarios creados exitosamente:")
for usuario in usuarios:
    print(f"- {usuario.nombre} {usuario.apellidos}")

