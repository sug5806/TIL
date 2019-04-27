크롤러 : 웹 페이지에 있는 자료를 자동으로 수집하는 프로그램
Ex) 검색엔진
-->
Robot.txt : 검색엔진에게 어디까지 검색을 허용할 것이냐?


브라우저가 혹은 크롤러 어떤식으로 서버에 접근해서 데이터를 가져가느냐?
1. 주소를 입력하면 해당 서버로 접근한다.  


2. 웹 서버 프로그램이 해당 주소에 맞는 내용을 전달한다.
  * request -> 3rd party 모듈  
  * urllib의 wrapper 클래스    

  
3. 소스   
  * 받은 내용을 해석해서 내가 원하는 데이터를 찾는다. 뽑아낸다.  
    * BeautifulSoup   
    * HTML 코드의 해석  
    * CSS Selector 만드는 방법  


모듈 설치 :  
1. request -> pip install request  
2. BeautifulSoup -> pip install BeautifulSoup4  


크롤러 자체는 불법이 아니나 얻은 정보로 수익창출을 하면 불법이다.  
크롤러를 이용해 매크로 구현가능  


웹 페이지에 접근해서 데이터를 가져온다.  
requests는 Ajax로 받아온 데이터를 실시간으로 반영할 수 없다.  
requestt로 받아온 데이터는 소스보기에서 보는 소스까지만 있다.  
  * selenium : 웹 브라우저를 원격 조작하는 방식의 크롤러
  * 크롤링 모듈 : selenium, scrapy  
  
```python
import requests
```


# 가져온 데이터를 HTML로 해석한다.
```python
from bs4 import BeautifulSoup
```

개발자도구의 elements와 우클릭 페이지 소스보기가 다른경우가 있다
  * 페이지 소스보기 : 맨처음 
  * 개발자 도구 Elements
    * AJAX를 이용해 일부만 리프레쉬가능

    
개발자도구
   * Sources를 통해 홈페이지가 어떻게 구성되어 있는지 알 수 있다
   * Network : 웹페이지를 띄울때 파일들이 잘 받아와졌나 볼 수 있다
      * Protocol : h2은 http2.0으로 접속을 하였다.
      
      
셀렉터
HTML 태그
1. Container Tag : 안에 내용을 포함하고 있는 태그(Ex. `<div td="asdf">내용</div>`)
2. Empty Tag : 안에 내용을 포함하고 있지 않는 태그(Ex. `<img src="이미지주소">`)


가지고오고 싶은 내용을 감싸고있는 태그를 가져온다.
### 단일 셀렉터
1. tag이름 : div
  * 태그는 속성을 갖는다. -> `<tag id="" class="test" data-rel="" data-num="">cont</tag>`
2. id : 태그와 구분하기위해 #super -> 한 페이지 내에서 단 한개
3. class : 태그와 구분하기위해 .test -> 별명또는 그룹 개념

### 다중 셀렉터  
~안에 있는 무엇  
1. div ul li.ah_k -> 띄어쓰기로 구분  
  * div li.ah_k : 중간경로 생략 가능, 그냥 ~안에  
2. div > ul > li.ah_k : >로 구분, 조금 더 빠르다  
  * 중간경로 생략 불가능, ~바로 ~안에  
~이고 ~인것  
`<span class="ah_k">???</span>`
span.ah_k.anroll

`<div class="ah_k">???</div>`
~의 근처에 있는 것

