from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
     def clean(self):
        username_or_email = self.cleaned_data.get('username_or_email')
        password = self.cleaned_data.get('password')

        # Check if the input is an email
        if '@' in username_or_email:
            # Try to get the user by email
            try:
                user = User.objects.get(email=username_or_email)
            except User.DoesNotExist:
                raise forms.ValidationError("Invalid login credentials")

            # Check if the password is valid for the user
            if not user.check_password(password):
                raise forms.ValidationError("Invalid login credentials")

        else:
            # If not an email, proceed with the default behavior (username)
            return super().clean()



