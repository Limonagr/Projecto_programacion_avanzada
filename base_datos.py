import os
import sqlite3
from datetime import datetime


class BaseDatos:
    def __init__(self, db_path="student_log.db", data_dir="data", embeddings_dir="data/embeddings/"):
        """
        Inicializa la conexión con la base de datos y asegura la existencia de los directorios.
        """
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.data_dir = data_dir  
        self.embeddings_dir = embeddings_dir  
        self.crear_tablas()
        self._asegurar_directorios()

    def _asegurar_directorios(self):
        """Crea los directorios base del data y embeddings si no existen."""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        if not os.path.exists(self.embeddings_dir):
            os.makedirs(self.embeddings_dir)

    def crear_tablas(self):
        """Crea las tablas necesarias en la base de datos."""
      
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes_registrados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL,
            fecha_registro TEXT NOT NULL,
            embedding_path TEXT NOT NULL
        )
        ''')

       
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS cupos_apartados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            estudiante_id INTEGER NOT NULL,
            nombre TEXT NOT NULL,
            hora_apartado TEXT NOT NULL
        )
        ''')

       
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS cupos_reclamados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            estudiante_id INTEGER NOT NULL,
            nombre TEXT NOT NULL,
            hora_reclamado TEXT NOT NULL
        )
        ''')

        self.connection.commit()

    def registrar_estudiante(self, nombre, embedding_filename):
        """
        Registra un nuevo estudiante o actualiza uno existente.
        Si el estudiante ya existe, actualiza su embedding y fecha de registro.
        
        :param nombre: Nombre del estudiante.
        :param embedding_filename: Nombre del archivo de embedding.
        """

       
        embedding_path = os.path.join(self.embeddings_dir, embedding_filename)

        
        if not os.path.exists(embedding_path):
            raise FileNotFoundError(f"El archivo de embedding {embedding_path} no existe.")

      
        fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.cursor.execute(
            """
                INSERT INTO estudiantes_registrados (nombre, fecha_registro, embedding_path)
                VALUES (?, ?, ?)
                ON CONFLICT(nombre) DO UPDATE SET 
                    fecha_registro = excluded.fecha_registro,
                    embedding_path = excluded.embedding_path
                """,
                (nombre, fecha_registro, embedding_path)
            )
            self.connection.commit()
            print(f"Estudiante '{nombre}' registrado o actualizado con éxito.")
        except Exception as e:
            print(f"Error al registrar/actualizar el estudiante '{nombre}': {e}")




    def buscar_estudiante(self, nombre=None):
        """
        Busca un estudiante por nombre.

        :param nombre: Nombre del estudiante.
        :return: Registro del estudiante o None si no existe.
        """
        if nombre:
            self.cursor.execute(
                "SELECT * FROM estudiantes_registrados WHERE nombre = ?",
                (nombre,) 
            )
        else:
            raise ValueError("Debe proporcionar un nombre para buscar un estudiante.")
        return self.cursor.fetchone()



    def apartar_cupo(self, estudiante_id, nombre):
        """
        Aparta un cupo para un estudiante.

        :param estudiante_id: ID del estudiante.
        :param nombre: Nombre del estudiante.
        """
        self.cursor.execute(
        "SELECT * FROM cupos_apartados WHERE estudiante_id = ? AND nombre = ?",
        (estudiante_id, nombre)
        )
        cupo_apartado = self.cursor.fetchone()
    
        if cupo_apartado:
            raise ValueError(f"{nombre} (ID: {estudiante_id}) ya ha apartado un cupo.")
            
        
        hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(
            "INSERT INTO cupos_apartados (estudiante_id, nombre, hora_apartado) VALUES (?, ?, ?)",
            (estudiante_id, nombre, hora)
        )
        self.connection.commit()
        print(f"Cupo apartado exitosamente para el estudiante {nombre} (ID: {estudiante_id}).")
        
        

    def reclamar_cupo(self, estudiante_id, nombre):
        """
        Reclama un cupo para un estudiante.

        :param estudiante_id: ID del estudiante.
        :param nombre: Nombre del estudiante.
        """
        self.cursor.execute(
        "SELECT * FROM cupos_reclamados WHERE estudiante_id = ? AND nombre = ?",
        (estudiante_id, nombre)
        )
        cupo_reclamado = self.cursor.fetchone()
    
        if cupo_reclamado:
            raise ValueError(f"{nombre} (ID: {estudiante_id}) ya ha reclamado un cupo.")
        
        self.cursor.execute(
            "SELECT * FROM cupos_apartados WHERE estudiante_id = ? AND nombre = ?",
            (estudiante_id, nombre)
        )
        cupo_apartado = self.cursor.fetchone()

        if not cupo_apartado:
            raise ValueError(f"No se encontró un cupo apartado para {nombre} (ID: {estudiante_id}).")
        hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(
            "INSERT INTO cupos_reclamados (estudiante_id, nombre, hora_reclamado) VALUES (?, ?, ?)",
            (estudiante_id, nombre, hora)
        )
        self.connection.commit()
        print(f"Cupo reclamado exitosamente para el estudiante {nombre} (ID: {estudiante_id}).")

    def cerrar(self):
        """Cierra la conexión con la base de datos."""
        self.connection.close()
