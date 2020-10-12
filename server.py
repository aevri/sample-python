import os
import http.server
import random
import socketserver
import urllib.request

from http import HTTPStatus

WORDS_URL = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

with urllib.request.urlopen(WORDS_URL) as response:
   WORDS = text.splitlines(response.read())


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'Your random word is: ' + random.choice(WORDS)
        self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
