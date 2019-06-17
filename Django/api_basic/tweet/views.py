from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from tweet.models import Tweet
from .permissons import *
from .serializers import ListSerializer, Serializer


# Create your views here.


# class ListView(generics.ListAPIView):
#     queryset = get_user_model().object.all()
#     serializer_class = ListSerializer
#

class TweetListCreateView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = ListSerializer
    search_fields = ('text', 'author__username')


    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user.id
        return super().create(request, *args, **kwargs)


class TweetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = Serializer
    # 권한 체크
    permission_classes = [IsAuthenticated, IsOwnerAndAdminOnly]
