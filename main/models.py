from django.db import models
from .models import *

class Clue(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    label = models.CharField(max_length=500)
    state = models.BooleanField()
    form = models.BooleanField(default=0)

    def __str__(self):
        return str(self.id)+ ". " + str(self.label)

class Winner(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    half1 = models.ForeignKey('Participant', on_delete=models.SET_NULL, null=True, related_name='half1')
    half2 = models.ForeignKey('Participant', on_delete=models.SET_NULL, null=True, related_name='half2')
    clue1 = models.BooleanField()
    clue2 = models.BooleanField()
    clue3 = models.BooleanField()
    clue4 = models.BooleanField()
    clue5 = models.BooleanField()
    clue6 = models.BooleanField()
    clue7 = models.BooleanField()

    def __str__(self):
        return str(self.half1) + " :: " + str(self.half2)

class Answer(models.Model):
    clue = models.ForeignKey('Clue', on_delete=models.SET_NULL, null=True)
    source = models.ForeignKey('Winner', on_delete=models.SET_NULL, null=True)
    label = models.CharField(max_length=100)


class Question(models.Model):
    qid = models.CharField(max_length=10)
    qno = models.IntegerField(null=True)
    qtype = models.CharField(max_length=10, choices=(('mcq','mcq'),('rapidfire','rapidfire')), default="mcq")
    label = models.TextField(blank=True)
    option1 = models.CharField(max_length=70, null=True, blank=True, default=None)
    option2 = models.CharField(max_length=70, null=True, blank=True, default=None)
    option3 = models.CharField(max_length=70, null=True, blank=True, default=None)
    option4 = models.CharField(max_length=70, null=True, blank=True, default=None)
    option5 = models.CharField(max_length=70, null=True, blank=True, default=None)
    option1image = models.ImageField(upload_to="images", null=True, blank=True)
    option2image = models.ImageField(upload_to="images", null=True, blank=True)
    question_first = models.BooleanField(default=False)
    question_last = models.BooleanField(default=False)

    def __str__(self):
        return str(self.qno) + ". " +(self.label)

class Entry(models.Model):
    technexid = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30)
    year = models.IntegerField()
    gender = models.CharField(max_length=10)
    ques1 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques2 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques3 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques4 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques5 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques6 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques7 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques8 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques9 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques10 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques11 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques12 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques13 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques14 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques15 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques16 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques17 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques18 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques19 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques20 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques21 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques22 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques23 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques24 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques25 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques26 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques27 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques28 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques29 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques30 = models.CharField(max_length=70, null=True, blank=True, default=None)
    submitted = models.BooleanField(default=0)

    def __str__(self):
        return str(self.technexid)

class CustomEntry(models.Model):
    technexid = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30)
    year = models.IntegerField()
    gender = models.CharField(max_length=10)
    ques1 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques2 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques3 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques4 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques5 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques6 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques7 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques8 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques9 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques10 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques11 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques12 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques13 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques14 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques15 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques16 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques17 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques18 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques19 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques20 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques21 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques22 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques23 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques24 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques25 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques26 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques27 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques28 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques29 = models.CharField(max_length=70, null=True, blank=True, default=None)
    ques30 = models.CharField(max_length=70, null=True, blank=True, default=None)
    submitted = models.BooleanField(default=0)

    def __str__(self):
        return str(self.technexid)

class Participant(models.Model):
    technexid = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    college = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name) + " : " + str(self.technexid)  



