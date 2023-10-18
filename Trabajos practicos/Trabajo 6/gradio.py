import gradio as gr
import requests
from PIL import Image

# Definir función para obtener una imagen de Unsplash
def obtener_imagen(palabra_clave):
    # API Key de Unsplash (reemplazar con tu propia clave)
    api_key = "UbnoE5GocSne8GrjLvwddhiC9iXlfo9xy3fxM6YN4bg"

    # Llamar a la API de Unsplash
    response = requests.get(f"https://api.unsplash.com/photos/random?query+{palabra_clave}&client_id={api_key}")
    data = response.json()

    # Obtener la URL de la imagen y descargarla
    imagen_url = data["urls"]["regular"]
    imagen_resp = requests.get(imagen_url)
    imagen = Image.open(BytesIO(imagen_resp.content))

    return imagen

# Definir función para generar una frase relacionada a la palabra clave
def generar_frase(palabra_clave):
    # Aquí puedes usar cualquier método para generar la frase relacionada a la palabra clave
    frase = f"Una imagen relacionada a '{palabra_clave}'"

    return frase

# Definir la interfaz Gradio
interfaz = gr.Interface(
    fn=lambda texto: (obtener_imagen(texto), generar_frase(texto)),
    inputs="text",
    outputs=["image", "text"],
    layout="vertical",
    examples=[["guerra"]]
)

# Ejecutar la interfaz
interfaz.launch(share=True)