---
title: 2019-04-10 reguler-expression
date: 2019-04-10 15:23:46
subtitle : reguler-expression
categories:
 - reguler-expression
tags:
 - reguler-expression
  
---


# 정규 표현식
* r`[] -> row string(파이썬에서만 쓰임)
  * [a-z] : a~z까지

Match -> 문자열의 처음부터 찾고 안맞으면 False
Search -> 문자열 중에서 하나라도 있으면 return

* 반복
  1. \* : 0 ~ 무한대 -> {0, 무한대}
  2. \+ : 1 ~ 무한대 -> {1, 무한대}
  3. ? : 0 ~ 1 -> {0, 1}
  4. {m} : m개
  5. {m,n} : m개부터 n개까지

* ^
    1. 일반적인 경우 문자열의 시작
    2. [^abc] : a,b,c가 모두 아닌 모든 문자열 

* $
    1. 일반적인 경우 문자열의 끝

* . 
  * 일반적으로는 모든 문자들 나타냄
  
* r
  * r' '안에 있으면 모든 특수문자들이 효력을 잃음


* 특수문자 
  * \\ : \
  * \d : [0-9]
  * \D : [^0-9]
  * \s(white space) : \t, \n, space, \r 
  * \S : not white space
  * \w : [a-zA-Z0-9]
  * \W : [^a-zA-Z0-9]


* Group
  * pattern = r'([0-9]{3})[-./ ]*(\d{3,4})[-./ ]*(\d{4})'
  * 그룹을 3개로 나눔
   
    
---

Ex) 변수할당 구분하기
  * r'([a-zA-Z_]\w*)\s*=\s*([0-9]+)'