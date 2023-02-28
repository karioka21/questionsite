from django.shortcuts import render
from rest_framework import generics

from .models import Question
from .serializers import QuestionSerializer


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


