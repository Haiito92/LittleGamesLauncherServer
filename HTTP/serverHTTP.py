from http.server import HTTPServer, SimpleHTTPRequestHandler

server_address = ('', 8000)

httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

httpd.serve_forever()