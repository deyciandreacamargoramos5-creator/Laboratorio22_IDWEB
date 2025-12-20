# Laboratorio N° 22_Ejercicio 08
# Autor: Andrea Camargo
# Colaboró:
# Tiempo: 15 minutos

import json
from wsgiref.simple_server import make_server

# Datos iniciales (Punto A)
libros = [{"id": 1, "titulo": "1984", "autor": "George Orwell", "año": 1949}]
id_actual = 2
def app(environ, start_response):
    global id_actual
    metodo = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]
    
    # a) Listar libros 
    if metodo == "GET" and path == "/libros":
        start_response("200 OK", [("Content-Type", "application/json")])
        return [json.dumps(libros).encode()]
    
    # b) Registrar un nuevo libro 
    elif metodo == "POST" and path == "/libros":
        length = int(environ.get("CONTENT_LENGTH", 0))
        body = environ["wsgi.input"].read(length)
        nuevo_libro = json.loads(body)     
        
        # Asignar ID incremental automáticamente
        nuevo_libro["id"] = id_actual
        libros.append(nuevo_libro)
        id_actual += 1
        start_response("201 Created", [("Content-Type", "application/json")])
        return [json.dumps(nuevo_libro).encode()]
    
    # c) Consultar un libro por ID 
    elif metodo == "GET" and path.startswith("/libros/"):
        try:
            libro_id = int(path.split("/")[-1])
            libro = next((l for l in libros if l["id"] == libro_id), None) 
            if libro:
                start_response("200 OK", [("Content-Type", "application/json")])
                return [json.dumps(libro).encode()]
        except ValueError:
            pass
        start_response("404 Not Found", [("Content-Type", "text/plain")])
        return [b"Libro no encontrado"]
    start_response("404 Not Found", [("Content-Type", "text/plain")])
    return [b"Ruta no valida"]
if __name__ == "__main__":
    server = make_server("localhost", 8000, app)
    print("Servidor de Libros en http://localhost:8000")
    server.serve_forever()