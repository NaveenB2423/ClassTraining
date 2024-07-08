from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages





def admin_login(request):
    if request.method == 'POST':
        mobile_no = request.POST.get('mobile_no', '')
        password = request.POST.get('password', '')
        user = authenticate(request,mobile_no=mobile_no, password=password)
        print(user)
        if user and user.is_active:
            login(request, user) 
            return redirect(dashboard)
        else:
            return render(request, 'admin_page/login.html', {'message' : "Invalid Credentials"})
    return render(request, 'admin_page/login.html')


def dashboard(request):
    return render(request,'forms.html')

