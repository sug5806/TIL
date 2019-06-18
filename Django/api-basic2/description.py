"""
API : Application Programming Interface

백엔드 프로그래머 : 데이터를 전달 받고, 가공, 저장 전달하는 역할
- 그동안 일반 뷰를 이용하여 했다
뷰 - 데이터를 전달 받는 인터페이스를 제공하던가, 전달 받은 데이터를 Model을 사용해서 DB에 저장하는 역할

- 일반 회원 가입 : 주소, 주민번호, 휴대폰 번호
- 판매자회원 가입 : 사업자번호, 사업장주소, 사업장 전화번호, 전자상거래 사업자 번호
공통사항 : username, password, first_name, last_name

1) 모델이 1개일 경우 : 필수 필드가 무엇인지 회원 타입에 따라서 분기
2) 모델을 여러개 만드는 경우 :

--------------------------------------------------------------------------

프론트 개발자 : 사용자가 만나게 되는 UI를 제공하는 사람

웹 프론트 엔드 개발자 : Template파일에서 Form을 출력하고, context value 내용을 출력 -> 화면을 렌더링 한다
- 백엔드 프로그래머가 context_data에 담아서 넘겨준 데이터를 가지고

- IOS, Android 앱 개발자들 : 프론트 개발자가 능동적으로 데이터를 요청해서
받아갈 수 있게 만드는 것 = API
앱의 화면 설계도 API를 통해서 한다.

API를 통해서만 앱을 만들 수 있다.
iOS : Cocoa CoreUI
Android : Android OS API

네이버 API(로그인), Facebook API(로그인), IAMPORT API(결제)

- 내 서비스에서 제공하는 기능을 상대가 능동적으로 활용할 수 있도록 권한을 제공하는 것

- 트위터 서비스
모델
뷰 : 뷰를 제거하면 UI를 제공하지 않겠다. 기능이 없다는 아니다
iOS, Android, Angular, React, Vue를 사용해서 API를 호출해서 UI를 제공해야한다.

내 웹 서비스에서 API를 지원하겠다.
내 프로젝트에 API뷰를 작성하겠다. (UI를 제공하는 뷰를 제공하겠다. X)

1) API를 만들고 웹 서비스를 작성하는 경우 : 트위터 - UI뷰가 없다. API를 가지고 프론트 렌더링
2) 웹 서비스를 작성하고 API를 만들어 제공하는 경우 - 대부분

- 웹 서비스를 제작하는데 있어서 유용한 경우 - 품질향상
- 외부에 서비스를 제공하기 위해서 - 시장 점유율 상승


Swagger - Documantation - 문서화
API 사용자들을 위해 제공
- 인자에 대한 설명
- 처리 결과에 대한 설명(완료 후 얻을 수 있는 데이터셋)
- 오류에 대한 설명

* Elastic Beanstalk : 배포 자동화
-> ELB, EC2, 모니터링 등이 자동화
-> 소스 코드로만 동작하기 때문에 RDS, S3는 프로젝트에 미리 설정
-> 갱신되는 소스코드는 항상 새로 만들어진다

-> Git 기반으로 관리
1) 중요 정보가 노출될 수 있다. -> Heroku : 내부 repo에 업로드함
2) Elastic Beanstalk : Private Repository를 사용
- CodeCommit 이라는 서비스 (개인 전용 Git Hub라고 생각)
- Local Repository를 사용


1. Dstagram 만들기
2. Dstagram API 만들기
3. EB에 배포하기 - RDS 자동, 도메인 자동연결은 해주지 않는다.
- 이것을 하게 하려면 아마존 CLI를 이용하여 해야한다(공부해두면 좋음)


앱
1) photo : 사진 쓰레드 업로드
-Photo : author, image, text, created, updated
2) accounts : 회원 가입


"""