---

title: 2019-04-29 Django bookmark
date: 2019-04-29 16:59:20
subtitle : Django bookmark
categories:
 - Django
tags:
 - Django

---


1. 파이썬 프로젝트 만들기 :
2. 장고 설치 : `pip install django==2.1`
3. 장고 프로젝트 만들기 : `django-admin startproject config .`
4. DB 초기화 : `python manage.py migrate`
5. 관리자 계정 생성 : `python manage.py createsuperuser`
6. 기본 앱 만들기 : `python manage.py startapp bookmark`
7. INSTALLED_APPS 에 추가 : bookmark  
--- 템플릿 폴더 검색, DB 변경사항 추가

---

앱
(custom field)
1. ``models.py`` 작성
    * 필드 => DB에 컬럼 -> 컬럼의 데이터 타입, 제약조건(``form.py`` 작성)
      * Bookmark site_name, url, created 이런 정보들만 입력받아서 저장한다 하면 form이 필요없음  
        User, username, paaword, first_name, last_name, create이외에
        DB에 저장되지 않는 항목들(비밀번호 확인과 같은 것, 전화번호 인증)이 추가로 필요하면 form이 필요함
    * models.Model을 상속받는 이유
        * models.Model이 가지고 있는 메서드나 속성값을 사용하기 위해서
        * models.Model : ORM 관련 기능들
            * ORM관련기능 : DB를 추상화해서 코드로 조작할 수 있게 하는 기능 -> 데이터를 추가, 수정, 검색, 삭제
    * created :
        작성자 -> 로그인한 유저 정보를 찾아서 추가
      * 작성자 != 로그인한 유저
         -> 모델 저장 직전에 직접 코드로 처리  
       작성일 -> 서버시간을 읽어서 timestamp값을 만들어 추가
    * 자동 옵션 auto_now, auto_now_add
       * auto_now : 저장, 갱신 이런것을 할때의 시간을 기준
       * auto_now_add : 생성할때의 시간      
            
2. `views.py` 작성
(context_processor 작성) 모든 페이지(템플릿 파일 전체)에 출력될 내용
    * 장바구니, user
(custom template tag)
    * 템플릿 엔진에서 지원하는 태그 외에, 개발자가 추가로 필요한 기능
    * 뷰 종류 -> 클래스형, 함수형, 서로 상호 기능 제약이 거의 없다.(둘중 아무거나로 해도 생산 없다)
       * 함수형 : def 뷰이름(request,[추가 인수]) :
          * CRUDL에 특별한 처리를 추가해야 하는 경우  
            함수형뷰는 클래스형 뷰에 비해서 자유도가 높다(커스터마이징)  
            처리할 코드를 직접 다 개발자가 작성  
       * 클래스형 : class 뷰이름(제네릭뷰):
          * CRUDL에 관련 기능은 자주 사용하기 떄문에 장고에서 만들어 놓음  
            클래스형뷰가 함수형뷰 보다 생산성이 좋다  
            제네릭 기능외에 추가적인 기능을 개발자가 작성  
            메서드 방식- 커스터마이징에 관련된 메서드를 찾아야 한다.  
            `from django.views.generic`에 다 있음  
              * 메타 클래스는 옵션 클래스 -> 내가 상속을 받았는데, 속성값에 변경이 필요하다면 사용
        

1. `urls.py` 작성  
    * namespace = 이름 공간  
     다른 앱들과 url pattern 이름이 겹치는 것을 방지하기 위해서 사용  
     2.x버전 이전에는 namespace라는 인수가 존재  
     함수형 뷰 : 이름만 쓴다  
     클래스형 뷰 : 이름.as_view()
      * Ex) `path('', BookmarkList.as_view(), name='index')`
      * 그 글을 특정하기 위해서는 path방식이나 query string을 작성해야한다.(create제외 detail, delete, update)
          * localhost/bookmark/1 : 글보기, 수정, 삭제 
            localhost/bookmark/create : 글쓰기  
            `<value>/` 이렇게 설정을 하면 위에 2개 모두 해당된다.  
            `<int:value>/` 이렇게 설정하면 위에것만 해당된다.
           * converter가 없으면 무조건 str이 기본값
            * int : 정수  
             str : 문자열  
             slug : 여러 단어들을 뭉쳐서 주소로 만드는것(주소도 SEO에 들어간다) => SEO 때문에 사용  
             uuid : 많이 쓰이지는 않는다, 어플리케이션 호출  
              * Ex) 웹서핑을 하다가 어플을 실행할때  
             path : `bookmark/<path:value/>` => bookmark/19/04/29
             위의 기본 converter를 제외한 형태가 필요하다면 custom converter를 만든다.  
            
          * `path('delete/<int:pk>/', BookmarkDelete.as_view(), name='delete')`
            * pk = primary key  
             int = converter -> 여기에 들어 오는 값을 int로 변환하겠다
          * 어떤 사람이 detail/abc/로 접속을 하게되면 여기에 접속할 수 없다.
      
2. template 만들기
3. `admin.py` 추가
   * 관리자 페이지 목록에 표시될 내용  
     확인 메시지에 출력되는 내용을 만들기 위함
    * `__str__(self)`을 이용
         ```python
          def __str__(self):
              return "Site name : " + self.site_name + ", URL : " + self.url
          ```
    * 모델 클래스가 수정됐다고 해서 항상 migrate를 해야하는것은 아니.
    DB에 변경사항이 반영돼야할 항목들만 migrate를 한다

---

SEO - Search Engin OPtimization  
  * HTML 표준에 맞춰 Meta Tag, OpenGraph -> 프론트가 하는일
  * 최신글을 계속 보고 태그를 익히는게 좋음게 -> 계속 바뀌기 때문
  
CSS Framework
1. Bootstrap
2. Falt UI
3. Material Design Lite : Google - Android랑 디자인이 비슷하다

---

```html
<form action="" method="post">
    {% csrf_token %}
    
    {{form.as_p}}
    <input type="submit" value="Create">
</form>
```
추가, 수정, 삭제의 경우 해당 기능을 완료한 후에 이동할 페이지가 필요하다.  
1. view 클래스에 success_url 이라는 속성값을 지정
2. model에 get_absolute_url이라는 메서드를 만든다.
  
공통으로 들어갈 부분을 template파일 하나로 분리한다.
* 확장 : 상속을 받아 공통된 부분을 껴놓는것  
  1. 프로젝트에다 폴더를 하나 만들고 base.html파일을 만든다.  
  블록에 상속할 내용을 넣는다.  
  2. 자식파일에는 부모와 중복되는 내용은 다 지워준다.
  3. 자식에서 블록을 만들면 부모의것을 덮어쓰고 없으면 부모것을 쓴다.
* 루트에 있는 common_template를 인식시키려면 settings로 가서 DIR을 수정해준다.

---

과제 : 오늘한거 복습,  bootstrap 보기, 개인 프로젝트에 오늘한거 적용하