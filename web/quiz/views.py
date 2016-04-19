import django_rq
import random

from django.contrib import messages
from django.shortcuts import redirect, render

from quiz.forms import QuizForm
from quiz.models import Answer, Category, Result, ScoreCard, Question


def select_category(request):
    categories = Category.objects.all()
    return render(request, 'quiz/select_category.html', {'categories':  categories})

def set_category(request, category_id):
    "populates redis queue with question set"
    result = Result.objects.create(category_id=category_id, user=request.user)
    game_id = str(result.game_id)
    queue = django_rq.get_queue('quiz') # TODO: dynamic queue creation 
    queue.empty() 
    for question in Question.objects.filter(category_id=category_id): 
        queue.enqueue(str(question.id))
    return redirect('do_quiz', game_id=game_id)

def do_quiz(request, game_id):
    "cycles through queue displaying questions or redirects to results view"
    queue = django_rq.get_queue('quiz')
    queue.jobs # bug that prevents is_empty from returning true 
               # unless the jobs member is accessed first
    if queue.is_empty(): 
        return redirect('results', game_id=game_id)
    job = random.choice(queue.jobs) 
    question_id = job.func_name
    job.delete()
    form = QuizForm({'question_id': question_id})
    question = Question.objects.get(id=question_id)
    return render(request, 'quiz/do_quiz.html', {'question': question, 'form': form, 'game_id': game_id})
  
def check_answer(request, game_id):
    if request.method == 'POST':
        result = Result.objects.get(game_id=game_id)
        form = QuizForm(request.POST)
        if form.is_valid():
            question = Question.objects.get(id=request.POST.get('question_id'))
            answered_text = request.POST.get('answer_text')
            time_completed = request.POST.get('time_completed')
            pass_fail = (answered_text == question.answer_set.first().answer_text)
            score_card = ScoreCard.objects.create(
                    question=question, 
                    answered_text=answered_text, 
                    time_completed=time_completed, 
                    pass_fail=pass_fail,
                    user_id=request.user.id,
                    result=result
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
    return redirect('do_quiz', game_id=game_id)

def results(request, game_id):
    "displays results of completed quiz scorecards"
    result = Result.objects.get(game_id=game_id)
    score_cards = result.scorecard_set.all()
    return render(request, 'quiz/results.html', {'result': result, 'score_cards': score_cards})
