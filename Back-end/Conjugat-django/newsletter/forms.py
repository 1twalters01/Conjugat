from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'placeholder':'Email'}))

class InfoForm(forms.Form):
    language_options = (
        ('English', 'English'),
        ('French', 'French'),
        ('Spanish', 'Spanish'),
        ('Italian', 'Italian'),
        ('Portuguese', 'Portuguese'),
        ('Other', 'Other'),
    )
    first_name = forms.CharField()
    last_name = forms.CharField()
    languages = forms.MultipleChoiceField(choices = language_options)