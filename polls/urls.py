from django.urls import path, include
from .views import questions, question
urlpatterns = [
  path('questions/', questions, name='question-list'),
  path('questions/<int:question_id>', question, name='question-detail')

]



def question_detail(question_id):
  pass


question_detail(3)
question_detail(question_id=3)