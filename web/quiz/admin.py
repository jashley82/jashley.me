from django.contrib import admin

from quiz.models import Answer, Category, ScoreCard, Question


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


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline, ScoreCardInline,]


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)
