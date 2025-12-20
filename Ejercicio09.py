# Laboratorio N° 22_Ejercicio 09
# Autor: Andrea Camargo
# Colaboró:
# Tiempo: 15 minutos

from wsgiref.simple_server import make_server
import json, os, mimetypes
from urllib.parse import unquote

# Directorio donde guardaremos el HTML
STATIC_DIR = "static"

# Datos iniciales (Punto API)
equipos = [
    {"id": 1, "nombre": "Real Madrid", "ciudad": "Madrid", "nivelAtaque": 10, "nivelDefensa": 9},
    {"id": 2, "nombre": "Melgar", "ciudad": "Arequipa", "nivelAtaque": 5, "nivelDefensa": 4}
]
id_counter = 3

def servir_estatico(path):
    file_path = path.lstrip("/")
    # Buscamos dentro de la carpeta 'static'
    full_path = os.path.join(STATIC_DIR, file_path.replace("static/", ""))
    
    if not os.path.isfile(full_path): 
        return None, None
    
    ctype, _ = mimetypes.guess_type(full_path)
    with open(full_path, "rb") as f:
        return f.read(), ctype or "application/octet-stream"

def app(environ, start_response):
    global id_counter
    metodo = environ["REQUEST_METHOD"]
    path = unquote(environ["PATH_INFO"])

    # 1. Servir archivos estáticos
    if path.startswith("/static/"):
        contenido, tipo = servir_estatico(path)
        if contenido:
            start_response("200 OK", [("Content-Type", tipo)])
            return [contenido]
        
    # 2. Ruta principal (Carga el index.html de la carpeta static)
    if metodo == "GET" and path == "/":
        contenido, tipo = servir_estatico("index.html")
        if contenido:
            start_response("200 OK", [("Content-Type", tipo)])
            return [contenido]
        else:
            start_response("404 Not Found", [("Content-Type", "text/plain")])
            return [b"Error: No se encontro index.html en la carpeta static"]

    # 3. API de Equipos
    if path == "/equipos":
        if metodo == "GET":
            start_response("200 OK", [("Content-Type", "application/json")])
            return [json.dumps(equipos).encode()]
        elif metodo == "POST":
            length = int(environ.get("CONTENT_LENGTH", 0))
            data = json.loads(environ["wsgi.input"].read(length))
            data["id"] = id_counter
            equipos.append(data)
            id_counter += 1
            start_response("201 Created", [("Content-Type", "application/json")])
            return [json.dumps(data).encode()]

    # 4. Consultar por ID
    elif path.startswith("/equipos/"):
        try:
            eq_id = int(path.split("/")[-1])
            equipo = next((e for e in equipos if e["id"] == eq_id), None)
            if equipo:
                start_response("200 OK", [("Content-Type", "application/json")])
                return [json.dumps(equipo).encode()]
        except: pass
        start_response("404 Not Found", [("Content-Type", "text/plain")])
        return [b"Equipo no encontrado"]

    start_response("404 Not Found", [("Content-Type", "text/plain")])
    return [b"No encontrado"]

# Iniciar el servidor
if __name__ == "__main__":
    server = make_server("localhost", 8000, app)
    print("Servidor Avanzado corriendo en http://localhost:8000")
    server.serve_forever()