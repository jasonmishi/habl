from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import SignUpForm


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})
