from django.shortcuts import render, redirect
from django.conf import settings
from accounts.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    if request.method=="POST":
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        forms=UserCreationForm()
    return render(request,'accounts/signup.html',{'forms':forms})