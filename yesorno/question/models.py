from django.db import models
from django.urls import reverse



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_yes = models.CharField(max_length=25)
    answer_no = models.CharField(max_length=25)
    time_create = models.DateTimeField(auto_now_add=True)

#добавить время жизни

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse('question', kwargs={'question_id': self.pk})

