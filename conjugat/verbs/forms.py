from django import forms

class HomeForm(forms.Form):
    choices = [
        ('English', 'English'),
        ('French', 'French'),
        ('Italian', 'Italian'),
        ('Portuguese', 'Portuguese'),
        ('Spanish', 'Spanish')
    ]
    language = forms.ChoiceField(label='Test language', choices=choices)

class SingleTestForm(forms.Form):
    verb = forms.ChoiceField()