import requests

from bs4 import BeautifulSoup

url = "https://shopping.naver.com/"

req = requests.get(url)

if req.status_code == requests.codes.ok:
    print("접속성공")
    html = BeautifulSoup(req.text, "html.parser")

    # 각 리스트 원소마다 태그가 여러개 중첩되어 있음
    s_list1 = html.select('ul#mallListPage1 li')
    # print(s_list1)

    # 각 리스트 원소마다 태그가 1개밖에 없음
    s_list2 = html.select('ul#mallListPage1 li img')
    # print(s_list2)

    for i in s_list1:
        # 중첩되어 있는 태그를 하나씩 분리함
        mall_url = i.select_one('a')
        mall_name = i.select_one('img')

        # print(mall_name.get('alt'), mall_url.get('href'))
        # print(mall_name['alt'], mall_url['href'])

        # s_list2는 애초에 태그가 1개밖에 없으므로 분리 안해도 무방
    for i in s_list2:
        print(i['alt'])
        print(i.get('alt'))
