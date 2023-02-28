from django.db import models
from django.urls import reverse

from question.utils import h_encode


class Question(models.Model):
    text = models.CharField(max_length=255)
    choice_yes = models.CharField(max_length=255)
    choice_no = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)

#добавить время жизни

    def __str__(self):
        return self.text

    def get_hashid(self):
        return h_encode(self.id)

    def get_absolute_url(self):
        return reverse('question', kwargs={'question_id': self.pk})

