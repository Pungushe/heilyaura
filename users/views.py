from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from .forms import UserLoginForm

def login(request):
     if request.method == 'POST':
          form = UserLoginForm(data=request.POST)
          
          if form.is_valid():
               username = request.POST['username']
               password = request.POST['password']
               user = auth.authenticate(username=username, password=password)
               
               if user:
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse('frontpage:product'))
     else:
          form = UserLoginForm()
     return render(request, 'users/login.html', {'form': form})
def registration(request):
     return render(request, 'users/registration.html')
def profile(request):
     return render(request, 'users/profile.html')
def logout(request):
     pass
