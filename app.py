from server import Server

handler = Server

PORT = 8000

server = http.server.HTTPServer(("", PORT), handler)

server.serve_forever()