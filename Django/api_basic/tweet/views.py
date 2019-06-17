from django.contrib.auth import get_user_model
from rest_framework import generics

from tweet.models import Tweet
from .serializers import ListSerializer, Serializer

from .permissons import *

# Create your views here.


# class ListView(generics.ListAPIView):
#     queryset = get_user_model().object.all()
#     serializer_class = ListSerializer
#

class TweetListCreateView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = ListSerializer

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user.id
        return super().create(request, *args, **kwargs)


class TweetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = Serializer
    # 권한 체크
    permission_classes = [IsOwnerAndAdminOnly]

