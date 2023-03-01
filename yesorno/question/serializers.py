from rest_framework import serializers

from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('pk', 'question_text', 'answer_yes', 'answer_no')