import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from base_datos import BaseDatos
from reconocimiento import Reconocimiento


class Interfaz:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Gestión de Cupos")
        self.root.geometry("400x400")
        self.root.configure(bg="#003366")  

        
        self.bd = BaseDatos()
        self.reconocimiento = Reconocimiento()

        
        container = tk.Frame(self.root, bg="#003366")
        container.pack(expand=True)

       
        tk.Label(
            container,
            text="Sistema para cupos",
            font=("Arial", 18),
            fg="white",
            bg="#003366"
        ).pack(pady=20)

        
        tk.Button(
            container,
            text="Apartar Cupo",
            font=("Arial", 16),
            bg="#00509E",
            fg="white",
            activebackground="#003f7f",
            activeforeground="white",
            command=self.apartar
        ).pack(pady=10)

        
        tk.Button(
            container,
            text="Reclamar Cupo",
            font=("Arial", 16),
            bg="#00509E",
            fg="white",
            activebackground="#003f7f",
            activeforeground="white",
            command=self.reclamar
        ).pack(pady=10)

        
        tk.Button(
            container,
            text="Registrar Estudiante",
            font=("Arial", 16),
            bg="#00509E",
            fg="white",
            activebackground="#003f7f",
            activeforeground="white",
            command=self.registrarse
        ).pack(pady=10)

        
        tk.Button(
            container,
            text="Ver Registros",
            font=("Arial", 16),
            bg="#00509E",
            fg="white",
            activebackground="#003f7f",
            activeforeground="white",
            command=self.ver_registros
        ).pack(pady=10)

        
        tk.Button(
            container,
            text="Salir",
            font=("Arial", 16),
            bg="#00509E",
            fg="white",
            activebackground="#003f7f",
            activeforeground="white",
            command=self.root.quit
        ).pack(pady=20)


    def apartar(self):
        """Lógica para apartar cupo usando reconocimiento facial en tiempo real."""
        messagebox.showinfo("Apartar Cupo", "Por favor, mírese a la cámara para reconocimiento.")

       
        recognized_name = self.reconocimiento.real_time_recognition()
        print(f"Nombre reconocido: {recognized_name}")

        if recognized_name:
            
            _, nombre = recognized_name.split("_", 1)
            print(f"Nombre extraído: {nombre}")

           
            estudiante = self.bd.buscar_estudiante(nombre=nombre)
            print(f"Estudiante encontrado: {estudiante}")

            if estudiante:
                estudiante_id = estudiante[0]  

                
                self.bd.apartar_cupo(estudiante_id, nombre)
                messagebox.showinfo("Éxito", f"Cupo apartado exitosamente para {nombre}.")
            else:
                messagebox.showerror("Error", f"No se encontró un estudiante registrado con el nombre {nombre}.")
        else:
            messagebox.showerror("Error", "No se reconoció ningún estudiante.")




    def reclamar(self):
        """Lógica para reclamar un cupo usando reconocimiento facial en tiempo real."""
        messagebox.showinfo("Reclamar Cupo", "Por favor, mírese a la cámara para reconocimiento.")

        
        recognized_name = self.reconocimiento.real_time_recognition()
        print(f"Nombre reconocido: {recognized_name}")

        if recognized_name:
           
            _, nombre = recognized_name.split("_", 1)
            print(f"Nombre extraído: {nombre}")

            
            estudiante = self.bd.buscar_estudiante(nombre=nombre)
            print(f"Estudiante encontrado: {estudiante}")

            if estudiante:
                estudiante_id = estudiante[0]  

                try:
                    
                    self.bd.reclamar_cupo(estudiante_id, nombre)
                    messagebox.showinfo("Éxito", f"Cupo reclamado exitosamente para {nombre}.")
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
            else:
                messagebox.showerror("Error", f"No se encontró un estudiante registrado con el nombre {nombre}.")
        else:
            messagebox.showerror("Error", "No se reconoció ningún estudiante.")



    def registrarse(self):
        """Abre una ventana para registrar un estudiante con nombre e ID."""
        ventana = tk.Toplevel(self.root)
        ventana.title("Registrar Estudiante")
        ventana.geometry("400x250")
        ventana.configure(bg="#003366")

        
        tk.Label(
            ventana, 
            text="Nombre:", 
            font=("Arial", 14), 
            fg="white", 
            bg="#003366"
        ).pack(pady=10)
        nombre_entry = tk.Entry(ventana, font=("Arial", 14))
        nombre_entry.pack(pady=5)

        
        tk.Label(
            ventana, 
            text="ID del Estudiante:", 
            font=("Arial", 14), 
            fg="white", 
            bg="#003366"
        ).pack(pady=10)
        id_entry = tk.Entry(ventana, font=("Arial", 14))
        id_entry.pack(pady=5)

        
        def confirmar_registro():
            nombre = nombre_entry.get().strip()
            estudiante_id = id_entry.get().strip()

            
            if not nombre or not estudiante_id:
                messagebox.showerror("Error", "Debe ingresar un nombre y un ID válidos.")
                return

            if not estudiante_id.isdigit():
                messagebox.showerror("Error", "El ID debe ser un número.")
                return

            estudiante_id = int(estudiante_id)  

           
            estudiante = self.bd.buscar_estudiante(nombre=nombre)
            embedding_filename = f"{estudiante_id}_{nombre}.npy" 

            if estudiante:
                renovar = messagebox.askyesno("Registro Existente", "Ya estás registrado. ¿Deseas renovar el registro?")
                if renovar:
                    
                    self.reconocimiento.capturar_foto(estudiante_id, nombre)
            
                   
                    self.bd.registrar_estudiante(nombre, embedding_filename)
                    messagebox.showinfo("Renovación Completa", "¡Fotos y registro actualizados exitosamente!")
            else:
                self.reconocimiento.capturar_foto(estudiante_id, nombre)
                self.bd.registrar_estudiante(nombre, embedding_filename)
                messagebox.showinfo("Registro Completo", "¡Estudiante registrado exitosamente!")
            

            ventana.destroy()  

        tk.Button(
            ventana,
            text="Confirmar Registro",
            font=("Arial", 14),
            bg="#00509E",
            fg="white",
            activebackground="#003f7f",
            activeforeground="white",
            command=confirmar_registro
        ).pack(pady=20)


    def ver_registros(self):
        """Ventana para seleccionar qué registros mostrar."""
        ventana = tk.Toplevel(self.root)
        ventana.title("Seleccionar tabla")
        ventana.geometry("300x200")

        tk.Label(
            ventana,
            text="Seleccione la tabla a mostrar:",
            font=("Arial", 14)
        ).pack(pady=20)

        botones_frame = tk.Frame(ventana)
        botones_frame.pack()

        tk.Button(
            botones_frame,
            text="Registrados",
            font=("Arial", 12),
            command=lambda: [self.mostrar_tabla("estudiantes_registrados"), ventana.destroy()]
        ).pack(pady=5)

        tk.Button(
            botones_frame,
            text="Apartados",
            font=("Arial", 12),
            command=lambda: [self.mostrar_tabla("cupos_apartados"), ventana.destroy()]
        ).pack(pady=5)

        tk.Button(
            botones_frame,
            text="Reclamados",
            font=("Arial", 12),
            command=lambda: [self.mostrar_tabla("cupos_reclamados"), ventana.destroy()]
        ).pack(pady=5)

    def mostrar_tabla(self, tabla):
        """Muestra el contenido de una tabla en una ventana nueva con un Treeview."""
        ventana = tk.Toplevel(self.root)
        ventana.title(f"Registros de {tabla}")
        ventana.geometry("600x400")

        
        tree = ttk.Treeview(ventana, columns=("#1", "#2", "#3"), show="headings")
        tree.pack(expand=True, fill="both")

        
        encabezados = {
            "estudiantes_registrados": ["Estudiante ID", "Nombre", "Fecha de Registro"],
            "cupos_apartados": ["Estudiante ID", "Nombre", "Hora Apartado"],
            "cupos_reclamados": ["Estudiante ID", "Nombre", "Hora Reclamado"]
        }
        columnas = encabezados.get(tabla)

        for i, col in enumerate(columnas, start=1):
            tree.heading(f"#{i}", text=col)
            tree.column(f"#{i}", width=200)

       
        self.bd.cursor.execute(f"SELECT * FROM {tabla}")
        registros = self.bd.cursor.fetchall()

        if registros:
            for registro in registros:
                tree.insert("", "end", values=registro)
        else:
            tk.Label(
                ventana,
                text="No hay registros disponibles.",
                font=("Arial", 14),
                fg="red"
            ).pack(pady=20)

    def iniciar(self):
        """Inicia la aplicación."""
        self.root.mainloop()

app = Interfaz()
app.iniciar()

