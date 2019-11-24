from django import forms


class ExamForm(forms.Form):

    question = forms.CharField(label='問題', widget=forms.Textarea(attrs={'class': 'form-control'}))
    answer1 = forms.CharField(label='解答1', widget=forms.TextInput(attrs={'class': 'form-control'}))
    answer2 = forms.CharField(label='解答2', widget=forms.TextInput(attrs={'class': 'form-control'}))
    answer3 = forms.CharField(label='解答3', widget=forms.TextInput(attrs={'class': 'form-control'}))
    answer4 = forms.CharField(label='解答4', widget=forms.TextInput(attrs={'class': 'form-control'}))
    submit_button = forms