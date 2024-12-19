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

- Asegúrese de tener [lenguaje de programación o tecnología requerida] instalado.
- [Lista de otros prerrequisitos si es necesario]

### Pasos de Instalación

1. Clone el repositorio:
    ```bash
    git clone https://github.com/Limonagr/Projecto_programacion_avanzada.git
    ```
2. Navegue al directorio del proyecto:
    ```bash
    cd Projecto_programacion_avanzada
    ```
3. Instale las dependencias:
    ```bash
    [comando para instalar dependencias, por ejemplo, npm install]
    ```

## Uso

Proporcione instrucciones claras y ejemplos sobre cómo utilizar su proyecto.

1. Ejecute el proyecto:
    ```bash
    [comando para ejecutar el proyecto, por ejemplo, npm start]
    ```
2. Abra su navegador y navegue a `http://localhost:3000` para ver la aplicación en funcionamiento.

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
