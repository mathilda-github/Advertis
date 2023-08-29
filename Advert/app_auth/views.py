from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import RegisterationForm
from django.views.generic import CreateView

@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    if request.user.is_authenticated:
        user_profile = request.user.is_authenticated
    return render(request, 'app_auth/profile.html', {'user_profile': user_profile})


def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('profile'))
        user_profile = False
        return render(request, 'app_auth/login.html', {'user_profile': user_profile})

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('profile'))
    return render(request, 'app_auth/login.html', {'error': 'Пользователь не найден!'})

def logout_view(request):
    logout(request)
    user_profile = False
    return render(request, 'app_auth/login.html', {'user_profile': user_profile})

@login_required(login_url=reverse_lazy('main_page'))
def register_view(request):
    class SignUp(CreateView):
        form_class = RegisterationForm()
#        success_url = reverse_lazy('main_page')
        template_name = 'app_auth/regoster.html'
    form = RegisterationForm()
    return render(request, 'app_auth/register.html', {'form':form})




