import os
import cv2
import numpy as np
import face_recognition as fr


class Reconocimiento:
    def __init__(self, data_dir="data/embeddings/"):
        """
        Inicializa el sistema de reconocimiento facial.
        """
        self.data_dir = data_dir  
        self.known_faces = []
        self.known_labels = []
        self._cargar_datos()


    def _cargar_datos(self):
        """
        Carga los embeddings de rostros conocidos y sus etiquetas desde archivos .npy.
        """
        for filename in os.listdir(self.data_dir):
            if filename.endswith(".npy"):
                name = filename.split(".")[0]
                embedding = np.load(os.path.join(self.data_dir, filename))
                self.known_faces.append(embedding)
                self.known_labels.append(name)

        self.known_faces = np.array(self.known_faces)
        self.known_labels = np.array(self.known_labels)
        print(f"Se cargaron {len(self.known_faces)} rostros conocidos.")


    def real_time_recognition(self):
            """
            Realiza el reconocimiento facial en tiempo real y devuelve el nombre del estudiante reconocido.
            
            """
            
            cap = cv2.VideoCapture(0)
            recognized_name = None

            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Error al capturar el frame.")
                    break

                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
                
                face_locations = fr.face_locations(rgb_frame)
                face_encodings = fr.face_encodings(rgb_frame, face_locations)

                for face_encoding, face_location in zip(face_encodings, face_locations):
                    matches = fr.compare_faces(self.known_faces, face_encoding, tolerance=0.6)
                    face_distances = fr.face_distance(self.known_faces, face_encoding)
                    best_match_index = np.argmin(face_distances)

                    if matches[best_match_index]:
                        recognized_name = self.known_labels[best_match_index]
                        self._draw_label(frame, face_location, recognized_name, color=(0, 255, 0))
                    else:
                        self._draw_label(frame, face_location, "Desconocido", color=(0, 0, 255))

                cv2.imshow("Reconocimiento Facial", frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    print("Reconocimiento facial finalizado.")
                    break

            cap.release()
            cv2.destroyAllWindows()
            
            return recognized_name


    def capturar_foto(self, estudiante_id, nombre, output_dir="data/fotos/"):
        """
        Captura una sola foto del rostro del estudiante y genera un embedding.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        camara = cv2.VideoCapture(0)
        foto_tomada = False

        while not foto_tomada:
            ret, frame = camara.read()
            if not ret:
                print("Error al capturar la imagen.")
                break

           
            cv2.imshow("Captura de Foto - Presione 'c' para capturar", frame)

           
            if cv2.waitKey(1) & 0xFF == ord("c"):
                foto_tomada = True
                
                file_path = os.path.join(output_dir, f"{estudiante_id}_{nombre}.jpg")
                cv2.imwrite(file_path, frame)
                print(f"Foto guardada en {file_path}.")

               
                self._guardar_embedding(frame, estudiante_id, nombre)
                break

        camara.release()
        cv2.destroyAllWindows()
        

    def _guardar_embedding(self, frame, estudiante_id, nombre):
        """
        Genera y guarda el embedding del rostro basado en la foto capturada.
        """
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = fr.face_locations(rgb_image)
        face_encodings = fr.face_encodings(rgb_image, face_locations)

        if face_encodings:
            embedding = face_encodings[0]
            filename = os.path.join(self.data_dir, f"{estudiante_id}_{nombre}.npy")
            np.save(filename, embedding)
            print(f"Embedding guardado para {nombre} (ID: {estudiante_id}) en {filename}.")
        else:
            print(f"No se detectaron rostros en la imagen para {nombre} (ID: {estudiante_id}).")
            

    def _draw_label(self, frame, face_location, label, color):
        """
        Dibuja un rectángulo y etiqueta en el rostro reconocido.
        """
        top, right, bottom, left = [v * 4 for v in face_location]
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
        cv2.putText(frame, label, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)
