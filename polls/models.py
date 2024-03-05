from django.db import models

# Create your models here.
class Questions(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
class Answers(models.Model):
    answer = models.CharField(max_length=30)
    question = models.ForeignKey(Questions, on_delete= models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.answer
