from django.contrib import messages
from django.shortcuts import redirect, render

from quiz.forms import QuizForm
from quiz.models import Answer, ScoreCard, Question


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
            answered_text = request.POST.get('answer_text')
            time_completed = request.POST.get('time_completed')
            pass_fail = (answered_text == question.answer_set.first().answer_text)
            score_card = ScoreCard.objects.create(
                    question=question, 
                    answered_text=answered_text, 
                    time_completed=time_completed, 
                    pass_fail=pass_fail,
                    user_id=request.user.id
                    )
            msg = "{} {} {} {} {} {}"
            if pass_fail:
                messages.add_message(request, messages.SUCCESS, msg.format(
                    'Correct',
                    score_card.question.question_text,
                    score_card.question.answer_set.first().answer_text,
                    score_card.answered_text,
                    score_card.pass_fail,
                    score_card.count(question)
                    ))
            else:
                 messages.add_message(request, messages.ERROR, msg.format(
                    'Incorrect',
                    score_card.question.question_text,
                    score_card.question.answer_set.first().answer_text,
                    score_card.answered_text,
                    score_card.pass_fail,
                    score_card.count(question)
                    ))
    return redirect('do_quiz')
