1. aws.amazon.com 가입

2. heroku.com 가입
3. heroku cli tool 설치

4. 개인 도메인 구입
   * gabia.com
   * https://www.hosting.kr/
   * https://www.whois.co.kr/
   
   
---

1. 파이썬 프로젝트 만들기
2. 장고 설치
3. 장고 프로젝트 만들기 : django-admin startproject config.
4. DB 초기화
5. 관리자 계정 생성 python manage.py createsuperuser [계정명]
6. 앱 만들기 : accounts, photo
   * python manage.py startapp accounts
   * python manage.py startapp photo
   * follow 기능 -> Ajax로 follow, unfollow, timeline구현
     * DM 구현해보기
   * 사진 업로드할때 필터 걸기 - 흑백
7. INSTALLED APPS에 추가

---

외래키로 PK로 걸어놓으면 PK에 Index를 걸어 속도가 빠르고 데이터 크기가 절약된다

raw_id_fields = ['author']
   * 이것을 하면 숫자로 선택할 수 있다
   
제네릭뷰 
  * 쿼리셋 변경하기, context_data 추가하기, 권한 체크, 함수형뷰 <-> 클래스
  

---

model에 이미지를 첨부하려면 Pyillow를 설치해야 한다

absolute_url을 지정해놓고 다른곳으로 가고싶다면 success_url로 지정하면된다
  * success_url이 우선순위가 더 높다

log in, log out은 장고가 제공해줘서 뷰를 만들지 않아도 된다

---
  ## 다른유저가 내 게시물 접근 못하게 하기
  방법 1 : html파일에서 하기
  방법 2 : dispath 등등

Life Cycle - iOS, Android, Vue, React, Django, Rails
Framework는 라이프 사이클이 존재 : 어떤 순서로 구동이 되느냐?  
  * Life Cycle을 정리를 해볼것  
  
URLConf -> View -> Model(View에서 DB가 필요하다면) 순으로 동작  
어떤 뷰를 구동할 때 그 안에서 동작하는 순서  

    
---

도식도 그려보기

소셜댓글은 나의 DB에 저장할수가 없어 악성댓글에 대처할수 없으나 유저 입장에서는 조작할수 없어 좋다

DOM구조하고 바꾸고 AJAX 걸기


1. 포스팅 저장하기 기능 구현
2. 저장한 포스팅 리스트 페이지 구현