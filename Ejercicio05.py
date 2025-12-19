# Laboratorio N° 22_Ejercicio 04
# Autor: Andrea Camargo
# Colaboró:
# Tiempo: 15 minutos

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MiServidor(BaseHTTPRequestHandler):
    def do_GET(self):
       
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>Bienvenido al Servidor Estatico</h1>")
        
        elif self.path == "/saludo":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"msg": "Hola"}
            self.wfile.write(json.dumps(data).encode())

server = HTTPServer(("localhost", 8000), MiServidor)
print("Servidor corriendo en http://localhost:8000")
print("Presiona Ctrl+C para detenerlo")
server.serve_forever()