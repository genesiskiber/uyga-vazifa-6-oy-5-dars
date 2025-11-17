from django.shortcuts import render, redirect
from .forms import CustomRegisterForm

def register(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomRegisterForm()
    return render(request, "accounts/register.html", {"form": form})

