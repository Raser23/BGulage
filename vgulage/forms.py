from django import forms
from django.utils.safestring import mark_safe


class RegForm(forms.Form):

    def is_valid(self):  # TODO: customize
        return super(RegForm, self).is_valid()

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(RegForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label="Логин",
                               widget=forms.TextInput(attrs={'class': 'form_field'}), max_length=100)

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_field'}),
                               label=mark_safe('<br />Пароль'), max_length=100)

    surname = forms.CharField(label=mark_safe('<br />Фамилия'),
                              widget=forms.TextInput(attrs={'class': 'form_field'}), max_length=100)

    name = forms.CharField(label=mark_safe('<br />Имя'),
                           widget=forms.TextInput(attrs={'class': 'form_field'}), max_length=100)

    second_name = forms.CharField(label=mark_safe('<br />Отчество'),
                                  widget=forms.TextInput(attrs={'class': 'form_field'}), max_length=100)

    date_of_birth = forms.DateField(label=mark_safe('<br />Дата рождения'),
                                    widget=forms.DateInput(attrs={'class': 'form_field'}))
