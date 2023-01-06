import http.server
import socketserver

PORT = 8000

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print("body string starts here:")
        print(body)
        print("end")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()



