from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Question
from .serializers import QuestionSerializer


class QuestionListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
#    page = 1
#    page_query_param = 'page_number'
    max_page_size = 100

class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = QuestionListPagination

class QuestionCreate(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionUpdate(generics.RetrieveUpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


