from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserSignupForm

def home(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirects to homepage after signup
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})
