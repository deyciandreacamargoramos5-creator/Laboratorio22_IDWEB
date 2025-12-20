# Laboratorio N° 22_Ejercicio 06
# Autor: Andrea Camargo
# Colaboró:
# Tiempo: 15 minutos

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SumaHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            
            length = int(self.headers["Content-Length"]) 
            
            body = self.rfile.read(length) 
            
            data = json.loads(body) 
            
            resultado = {"suma": data["a"] + data["b"]} 
            
            self.send_response(200) 
            self.send_header("Content-Type", "application/json") 
            self.end_headers()
            self.wfile.write(json.dumps(resultado).encode())
            
        except (KeyError, json.JSONDecodeError, TypeError):
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'{"error": "Datos invalidos. Enviar JSON con a y b"}')

puerto = 8000
server = HTTPServer(("localhost", puerto), SumaHandler) 
print(f"Servidor de SUMA escuchando en http://localhost:{puerto}")
print("Esperando peticion POST...")
server.serve_forever()