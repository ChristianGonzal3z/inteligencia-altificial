
from moviepy.editor import VideoFileClip
import cv2


"""
haarcascade_fullbody.xml
haarcascade_lefteye_2splits.xml
haarcascade_lowerbody.xml
haarcascade_eye_tree_eyeglasses.xml
haarcascade_smile.xml
haarcascade_frontalcatface.xml
haarcascade_profileface.xml
haarcascade_eye.xml
haarcascade_frontalface_default.xml
haarcascade_frontalface_alt_tree.xml
haarcascade_license_plate_rus_16stages.xml
haarcascade_frontalcatface_extended.xml
haarcascade_righteye_2splits.xml
haarcascade_russian_plate_number.xml
haarcascade_upperbody.xml
haarcascade_frontalface_alt.xml
haarcascade_frontalface_alt2.xml

""" 


# Cargar el clasificador de Haar
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Inicializar el video
clip = VideoFileClip("video.mp4")

# Función para procesar cada frame
def process_frame(frame):
    # Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar rostros en el frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    # Mostrar la cantidad de rostros detectados en pantalla
    
    cv2.putText(frame, f"Cantidad de rostros detectados:{len(faces)} "
                 , (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
     
    
    # Dibujar rectángulos alrededor de los rostros detectados
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
    
    return frame

# Procesar el video
processed_clip = clip.fl_image(process_frame)

# Reproducir el video
processed_clip.preview()

# Liberar recursos
clip.close()
processed_clip.close()