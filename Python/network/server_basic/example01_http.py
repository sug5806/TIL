import http.server
import socketserver

# 서버에 접속하는 포트
PORT = 8000

# 요청이 들어오면 어느 객체가 요청을 해석하고 처리할것이냐?
# Ex) 수리기사를 부르는 개념

# 현재 디렉토리와 하위의 파일을 제공하고 디렉토리 구조를 HTTP 요청에 직접 매핑함
Handler = http.server.SimpleHTTPRequestHandler

# ""으로 하면 localhost(127.0.0.1)이다"
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at PORT", PORT)
    # 클라이언트의 접속 요청을 수신대기 한다. 접속 요청이 있을시
    # 수락하고 SimpleHTTPRequestHandler의 handle 메소드를 호출한다.
    httpd.serve_forever()
