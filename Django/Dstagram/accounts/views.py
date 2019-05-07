from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
# 유저 목록이 출력되는 뷰
# + 기능 Follow라는 기능
# 중간 테이블을 직접 생성 - 모델

# 유저 모델을 커스터마이징 -> 1. 커스터마이징 하는 방법을 배워서
# 확장 하는 방법에 따라서
# 1) 새로운 유저 모델을 만드는 방법 - 기존 유저 데이터를 유지할 수가 없다.
# 2) 기존 모델을 확장 하는 방법 - DB 다운 타임 alter table - table lock
# 나 유저 모델
# 나를 팔로우한 사람 필드
# 내가 팔로우한 사람 필드

# 커스터마이징 할 수가 없다면?
# 새로운 모델을 추가하는 방법


# 사진 모델
# 사진을 좋아요한 사람 필드
# 사진을 저장한 사람 필드


"""
1. 유저 목록 혹은 유저 프로필에서 팔로우 버튼
1-1. 전체 유저 목록을 출력해주는 뷰 - User모델에 대한 ListView

2. 팔로우 정보를 저장하는 뷰
"""
from django.views.generic.list import ListView
from django.contrib.auth.models import User

class UserList(ListView):
    model = User
    template_name = 'accounts/user_list.html'
