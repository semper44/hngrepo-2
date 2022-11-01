from rest_framework import generics
from .models import hngapi
from .serializers import PostSerializer

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset=hngapi.objects.all()
    serializer_class= PostSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset=hngapi.objects.all()
    serializer_class= PostSerializer
