from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django.urls import reverse



@admin.register(Clue)
class ClueAdmin(admin.ModelAdmin):
    list_display = ('id', 'label', 'state', 'form')
    fields = ('id', 'label', 'state', 'form')
    list_display_links = ()

@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'half1', 'half2', 'clue1', 'clue2', 'clue3', 'clue4', 'clue5', 'clue6', 'clue7')
    fields = ('id', 'half1', 'half2', 'clue1', 'clue2', 'clue3', 'clue4', 'clue5', 'clue6', 'clue7')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('clue', 'source', 'label')

@admin.register(Question)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('qid','qno','qtype','label', 'option1', 'option2', 'option3', 'option4', 'option5','question_first', 'question_last')
    fields = (('qid', 'qno','qtype'),('label'), ('option1', 'option2'),('option1image', 'option2image'),( 'option3', 'option4'), ('option5'),('question_first', 'question_last'))

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = (
        'technexid', 
        'name', 
        'gender', 
        'year', 
        'ques1',
        'ques2',
        'ques3',
        'ques4',
        'ques5',
        'ques6',
        'ques7',
        'ques8',
        'ques9',
        'ques10',
        'ques11',
        'ques12',
        'ques13',
        'ques14',
        'ques15',
        'ques16',
        'ques17',
        'ques18',
        'ques19',
        'ques20',
        'ques21',
        'ques22',
        'ques23',
        'ques24',
        'ques25',
        'ques26',
        'ques27',
        'ques28',
        'ques29',
        'ques30',
        'submitted'
        )

@admin.register(CustomEntry)
class CustomEntryAdmin(admin.ModelAdmin):
    list_display = (
        'technexid', 
        'name', 
        'gender', 
        'year', 
        'ques1',
        'ques2',
        'ques3',
        'ques4',
        'ques5',
        'ques6',
        'ques7',
        'ques8',
        'ques9',
        'ques10',
        'ques11',
        'ques12',
        'ques13',
        'ques14',
        'ques15',
        'ques16',
        'ques17',
        'ques18',
        'ques19',
        'ques20',
        'ques21',
        'ques22',
        'ques23',
        'ques24',
        'ques25',
        'ques26',
        'ques27',
        'ques28',
        'ques29',
        'ques30',
        'submitted'
        )

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        'technexid','name','gender','year','college','email','phone','city'
    )
    search_fields = (
        'technexid','name','gender','year','college','email','phone','city'
    )