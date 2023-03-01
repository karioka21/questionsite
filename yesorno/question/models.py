from django.db import models
from django.urls import reverse

from question.utils import h_encode


class Question(models.Model):
    question = models.CharField(max_length=200, null=True)
    answer_yes = models.CharField(max_length=25, null=True)
    answer_no = models.CharField(max_length=25, null=True)
    time_create = models.DateTimeField(auto_now_add=True, null=True)

#добавить время жизни

    def __str__(self):
        return self.question

    def get_hashid(self):
        return h_encode(self.pk)

    def get_absolute_url(self):
        return reverse('question', kwargs={'question_id': self.pk})

