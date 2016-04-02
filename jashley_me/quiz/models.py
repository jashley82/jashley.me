from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    category = models.ForeignKey('Category', default=0)

    def __unicode__(self):
        return self.question_text


class Answer(models.Model):
    question = models.OneToOneField(
            'Question', 
            on_delete=models.CASCADE, 
            primary_key=True
            )
    answer_text = models.TextField()
    source = models.CharField(max_length=255)

    def __unicode__(self):
        return self.answer_text


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title
