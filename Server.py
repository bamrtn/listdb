import http.server
from listdb import listdb

PORT = 8000
Tables = ['a1','a2','a3','UserLogin','Sessions']

#Handler
class myHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path[0:3]=='/db':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            if self.path[4:] != '':
                self.wfile.write(bytes(listdb('asd.db',self.path[4:],Tables,'/db/'),"utf-8"))
            else:
                self.wfile.write(bytes(listdb('asd.db','a1',Tables,'/db/'),"utf-8"))
        else:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes("<h1>Hello World!</h1>","utf-8"))


#Starting server
server = http.server.HTTPServer(('0.0.0.0', PORT), myHandler)
print("serving at port", PORT)
server.serve_forever()
