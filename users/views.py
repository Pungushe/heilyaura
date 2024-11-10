from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import auth,messages
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm

from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from orders.models import Order, OrderItem
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, "Вы успешно вошли в систему.")
                return HttpResponseRedirect(reverse('frontpage:product_list'))
            else:
                messages.error(request, "Неверное имя пользователя или пароль.")
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})
def registration(request):
     if request.method == 'POST':
          form = UserRegistrationForm(data=request.POST)

          if form.is_valid():
               form.save()
               user=form.instance
               auth.login(request, user)
               messages.success(request, f'{user.username}', 'Вы успешно зарегистрировались!')
               return HttpResponseRedirect(reverse('users:login'))
     else:
          form = UserRegistrationForm()
     return render(request, 'users/registration.html', {'form': form})
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user,
                           files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile was changed')
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
        
        orders = Order.objects.filter(user=request.user).prefetch_related(
        Prefetch(
            'items',
            queryset=OrderItem.objects.select_related('product'),
        )
    ).order_by('-id')
    return render(request, 'users/profile.html',
                  {'form': form,
                   'orders': orders})
     
def logout(request):
     auth.logout(request)
     return redirect(reverse('frontpage:product_list'))
