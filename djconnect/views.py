from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import SignUpForm, EditUserInfos
from django.contrib.auth.forms import PasswordChangeForm


@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return render(request, 'djconnect/login.html', {})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('djconnect:dashboard')
    else:
        form = SignUpForm()
    return render(request, 'djconnect/registration.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('djconnect:dashboard')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'djconnect/login.html', {})

@login_required
def dashboard(request):
    if request.method == 'POST':
        edit_form = EditUserInfos(request.POST,instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('djconnect:dashboard')
        else:
            return HttpResponse('Nope')
    else:
        edit_form = EditUserInfos()
        return render(request, 'djconnect/dashboard2.html', {'edit_form':edit_form})

@login_required
def dashboard_security(request):
    if request.method == 'POST':
        edit_password_form = PasswordChangeForm(request.user, request.POST)
        if edit_password_form.is_valid():
            user = edit_password_form.save()
            update_session_auth_hash(request, user)
            return redirect('djconnect:dashboard_security')
        else:
            return redirect('djconnect:dashboard_security')
    else:
        edit_password_form = PasswordChangeForm(request.user)
        return render(request, 'djconnect/dashboard_security2.html', {'edit_password_form': edit_password_form,})

