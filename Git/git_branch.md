---
title: 2019-04-10 Git 특강2 branch
date: 2019-04-10 18:32:46
subtitle : Git
categories:
 - Git
tags:
 - Git
 - branch
---

# Git

### 브랜치란?
* 분기점을 생성하고 독립적으로 코드를 변경할 수 있도록 도와주는 모델
* Ex) 
  * matser branch
    ```python
    print("hellow python!")
    ```
  * another branch
    ```python
    for i in  range(1,10):
        print('hello world for the %s times!" % i)
    ```   

* 로컬의 branch와 리모트의 branch는 따로 존재한다
* git branch -r : 리모트의 브랜치를 조회한다
* git branch : 로컬의 브랜치를 조회한다


#### 브랜치 생성
* git branch feat/loop -> feat/loop라는 새로운 브랜치를 만든다
  *  **현재 브랜치**의 현재 상태 그대로 복제하여 만든다

#### 브랜치 이동
* git checkout feat/loop -> feat/loop 브랜치로 이동한다.

#### 리모트 레포와 동기화
* git push -u origin feat/loop : 리모트 레포에 feat/loop라는 새로운 브랜치 생성
  * -u : upstream의 약자 -> 리모트 레포에 feat/loop가 없으므로 해주어야 한다.


 ```text
 브랜치를 해도 deletion이 없으면 평행으로 되고 있으면 밑으로 추가되고, 우리가 논리적으로 생각하는 것으로 그림을 그린다.
 ```

#### 브랜치 병합하기
1. 우선 병합하고자 하는 브랜치로 이동한다 -> git checkout feat/loop
2. git merge feat/con-state : feat/loop를 feat/con-state의 내용과 동기화시킨다(feat/con-state와 같아진다)
3. 자동으로 commit이 생긴다.

#### 브랜치 삭제하기
* git branch -D/d 브랜치명
  * D는 강제로 삭제한다


```text
Master 브랜치는 사용자에게 보여지기 때문에  개발자는 develop이라는 브랜치를 따로 만든다.
```

#### 브랜치및 머지를 보다 쉽게 하기
* git flow 전략 : [다운로드 링크](https://danielkummer.github.io/git-flow-cheatsheet/index.ko_KR.html)
  * master는 항상 개발이 끝난 것만 보여야한다
 ![](https://camo.githubusercontent.com/075a231fca71d6a23491041230f3a265671e3a36/68747470733a2f2f64616e69656c6b756d6d65722e6769746875622e696f2f6769742d666c6f772d636865617473686565742f696d672f6769742d666c6f772d636f6d6d616e64732e706e67)
* git init -> git flow init : git init을 하면서 flow까지 한꺼번에 함
* develop 브랜치를 만들어도 기능 개발을 할때는 브랜치를 또 만들어서 해야한다 

* git flow feature start Name : Name의 브랜치를 생성하고 checkout 한다
   * 자식 브랜치를 만들고나서 파일을 수정하고 꼭 commit을 해야 가지가 쳐진다.

* git flow feature finish Name : Name의 브랜치를 상위 브랜치와 merge하고 Name의 브랜치는 삭제 한다(**remote와 local에서 같이 지운다**)
