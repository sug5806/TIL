from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'
urlpatterns = [
    # views에서 클래스를 만들지않고 이렇게 연결할 수 있다.
    path('signin/', LoginView.as_view(template_name='accounts/signin.html'), name='signin'),
    path('signout/', LogoutView.as_view(template_name='accounts/signout.html'), name='signout'),
]