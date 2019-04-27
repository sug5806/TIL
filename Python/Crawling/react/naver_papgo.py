import os
import sys
import urllib.request
import requests
import json

client_id = "Sy6ZNZtWnm3TQA5rcAL9" # 개발자센터에서 발급받은 Client ID 값
client_secret = "" # 개발자센터에서 발급받은 Client Secret 값


custom_header = {
    "X-Naver-Client-Id" : client_id,
    "X-Naver-Client-Secret":client_secret
}

encText = "나는 남자 입니다"#input("번역할 문장을 입력하세요:  ")
#data = "source=ko&target=en&text=" + encText

# 넘겨줄때는 딕셔너리 형태
data = {
    "source" : "ko",
    "target" : "en",
    "text" : encText
}

url = "https://openapi.naver.com/v1/papago/n2mt"

# 우리가 정보를 줄때는 post방식으로 해야함
#req = requests.get(url, headers=custom_header, params=data)
req = requests.post(url, headers=custom_header, data=data)

if req.status_code == requests.codes.ok:
    print("접속 성공")
    # json 형태
    #print(req.text)

    trans_data = json.loads(req.text)
    print(trans_data)
    print(trans_data['message']['result'])


# 단축 URL을 만드는 API 사용하기

