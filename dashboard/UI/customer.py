from django.shortcuts import render, HttpResponse, redirect
from django.http.response import JsonResponse
from domain.models import User, UserAddrsss
from django.contrib.auth.hashers import make_password

def add_customer(request):
   if request.method == "POST":
      try:
         customer =  User()
         customer.first_name = request.POST.get("frist_name",'').strip()
         customer.last_name = request.POST.get("last_name",'').strip()
         customer.email = request.POST.get("email",'').strip()
         customer.mobile_no = request.POST.get("mobile_no",'').strip()
         customer.date_joined = request.POST.get("date_joined",'').strip()
         customer.role = request.POST.get("role",'').strip()
         customer.password = make_password(request.POST.get("password",'').strip()) 
         customer.is_password_set =1
         customer.save()
         userdetails = UserAddrsss()
         userdetails.user = customer
         userdetails.address = request.POST.get("address",'').strip()
         userdetails.state = request.POST.get("state",'').strip()
         userdetails.city = request.POST.get("city",'').strip()
         userdetails.pincode = request.POST.get("pincode",'').strip()
         userdetails.save()
      except:
         pass
   else:
      print("It Else Part")
   return render(request, 'customers/add_customer.html')

def view_customer(request):
   user_data = User.objects.filter(role="Customer")
   
   context={
      'user_data':user_data,
     
   }
   return render(request, 'customers/list_customers.html',context)