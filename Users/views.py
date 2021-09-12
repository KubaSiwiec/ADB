from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        print('goog')
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print('good')
            # zapisuje formę
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can no log in')
            return redirect('register')
    else:
        print('bad')
        form = UserRegisterForm()
    return render(request, 'Users/register.html', {'form': form})

def profile(request):
    return render(request, 'users/profile.html')
