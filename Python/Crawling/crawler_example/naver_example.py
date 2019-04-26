# 웹 페이지에 접근해서 데이터를 가져온다.
import requests

# 가져온 데이터를 HTML로 해석한다.
from bs4 import BeautifulSoup

url = "https://www.naver.com/"

# HTTP Method : Get, Post, Put, Head, Delete
# Get : 리소스 얻기
# Post : 데이터 전달 - 로그인, 회원가입, 글쓰기 -> 이후에 수정할때
# Put : 리소스 전달(파일이나 동영상, 사진) - 사진 올리기 -> 최초 업로드
# Delete : 리소스 삭제
# Head : Method 확인
# 크름에 Postman 이라는 확장프로그램을 설치하라

req = requests.get(url)
#print(req.status_code)
#print(type(req.status_code))

# requests 모듈 안에 명세를 해놓음
if req.status_code == requests.codes.ok:
    print('접속 성공')
    # 여기서 데이터를 해석하면 된다
    # req.text  받아온 데이터가 담겨져 있다
    #print(req.text)
    html = BeautifulSoup(req.text, "html.parser")

    # select와 select_one의 차이점은 select_one()은 해당하는 것중 제일 첫번째만 반환
    # span1 = html.select('.PM_CL_realtimeKeyword_list_base span.ah_k')
    # print("span1", span1)
    # # 목록에 있는것 20개 돌아가고있는것 40
    # print(len(span1))



    # ~어떤 요소를 찾고
    # 그 요소 안에 각각의 요소를 다시 찾을 수 있다.
    # 클래스 ah_item에 랭크번호와 키워드가 들어있다
    items = html.select('.PM_CL_realtimeKeyword_list_base .ah_item')
    for item in items:
        # select_one으로 하나씩 뽑아온다.
        keyword = item.select_one('.ah_k')
        rank = item.select_one('.ah_r')
        link = item.select_one('.ah_a')
        #link['속성명']
        print(rank.text, keyword.text, link['href'])

else:
    print('접속 실패')











