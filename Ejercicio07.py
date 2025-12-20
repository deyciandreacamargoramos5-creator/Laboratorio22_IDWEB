# Laboratorio N° 22_Ejercicio 07
# Autor: Andrea Camargo
# Colaboró:
# Tiempo: 15 minutos

from wsgiref.simple_server import make_server

def app(environ, start_response):
    path = environ["PATH_INFO"] 
    if path == "/":
        status = "200 OK" 
        respuesta = b"Inicio" 
    elif path == "/saludo":
        status = "200 OK" 
        respuesta = b"Hola mundo desde WSGI" 
    else:
        status = "404 Not Found" 
        respuesta = b"Ruta no encontrada" 
    
    headers = [("Content-Type", "text/plain")] 
    start_response(status, headers)
    return [respuesta] 

server = make_server("localhost", 8000, app) 
server.serve_forever()