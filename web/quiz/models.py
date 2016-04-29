from uuidfield import UUIDField

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    category = models.ForeignKey('Category', default=0)

    def __unicode__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey('Question', default=0)
    answer_text = models.CharField(max_length=255)
    source = models.CharField(max_length=255)

    def __unicode__(self):
        return self.answer_text


class ScoreCard(models.Model):
    question = models.ForeignKey('Question')
    result = models.ForeignKey('Result')
    user_id = models.IntegerField()
    answered_text = models.CharField(max_length=255)
    time_completed = models.CharField(max_length=255)
    pass_fail = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    
    def count(self, obj):
        return ScoreCard.objects.filter(question=obj).count()


class Result(models.Model):
    category = models.ForeignKey('Category')
    created_at = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=255)
    game_id = UUIDField(auto=True)

    def __unicode__(self):
        return str(self.game_id)
