import math
from io import BytesIO
from PIL import Image # Ejecutar python -m pip install requests pillow
import requests

def calcular_aspect_ratio(url: str):
    try:
        # 1. Se descarga la imagen desde la URL
        respuesta = requests.get(url)
        respuesta.raise_for_status() # Verifica que no haya errores (ej. 404)

        # 2. Abrir imagen desde los bytes descargados y obtener dimensiones
        imagen = Image.open(BytesIO(respuesta.content))
        ancho, alto = imagen.size

        # 3. Calcular el Máximo Común Divisor (MCD)
        mcd = math.gcd(ancho, alto)

        # 4. Dividir ancho y alto por el MCD para obtener la relacion simplificada
        ratio_ancho = ancho // mcd
        ratio_alto = alto // mcd

        print(f"Dimensiones: {ancho}x{alto}px")
        print(f"Aspect Ratio: {ratio_ancho}:{ratio_alto}")

    except Exception as e:
        print(f"No se pudo procesar la imagen. Error: {e}")

url_ejemplo = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
calcular_aspect_ratio(url_ejemplo)
url_ejemplo1 ="https://www.tooltyp.com/wp-content/uploads/2014/10/1900x920-8-beneficios-de-usar-imagenes-en-nuestros-sitios-web.jpg"
calcular_aspect_ratio(url_ejemplo1)