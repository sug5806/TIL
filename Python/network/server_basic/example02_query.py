from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

# 1. 코드를 보낸다
# 2. 코드를 읽는다
# 3. 분리한다

PORT = 8080

class Handler(BaseHTTPRequestHandler):
    # do_GET과 do_POST라는 이름은 바꾸면 안되며 고정이다

    # 과제
    # do_GET : 검색창 만들기
    # do_POST : 검색 결과 보여주기 - 네이버에서 크롤링

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # url 를 쪼개준다
        # 주소표시줄에 나타난다
        query_text = urlparse(self.path).query
        print(query_text)
        query_vars = parse_qs(query_text)
        # 값이 리스트로 되어있는 이유는 변수명은 하나지만 값을 여러개 보낼 수 있다
        print(query_vars)

        # 1. 딕셔너리를 다룰 수 있는가?
        # 2. 변수형에 대해 인지하고 있는가?
        # 3. 연산에 대해 알고 있는가?

        # query string으로 키와 몸무게를 전달받아서
        # bmi를 계산해서 message로 출력하시오
        # BMI = 몸무게/신장^2

        message = "welcome"
        form_html = """
            <form action='' method='post'>
            
                <label>Weight:<input type='text' name='weight'></label>
                <label>Height:<input type='text' name='height'></label>
                <input type=submit value="Calc">
            </form>
        """
        if 'weight' in query_vars and 'height' in query_vars:
            weight = float(query_vars['weight'][0])
            height = float(query_vars['height'][0])
            bmi = weight / ((height / 100) ** 2)
            message += " BMI " + str(bmi)
        message += form_html
        # response 메시지를 파일처럼 쓴다
        self.wfile.write(bytes(message, "utf-8"))
        return


    def do_POST(self):
        content_length = int(self.headers.get('Content-Length'))
        # response 메시지를 파일처럼 읽는다
        post_body = self.rfile.read(content_length)
        # 파일을 해석해서 해석한
        queries = parse_qs(post_body.decode('utf8'))
        print(queries)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = ""
        if 'weight' in queries and 'height' in queries:
            weight = float(queries['weight'][0])
            height = float(queries['height'][0])
            bmi = weight / ((height / 100) ** 2)
            message += " BMI " + str("{:0.2f}".format(bmi))

        self.wfile.write(bytes("POST Test {}".format(message), "utf-8"))
        return

# 한페이지에서 접속 메소드에따라 기능을 분기
# 회원가입 페이지 domain.com/signup/
# GET : 회원가입 양식 보여주기
# POST : 전달받은 데이터를 처리해서 회원가입 진행하기(데이터베이스에 저장하기)
#     메소드를 통해 분기하는 방식이 좋다

def run():
    # example01_http 와 똑같음
    server_address = ('127.0.0.1', PORT)
    httpd = HTTPServer(server_address, Handler)
    print("serving at PORT", PORT)
    httpd.serve_forever()

run()