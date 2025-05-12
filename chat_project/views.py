from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate

def user_signup(request):
      if request.method == 'POST':
          form = SignUpForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('login')
      else:
          form = SignUpForm()
      return render(request, 'signup.html', {'form': form})

def user_login(request):
      if request.method == 'POST':
          form = LoginForm(data=request.POST)
          if form.is_valid():
              user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
              if user is not None:
                  login(request, user)
                  return redirect('chat_page')
      else:
          form = LoginForm()
      return render(request, 'login.html', {'form': form})


def chat_page(request):
    return render(request, 'wellcome.html')