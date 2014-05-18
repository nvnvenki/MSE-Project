import BaseHTTPServer

class Server(BaseHTTPServer.BaseHTTPRequestHandler):
	"""Server class"""
        def do_HEAD(self):
		self.send_response(200)
                self.send_header("Content-Type","text/html")
                self.end_headers()

        def do_GET(self):
   	        self.wfile.write("Server sent response")
                print self.path
      		

def main():
	Server_ = BaseHTTPServer.HTTPServer
	http_server = Server_(('',8000),Server)

	try:
      		http_server.serve_forever()
   	except KeyboardInterrupt,e:
      		print e.message
   	finally:
   		print "Server Stopped"
      		http_server.server_close()

if __name__ == '__main__':
	main()