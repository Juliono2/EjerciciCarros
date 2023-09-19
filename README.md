# Gestión de Carros en Flask

Este es un programa simple de gestión de carros desarrollado en Flask que te permite agregar carros a un archivo de texto y obtener la lista de carros guardados.

## Uso de POSTMAN

Para utilizar POSTMAN, sigue estos pasos:

1. Realiza un nuevo Workspace.

2. Crea una nueva conexión.

3. Adicionalmente, crea un nuevo request.

    3.1. La aplicación estará disponible en [http://localhost:5000](http://localhost:5000) en tu navegador.

    3.2. En el apartado Body, copia el contenido del archivo JSON llamado "standar_json.json" y pégalo en Body para RAW.

## API Endpoints

### Agregar un Carro

- **URL**: /carros
- **Método**: POST
- **Descripción**: Agrega un nuevo carro al archivo de texto con la información proporcionada en formato JSON.

### Obtener Lista de Carros

- **URL**: /carros
- **Método**: GET
- **Descripción**: Obtiene la lista de carros guardados en el archivo de texto.
