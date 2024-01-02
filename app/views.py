from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

# home
def index(request):
    return render(request, 'base.html')


@login_required
# logout
def custom_logout(request):
    logout(request)
    return redirect('user_login')



@login_required
# dashboard
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

@login_required
# profile
def profile(request):
    return render(request, 'profile.html', {'user': request.user})


# registration/sign-up
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


# Login 
class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'registration/login.html'