from django import forms


class QuizForm(forms.Form):
   question_text = forms.CharField(label='Question', max_length=255)
   answer_id = forms.IntegerField(widget=forms.HiddenInput)
