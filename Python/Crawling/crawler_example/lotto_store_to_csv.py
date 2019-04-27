import csv

import requests
from bs4 import BeautifulSoup

custom_header = {
    'referer': 'https://www.naver.com',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Whale/1.5.71.15 Safari/537.36'
}
# lotto.csv를 쓰기모드로 연다 만약 파일이 없으면 만든다.
csvfile = open('lotto.csv', 'w', newline='')
# lotto.csv를 csv.writer에 넣어준다.
# delimiter 옵션으로 문자 간격? 당 구분자를 지어준다
# 이것을 ,으로 해주거나 옵션을 주지 않으면 각 열에 따로따로 들어가지만
# 이외의 것을 하게되면 한 열에 전부다 들어가게 된다.
writer = csv.writer(csvfile, delimiter=',')

for i in range(1, 6):
    url = 'https://search.naver.com/search.naver?sm=tab_drt&where=nexearch&query=' + str(i) + '회로또'
    req = requests.get(url, headers=custom_header)

    if req.status_code == requests.codes.ok:
        print("접속 성공")
        html = BeautifulSoup(req.text, 'html.parser')

        items = html.select('div.num_box > span.num')

        for item in items[:6]:
            print(item.text, end=", ")
        print("보너스 : {}".format(items[-1].text))

        writer.writerow(['{}회차'.format(i), items[0].text, items[1].text, items[2].text, items[3].text, items[4].text,
                         items[5].text])
