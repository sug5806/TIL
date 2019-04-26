import http.server
import socketserver

# 서버에 접속하는 포트
PORT = 8000

# 요청이 들어오면 어느 객체가 요청을 해석하고 처리할것이냐?
# Ex) 수리기사를 부르는 개념
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at PORT", PORT)
    httpd.serve_forever()

