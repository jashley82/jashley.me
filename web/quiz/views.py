from django.contrib import messages
from django.shortcuts import redirect, render

from quiz.forms import QuizForm
from quiz.models import Answer, Question


def do_quiz(request):
    question = Question.objects.order_by('?').first()
    if question: 
        form = QuizForm({'question_id': question.id})
    else:
        form = QuizForm()
    return render(request, 'quiz/do_quiz.html', {'question': question, 'form': form})
  
def check_answer(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            question = Question.objects.get(id = request.POST.get('question_id'))
            if request.POST.get('answer_text') == question.answer_set.first().answer_text:
                messages.add_message(request, messages.SUCCESS, 'Correct!')
            else:
                messages.add_message(request, messages.ERROR, 'Wrong!')
        else:
            pass
    return redirect('do_quiz')
