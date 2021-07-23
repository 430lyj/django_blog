from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import SignupForm

# Create your views here.
def login_view(request):
  if request.method == 'POST': #더블 체크를 위해서
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = auth.authenticate(
        request=request,
        username=username,
        password=password
      )

      if user is not None: #유저가 존재하면
        auth.login(request, user)
        return redirect('home')

    return redirect('account:login')
  
  else:
    form = AuthenticationForm()
    return render(request, 'login.html', {'form' : form})

def logout(request):
    auth.logout(request)
    return redirect('home')

from .forms import SignupForm # 이 부분 추가

def signup_view(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth.login(request, user)
      return redirect('home')
    return redirect('account:signup')

  else:
    form = SignupForm()
    return render(request, 'signup.html', {'form' : form})