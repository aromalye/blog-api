from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
# Create your views here.

class BlogList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer