from django.contrib import admin

from quiz.models import Answer, Category, Result, ScoreCard, Question


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_text', 'source')


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1
    can_delete = False


class ScoreCardInline(admin.TabularInline):
    model = ScoreCard
    extra = 0
    ordering = ('-created_at',)
    can_delete = False
    readonly_fields = ('answered_text', 'time_completed', 'pass_fail', 'user_id', 'created_at')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
            AnswerInline, 
            ScoreCardInline,
            ]


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    extra = 1
    inlines= [QuestionInline,]

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    inlines = [ScoreCardInline,]
