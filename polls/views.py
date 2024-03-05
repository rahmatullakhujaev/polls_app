from django.shortcuts import render, redirect
from .models import Questions, Answers


# Create your views here.
def questions(request):
    print(request.method)
    questions = Questions.objects.all()
    return render(request, 'question_list.html', {'qs': questions})


def question(request, question_id):
    print(request.method)
    vote_id = request.GET.get('vote')
    if vote_id:
        one_answer = Answers.objects.get(id=int(vote_id))
        one_answer.votes += 1
        one_answer.save()
        answer = Answers.objects.filter(question_id=question_id)
        question = Questions.objects.get(pk=question_id)

        context = {
            'answer': answer,
            'question': question,
            'is_voted': True
        }
        return render(request, 'question.html', context)

    answer = Answers.objects.filter(question_id=question_id)
    question = Questions.objects.get(pk=question_id)

    context = {
        'answer': answer,
        'question': question,
        'is_voted': False
    }
    return render(request, 'question.html', context)
