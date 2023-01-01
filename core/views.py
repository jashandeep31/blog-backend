from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import mixins
from .serializers import BlogSerializer
from .models import Blog


class BlogViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "slug"
