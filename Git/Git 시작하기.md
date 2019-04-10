---
title: 2019-04-03 Git 특강1 Init
date: 2019-04-03 18:32:46
subtitle : Git
categories:
 - Git
tags:
 - Git
 - Init
---


### Init으로 시작하는 방법

레포 이름과 폴더 이름이랑 같지 않으면 나중에 헷갈릴수 있으므로 똑같이 하는게 좋다

1. 본인의 git 저장소로 쓰고싶은 로컬 디렉토리로 이동 한다음 git init을 한다
2. git config --global user.name "username"을 입력한다
3. git config --global user.email "email"을 입력한다
    * git 설정을 할때 git config --global을 하면 전체에 설정이 되고 global을 빼면 해당 레포?에서만 지정이 된다.
4.  git remote 
    * get-url 별명 : 별명이 가지고 있는 주소를 알 수 있다
    * 별명 주소 : 별명으로 주소의 리모트 레포를 이용 하겠다 반드시 별명이 있어야 함
5. git add 
6. commit을 할때는 동작을 하는 코드만 commit을 해야한다
    * -u를 붙임으로써 같은 브랜치라고 알려준다(브랜치 당  최초 1번만 하면 된다) 
        * (git commit -u 별명 master)
    * commit을 할때 기능에 따른 말머리를 추가하는것이 좋다
    * commit 메시지를 작성할때는 현재형으로 작성하는것이 좋다
    * commit 메시지를 적을때는 제목으로 무엇을 변경했는지 알아볼수 있게 작성하는게 좋다
    * collection (list, dictionary, tuple 등)을 사용할때는 나열식으로 하는것 보다는 값마다 한줄 한줄씩 하는게 좋다
    * collection을 사용할때는 마지막 원소에 ,(콤마)를 적어주면 깃에서 추가된 내용만 추가가 된다.

---

### Clone으로 시작하는 방법

1. 레포로 사용하고싶은 디렉토리로 이동한다음 git clone "github 주소"를 하면 자동으로 복사를 해서 만들어 준다.

---

private은 무료이나 통계기능이 잠겨있다 -> 돈을 내고 사용해야 풀림

gitignore : 무시하고 싶을때 포함하고 싶은 파일 확장자를 입력하면 push를 할때 깃에 올라가지 않게된다

index가 있으므로써 commit을 개별로 할 수 있고 local repo가 있으므로 offline 개발이 가능해진다
