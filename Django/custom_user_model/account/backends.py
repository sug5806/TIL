from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomeUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(request, username, password, **kwargs)

        if user:
            return user

        # id 로그인 실패 상황
        # email 로그인 시도
        UserModel = get_user_model()
        # 원래 id 로그인 처리를 할때 username이 넘어왔을경우
        # email 변수에 새로 값을 할당하려
        email = username
        if email is None:
            email = kwargs.get(UserModel.EMAIL_FIELD, kwargs.get('email'))
        try:
            user = UserModel._default_manager.get(email=email)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).고
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user


"""
과제 : 기본 프로젝트
1. 프로젝트 만들기
2. RDS - POSTgreSQL
3. S3 - 2 bucket - domain
4. Custom user Model - backend 적용
5. debug too bar, djano extenstions
6. pip freeze > requirements.txt
"""