from django.contrib import messages
from django.shortcuts import redirect, render

from quiz.forms import QuizForm
from quiz.models import Answer, Question


def do_quiz(request):
    answer = Answer.objects.order_by('?').first()
    if answer: 
        form = QuizForm({'answer_id': answer.id})
    else:
        form = QuizForm()
    return render(request, 'quiz/do_quiz.html', {'answer': answer, 'form': form})
  
def check_answer(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            answer = Answer.objects.get(id = request.POST.get('answer_id'))
            if request.POST.get('question_text') == answer.question.question_text:
                messages.add_message(request, messages.SUCCESS, 'Correct!')
            else:
                messages.add_message(request, messages.ERROR, 'Wrong!')
        else:
            pass
    return redirect('do_quiz')
