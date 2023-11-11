!pip install pythonping

import numpy as np
import pandas as pd
from pythonping import ping
import IPython.display

def check_server_status():
    ip = input("Ingrese la IP del servidor: ")

    # Realizamos el ping
    response = ping(ip, count=1)
    status = response.success()

    # Obtenemos los datos del ping
    latency = response.rtt[0] if status else np.nan

    # Mostramos la alerta
    if status:
        alert = IPython.display.HTML(
            f'<p style="color:green;">El servidor está activo. Latencia: {latency:.2f} ms</p>')
        display(alert)
    else:
        alert = IPython.display.HTML(
            '<p style="color:red;">El servidor está inactivo.</p>')
        display(alert)

# Llamamos a la función para verificar el estado del servidor
check_server_status()