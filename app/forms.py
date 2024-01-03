from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'custom-email-class', 'placeholder': 'Enter your email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-username-class', 'placeholder': 'Enter your username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-password-class', 'placeholder': 'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-confirm-password-class', 'placeholder': 'Repeat your password'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-username-class', 'placeholder': 'Enter your username_or_email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-password-class', 'placeholder': 'Enter your password'}))

    
    #  def clean(self):
    #     username_or_email = self.cleaned_data.get('username_or_email')
    #     password = self.cleaned_data.get('password')

    #     # Check if the input is an email
    #     if '@' in username_or_email:
    #         # Try to get the user by email
    #         try:
    #             user = User.objects.get(email=username_or_email)
    #         except User.DoesNotExist:
    #             raise forms.ValidationError("Invalid login credentials")

    #         # Check if the password is valid for the user
    #         if not user.check_password(password):
    #             raise forms.ValidationError("Invalid login credentials")

    #     else:
    #         # If not an email, proceed with the default behavior (username)
    #         return super().clean()



