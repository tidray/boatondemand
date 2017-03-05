from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from boatondemandapp.forms import UserForm, ManagerForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return redirect(manager_home)

@login_required(login_url='/manager/sign-in/')
def manager_home(request):
    return render(request, 'manager/home.html')

def manager_sign_up(request):
    user_form = UserForm()
    manager_form = ManagerForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        manager_form = ManagerForm(request.POST, request.FILES)

        if user_form.is_valid() and manager_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_manager = manager_form.save(commit=False)
            new_manager.user = new_user
            new_manager.save()

            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]

            ))

            return redirect(manager_home)


        return render(request, "manager/sign_up.html", {
                "user_form": user_form,
                "manager_form": manager_form
            })
