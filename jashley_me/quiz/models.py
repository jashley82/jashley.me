from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=255)

    def __unicode__(self):
        return self.question_text


class Answer(models.Model):
    category = models.ForeignKey('Category')
    question = models.ForeignKey('Question')
    answer_text = models.TextField()
    source = models.CharField(max_length=255)

    def __unicode__(self):
        return self.answer_text


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title
