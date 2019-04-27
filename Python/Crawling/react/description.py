"""
# requests : 웹 사이트에 접속, 데이터를 받아오는 역할
#   * 페이지 보기를 했을때 나오는 코드로 이용
# BeautifulSoup : 데이터를 HTML로 해석하는 역할

# 선행지식 : HTML에 대한 이해, CSS Selector를 만드는 방법


# 요소검사를 통해 확인할 수 있는 소스코드 or 업데이트되는 환경일 때
1) selennium : 웹 브라우저 자체를 컨트롤해서 Crawling(실시간으로 업데이트된 것을 가져오기 위해)
    * 요소를 선택해서 사용자의 동작을 흉내낸다. : 클릭, 키보드 입력
    * 이때는 선택자) xpath, css
    * 우클릭해서 copy를 하면 된다 그러나 selector에서 지원되지 않는 문법이 있으므로 카피하는것은 비추천
    * xpath는 그냥
2) BeatuifulSoup : 얻은 데이터를 HTML로 해석


request :
selenium : 컨트롤해야 하기때문에 request보다 느리다


페이지 이동을해도 페이지가 새로고침이 안되면 처음부터 다 불러와놓고 일부분만 보여준다거나 실시간으로 가져온다거나 둘중 하나이다

풀링 : 우리가 서버로 조회하는것
푸슁 : 서버가 우리에게 전달해주는것

days를 눌렀을떄 Headers로 보면 requestURL로 보면 링크가 있는데 어가면 막혀있다
  * reffer로 막아놓았다 확인하는 방법은 소스코드에서 아무 태그의 링크를 해당 URL로 바꿔보면 알수있다

"""
