#!/bin/py
import http.server

# class CGIRequestHandler(http.server.CGIHTTPRequestHandler):
class Server(http.server.CGIHTTPRequestHandler):
    _PORT = 8080
    _HOST = '127.0.0.1'

    def route(self, **kwargs):
        # def redirect(self):
        path = kwargs['path']
        print('\n\n'+path+'\n\n')
        return self.path
    
    
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
            
        elif self.path == '/random_generator':
            self.path = 'cgi-bin/random_gen.py'
            
        elif self.path == '/text_figlet':
            self.path = 'cgi-bin/text_figlet.py'
            
        elif self.path == '/about':
            self.path = '/about.html'
        
        self.route(path=self.path)
        return http.server.CGIHTTPRequestHandler.do_GET(self)

    
    
    def run(self, port=_PORT, host=_HOST):
        server = http.server.HTTPServer(("", port), self)
        server.serve_forever()

# handler = CGIRequestHandler
app = Server

if __name__ == '__main__':
    app.run(app)

# PORT = 8000

# server = http.server.HTTPServer(("", PORT), handler)

# @app.route('/')
# def index():
#     return "index.html"

# @app.route('/random_generator')
# def random_generator():
#     return "cgi-bin/random_gen.py"





# index = handler.route(index)

# server.serve_forever()

####------------------------------------------

# def route(func):
#     def redirect(path):
#         print("Redirecting...")
#         print(path)
#         func()
#     return func()


# def index():
#     return "index.html"

# index = route(index)

