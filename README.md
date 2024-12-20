# Proyecto de Programación Avanzada

## Descripción

Este proyecto implementa un sistema de gestión de cupos que utiliza reconocimiento facial para registrar, reservar y reclamar cupos de manera automatizada.  
Combina tecnologías de **programación orientada a objetos (POO)**, **bases de datos** y una **interfaz gráfica de usuario** para brindar una solución eficiente y moderna para el manejo de estudiantes y recursos.  

La aplicación incluye características como:  
1. **Registro de estudiantes**:  
   - Captura de foto y generación de un perfil de reconocimiento facial para cada estudiante.  
   - Almacenamiento de la información del estudiante en una base de datos, incluyendo su nombre, fecha de registro y un archivo de embedding facial único.  

2. **Reconocimiento facial en tiempo real**:  
   - Uso de la cámara para identificar a los estudiantes registrados mediante comparación de sus rostros con los embeddings almacenados.  
   - Visualización de resultados en vivo, destacando rostros reconocidos y no reconocidos.  

3. **Gestión de cupos**:  
   - **Apartar cupo**: Identifica a los estudiantes y les permite reservar un cupo disponible.  
   - **Reclamar cupo**: Permite a los estudiantes reclamar un cupo previamente reservado, validando su identidad facial.  
   - Manejo de errores como intentar apartar o reclamar un cupo más de una vez.  

4. **Interfaz gráfica intuitiva**:  
   - Menús interactivos creados con **Tkinter**, que incluyen botones para registrar estudiantes, apartar cupos, reclamar cupos y visualizar registros.  
   - Ventanas dinámicas para mostrar tablas de registros de estudiantes, cupos reservados y cupos reclamados.  

5. **Base de datos robusta**:  
   - Diseño de tablas relacionales para almacenar información de estudiantes, reservas y reclamos.  
   - Automatización de tareas como la creación de tablas y directorios necesarios.  

6. **Manejo de datos biométricos**:  
   - Gestión segura de embeddings faciales, almacenados como archivos `.npy` para una comparación eficiente.  
   - Carga y validación de datos al iniciar el sistema.  


## Tabla de Contenidos

1. [Instalación](#instalacion)
2. [Uso](#uso)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Contribución](#contribucion)
5. [Licencia](#licencia)

## Instalación

Siga los siguientes pasos para instalar y configurar el proyecto en su máquina local.

### Prerrequisitos
Antes de instalar y ejecutar el proyecto, asegúrate de cumplir con los siguientes requerimientos:

    Sistema Operativo:
       - Windows 10/11, Linux o macOS.

    Python:
       - Python 3.8 o superior instalado en tu máquina.
       - Puedes descargar Python desde su página oficial.

    Bibliotecas necesarias:
        Las siguientes bibliotecas de Python son requeridas para este proyecto:
           - opencv-python
           - face-recognition
           - numpy
           - tkinter (incluido por defecto en la mayoría de las distribuciones de Python).
        Estas dependencias están listadas en el archivo requirements.txt.

    Cámara:
       - Una cámara funcional conectada al equipo para capturar imágenes en tiempo real (puede ser la cámara integrada de una laptop o una cámara USB externa).

    Editor de Texto o IDE:
       - Se recomienda un editor como Visual Studio Code, PyCharm, o Jupyter Notebook para trabajar con el código.

    Git (Opcional):
       - Si deseas clonar el repositorio del proyecto desde GitHub, necesitarás tener Git instalado. Descárgalo desde su página oficial.

### Pasos de Instalación
   Sigue estas instrucciones para configurar el proyecto en tu máquina local:
1. Clonar el Repositorio (Opcional)

Si el proyecto está en GitHub, clónalo con el siguiente comando:

git clone <URL_DEL_REPOSITORIO>

Si no está en GitHub, asegúrate de descargar los archivos del proyecto en una carpeta local.
2. Crear un Entorno Virtual

Es una buena práctica trabajar en un entorno virtual para evitar conflictos de dependencias. Para crear uno, usa los siguientes comandos:

# Crear el entorno virtual (llámalo venv o como prefieras)
python -m venv venv

# Activar el entorno virtual:
# En Windows
venv\Scripts\activate

# En macOS/Linux
source venv/bin/activate

3. Instalar Dependencias

Asegúrate de estar en la carpeta raíz del proyecto (donde está ubicado requirements.txt) y ejecuta:

pip install -r requirements.txt

Esto instalará todas las bibliotecas necesarias, incluyendo:

    opencv-python
    face-recognition
    numpy
    Pillow
    mediapipe

4. Crear Directorios Necesarios

El proyecto requiere algunos directorios para almacenar los datos. Si no están creados automáticamente, créalos manualmente:

mkdir data
mkdir data/embeddings
mkdir data/fotos

5. Inicializar la Base de Datos

El archivo base_datos.py inicializa la base de datos automáticamente al ejecutarse por primera vez. No necesitas configurar nada manualmente. Solo asegúrate de que el archivo student_log.db se crea en el mismo directorio del proyecto al iniciar.

Si deseas limpiar o reiniciar la base de datos en el futuro, puedes eliminar el archivo student_log.db y ejecutar nuevamente el sistema.
6. Probar la Instalación

Para verificar que todo esté funcionando correctamente:

    Abre la terminal y ejecuta la interfaz principal del proyecto:

    python interfaz.py

    Se abrirá una ventana gráfica. Comprueba que los botones funcionen:
        Prueba el registro de estudiantes.
        Verifica que la cámara funcione durante la captura de imágenes.
        Intenta apartar un cupo para validar el reconocimiento facial.

Solución de Problemas Comunes

    Error al importar bibliotecas (ModuleNotFoundError):
        Asegúrate de que instalaste las dependencias usando pip install -r requirements.txt.
        Si el error persiste, intenta instalar la biblioteca manualmente, por ejemplo:

    pip install opencv-python face-recognition numpy Pillow mediapipe

Problemas con la cámara:

    Verifica que la cámara esté conectada y funcional en otras aplicaciones (como la aplicación de la cámara en tu sistema operativo).
    Si usas varias cámaras, asegúrate de que cv2.VideoCapture(0) esté configurado correctamente en el archivo reconocimiento.py.

Error de permisos en macOS/Linux:

    Si encuentras problemas de permisos, ejecuta el script con privilegios elevados:

    sudo python interfaz.py

Errores en reconocimiento facial:

    Si los rostros no se reconocen correctamente, verifica que los embeddings están correctamente generados en la carpeta data/embeddings.
    Asegúrate de que las imágenes sean claras y no estén borrosas al registrar un estudiante.



---

## Uso

A continuación, se describen los pasos y ejemplos para utilizar el sistema de gestión de cupos con reconocimiento facial. El proyecto incluye varias funcionalidades que se pueden acceder mediante la interfaz gráfica de usuario (GUI).


#### 1. **Iniciar la aplicación**

1. Asegúrate de que los pasos de instalación están completos y los directorios necesarios (`data/`, `data/embeddings/`) están creados.
2. Ejecuta el archivo principal desde la terminal:
   ```bash
   python interfaz.py
   ```

#### 2. **Registrar un Estudiante**

Este proceso permite agregar un nuevo estudiante al sistema:

1. En la interfaz principal, haz clic en el botón **"Registrar Estudiante"**.
   - ![imagen](https://github.com/user-attachments/assets/794b34b7-2ecc-4a05-9010-974626a46d14)

3. Se abrirá una nueva ventana que solicitará:  
   - **Nombre** del estudiante.  
   - **ID del Estudiante** (debe ser un número único).
   - ![imagen](https://github.com/user-attachments/assets/5a25691b-9826-4a73-a64e-667f65d1464f)
 
4. Una vez ingresados los datos, la aplicación activará la cámara:
   - Asegúrate de que el rostro del estudiante esté claramente visible en el cuadro.  
   - Presiona la tecla **`c`** para capturar la foto.
5. El sistema generará un embedding facial a partir de la foto y guardará el registro del estudiante en la base de datos.
6. Recibirás un mensaje de confirmación indicando que el estudiante fue registrado exitosamente.


#### 3. **Apartar un Cupo**

El proceso para reservar un cupo es el siguiente:

1. En la interfaz principal, haz clic en el botón **"Apartar Cupo"**.
   - ![imagen](https://github.com/user-attachments/assets/19a1be54-cd32-4ec8-b964-b6b58ff9abfe)

2. Aparecerá un mensaje solicitando al estudiante que mire a la cámara.
   - ![imagen](https://github.com/user-attachments/assets/ce8c3b7a-f0cf-4d47-baca-191e815195f5)

3. La cámara se activará y realizará el reconocimiento facial en tiempo real:
   - Si el estudiante es reconocido, su información se recuperará de la base de datos.
   - El sistema verificará si el estudiante ya tiene un cupo reservado.
4. Si todo es válido, el sistema registrará la reserva en la base de datos y mostrará un mensaje de éxito.

**Nota**: Si el estudiante no es reconocido o ya tiene un cupo reservado, aparecerá un mensaje de error indicando el motivo.


#### 4. **Reclamar un Cupo**

El proceso para reclamar un cupo reservado es similar al anterior:

1. En la interfaz principal, haz clic en el botón **"Reclamar Cupo"**.
   - ![imagen](https://github.com/user-attachments/assets/292e92b9-630d-43b4-861b-7366d608a70b)

2. Aparecerá un mensaje solicitando al estudiante que mire a la cámara.
   - ![imagen](https://github.com/user-attachments/assets/241d0e90-c6e0-4f5c-98bc-154c51217eb8)

3. La cámara realizará el reconocimiento facial:
   - Si el estudiante es reconocido, su información se verificará en la base de datos para comprobar si tiene un cupo reservado.
   - Si tiene un cupo reservado, este será marcado como reclamado en el sistema.
     - ![imagen](https://github.com/user-attachments/assets/25190127-7432-4ff1-81d3-5c299ef70913)

4. El sistema mostrará un mensaje de éxito si el reclamo se realiza correctamente.


#### 5. **Ver Registros**

Esta funcionalidad permite visualizar la información almacenada en las tablas de la base de datos.

1. En la interfaz principal, haz clic en el botón **"Ver Registros"**.
  - ![imagen](https://github.com/user-attachments/assets/2b3d1bb8-396b-49f4-8c6e-7779b36960e2)

2. Se abrirá una ventana para seleccionar la tabla que deseas visualizar:
   - **Registrados**: Muestra los estudiantes registrados en el sistema.
   - **Apartados**: Muestra los cupos reservados por los estudiantes.
   - **Reclamados**: Muestra los cupos que han sido reclamados.
   - ![imagen](https://github.com/user-attachments/assets/c1db35df-1e90-40e2-82a3-cb1d88d91422)

3. Selecciona la tabla deseada, y una nueva ventana mostrará los registros en un formato tabular.

---

### Ejemplo de Flujo Completo

1. **Registrar un estudiante**:
   - Ingresa el nombre: `Juan Pérez`.
   - Ingresa el ID: `101`.
   - Captura la foto para generar el embedding.

2. **Apartar un cupo**:
   - Juan Pérez abre la aplicación y selecciona "Apartar Cupo".
   - Mira a la cámara y el sistema reconoce su rostro.
   - El sistema registra su reserva y muestra el mensaje: _"Cupo apartado exitosamente para Juan Pérez."_.

3. **Reclamar un cupo**:
   - Más tarde, Juan Pérez selecciona "Reclamar Cupo".
   - Mira a la cámara, es reconocido y el sistema valida que tiene un cupo reservado.
   - El sistema registra el reclamo y muestra el mensaje: _"Cupo reclamado exitosamente para Juan Pérez."_.

---

### Teclas y Acciones Importantes

- **`q`**: Finaliza el reconocimiento facial en cualquier momento.
- **`c`**: Captura una foto durante el registro de estudiantes.

---


### Ejemplos

- [Incluya ejemplos de uso, capturas de pantalla o GIFs si es necesario]

## Estructura del Proyecto

<nombre_del_proyecto>/
│
├── base_datos.py          # Gestión de la base de datos SQLite (registro, reservas, reclamos).
├── interfaz.py            # Interfaz gráfica del usuario (GUI) construida con Tkinter.
├── reconocimiento.py      # Lógica de reconocimiento facial y gestión de embeddings.
├── data/
│   ├── embeddings/        # Almacena archivos .npy con embeddings faciales.
│   ├── fotos/             # Carpeta opcional para guardar fotos capturadas.
│
├── requirements.txt       # Archivo con las dependencias del proyecto.
└── README.md              # Documentación del proyecto. 

## Licencia

Este proyecto está bajo la Licencia MIT. Esto significa que puedes usar, modificar y distribuir el código con libertad, siempre y cuando se incluya la información de la licencia original.
