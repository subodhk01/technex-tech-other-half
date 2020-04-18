from django.urls import path
from . import views

urlpatterns = [
    path('index/<techid>', views.index, name="index"),
    path('about/<techid>', views.about),
    path('tandc/<techid>', views.tandc),
    path('end', views.end, name="end"),
    path('test_form', views.test_form),
    path('verify', views.verification),
    path('form/<key>', views.form, name='form'),
    path('clue/<techid>', views.clue, name="clue"),
    path('csv_subodhk/<gender>', views.customentry_csv)
]
