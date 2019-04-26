"""

CGI
Common Gateway Interface
CGI의 단점 : 요청이 있을 때마다 프로세스(응용프로그램)을 새로 실행
    이로인해 리로스관리가 힘듬, 오버헤드가 심하다

CGI의 장점 : 특별한 추가 프로그램 없이도 여러 언어의 스크립트 실행 가능

"""

import http.server
PORT = 8000

class Handler(http.server.CGIHTTPRequestHandler):
    # cgi 디렉토리 밑에 있는 애들만 실행이 된다
    # 이것을 이용하여 스크립트를 실행해 결과를 얻을 수 있다
    cgi_directories = ['/cgi']
with http.server.HTTPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

