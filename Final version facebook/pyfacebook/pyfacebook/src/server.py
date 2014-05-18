import BaseHTTPServer
import commentsInLastWeek
import DataForPlotting
import json
import urlparse

class Server(BaseHTTPServer.BaseHTTPRequestHandler):
   """Server class"""
   def do_HEAD(self):
      self.send_response(200)
      self.send_header("Content-Type","text/html")
      self.end_headers()

   def do_GET(self):
      self.send_response(200)
      self.send_header("Content-Type","application/json; charset=UTF-8")
      self.send_header("Access-Control-Allow-Origin","*")
      self.end_headers()
      fields = urlparse.parse_qs(self.path.strip('/'))
      if fields['query'][0] == 'comments-lastweek':
         self.wfile.write(json.dumps(commentsInLastWeek.getData()))
      elif fields['query'][0] == 'comments-percentage':
         self.wfile.write(json.dumps(DataForPlotting.getData()))

   def do_POST(self):
      self.send_response(200)
      self.send_header("Content-Type","application/json; charset=UTF-8")
      self.send_header("Access-Control-Allow-Origin","*")   
      self.end_headers()
      
def main():
   Server_ = BaseHTTPServer.HTTPServer
   http_server = Server_(('',1234),Server)

   try:
      http_server.serve_forever()
   except KeyboardInterrupt,e:
      print e.message
   finally:
      print "Server Stopped"
      http_server.server_close()

if __name__ == '__main__':
	main()
