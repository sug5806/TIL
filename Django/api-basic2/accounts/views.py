from rest_framework import generics
from .serializers import *

# Create your views here.

class AccountLCAPI(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = Account