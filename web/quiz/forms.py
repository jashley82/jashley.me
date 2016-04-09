from django import forms


class QuizForm(forms.Form):
   answer_text = forms.CharField(label='Answer', max_length=255)
   question_id = forms.IntegerField(widget=forms.HiddenInput)
   time_completed = forms.CharField(widget=forms.HiddenInput)
