import requests

from bs4 import BeautifulSoup


def craw(url):
    f = open("lotto.txt", 'w')
    # URL Encoding
    # URL Decoding
    # referer : 특정한 사이트 안에서 요청을 했는가?
    # user-agent : 브라우저의 정보
    custom_headers = {
        'referer' : 'https://www.naver.com',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Whale/1.5.71.11 Safari/537.36'
    }

    # url : 영문
    req = requests.get(url, custom_headers)

    if req.status_code == requests.codes.ok:
        print("접속성공")
        html = BeautifulSoup(req.text, "html.parser")

        # .num_box로 하게되면 num_box자체는 1개밖에 없으므로
        # loop는 1번밖에 돌지 않는다
        number = html.select('.num_box .num')

        for item in number[:6]:
            print(item.text, end=", ")
            f.write(item.text+', ')
        print("보너스 번호 : ", number[-1].text)
        f.writelines("보너스 번호 : " + number[-1].text+'\n')
    else:
        print("접속 실패")
    f.close()



craw('https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=로또당첨번호')
