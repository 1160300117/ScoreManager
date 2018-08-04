from django import forms

class AddForm(forms.Form):
    key = forms.CharField()

class ChangeForm(forms.Form):
    key = forms.CharField()

class DeleteForm(forms.Form):
    key = forms.CharField()

class SearchStudentForm(forms.Form):
    key = forms.CharField(max_length = 20) 

class SearchScoreForm(forms.Form):
    key = forms.FloatField()

class SearchSubjectForm(forms.Form):
    key = forms.CharField(max_length = 20)