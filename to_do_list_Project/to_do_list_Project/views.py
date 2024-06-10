from django.shortcuts import render,redirect
from to_do_list_App.models import *
from to_do_list_Project.forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def signupPage(request):
    if request.method=='POST':
        signupform=to_do_list_form(request.POST, request.FILES)
        if signupform.is_valid():
            signupform.save()
            return redirect('signinPage')
    else:
        signupform=to_do_list_form()
    return render(request,'common/signupPage.html',{'signupform':signupform})



def signinPage(request):
    if request.method=='POST':
        signinform=to_do_list_auth_form(request,data=request.POST)
        if signinform.is_valid():
            user=signinform.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        signinform=to_do_list_auth_form()

    return render(request,'common/signinPage.html',{'signinform':signinform})

@login_required
def dashboard(request):
    return render(request,'common/dashboard.html')

@login_required
def logoutPage(request):
    logout(request)
    return redirect('signinPage')