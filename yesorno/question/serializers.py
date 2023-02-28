from rest_framework import serializers

from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('text', 'choice_yes', 'choice_no')