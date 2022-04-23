import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class usuarios(models.Model):
    usuario = models.CharField(max_length=200)
    contrasena = models.CharField(max_length=200)
    email_user = models.CharField(max_length=300, default='corre@hotmail.com')
    sexo = models.CharField(max_length=200, default='no llenado')
    edad = models.IntegerField(default=0)

    def __str__(self):
        return self.usuario + '-' + self.contrasena