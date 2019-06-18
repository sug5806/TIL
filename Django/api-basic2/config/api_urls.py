from django.urls import path
from photo.views import *
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken.views import obtain_auth_token

schema_view = get_swagger_view('title=Dstagram API Document')

app_name = 'api'

urlpatterns = [
    path('list/', PhotoListAPI.as_view()),
    path('create/', PhotoCreateAPI.as_view()),
    path('detail/<int:pk>/', PhotoDetailAPI.as_view()),
    path('update/<int:pk>/', PhotoUpdateAPI.as_view()),
    path('doc/', schema_view),
    path('get_token/', obtain_auth_token),
]