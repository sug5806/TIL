import requests
from bs4 import BeautifulSoup

html = """<html> 
            <body> 
                <h1 id='title'>[1]크롤링이란?</h1> 
                <p class='cssstyle'>웹페이지에서 필요한 데이터를 추출하는 것</p> 
                <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p>
            </body> 
        </html>"""


# 태그가 아닌 문자열 자체로 검색
# 문자열, 정규표현식 등등으로 검색 가능

res = requests.get('https://news.v.daum.net/v/20190317150104393')
soup = BeautifulSoup(res.content, 'html5lib')

print(soup.find_all(string='공성윤')) # 작성자 이름
print(soup.find_all(string=['삼성 턱밑 쫓아온 화웨이 스마트폰.."올해 역전 예상"','공성윤'])) 
print(soup.find_all(string='삼성'))
#print(soup.find_all(string=res.compile('삼성'))[0])
# print(soup.find_all(string=res.complie('삼성)))
