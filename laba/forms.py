from django import forms
from django.contrib.auth.forms import UsernameField, AuthenticationForm
from django_registration.forms import RegistrationForm
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last_name', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-input'}),
            'text': forms.Textarea(attrs={'placeholder': 'Text', 'class': 'form-textarea'}),
            'request': forms.Select(choices=[
                'One',
                'Two',
            ], attrs={'class': 'form-input'}),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'placeholder': 'Username'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}))


# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = '__all__'
#         widgets = {
#             'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-input'}),
#             'last_name': forms.TextInput(attrs={'placeholder': 'Last_name', 'class': 'form-input'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-input'}),
#             'text': forms.Textarea(attrs={'placeholder': 'Text', 'class': 'form-textarea'}),
#             'request': forms.Select(choices=[
#                 'One',
#                 'Two',
#             ], attrs={'class': 'form-input'}),
#         }