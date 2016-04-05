from django.contrib import admin

from quiz.models import Answer, Category, Question


# class AnswerAdmin(admin.ModelAdmin):
    # list_display('answer_text', 'source')


# class QuestionAdmin(admin.ModelAdmin):
    # list_display('question_text')

admin.site.register(Answer)
admin.site.register(Category)
admin.site.register(Question)
