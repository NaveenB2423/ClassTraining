from django.shortcuts import render, HttpResponse
from domain.models import Product, ProductVariant, Cart, Color, Size
from domain.models import MainMenus, SubMenus, User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout


# Create your views here.
# def index(request):
#     print(request.user.id)
#     product = Product.objects.filter(status=1).last()
#     if request.method == 'POST':
#         product_id = request.POST.get('product_id')
#         size_name = request.POST.get('size')
        
#         color_name =request.POST.get('color')
       
#         qty =request.POST.get('qty')
#         size = Size.objects.get(name=size_name,status=1)
#         color = Color.objects.get(name=color_name,status=1)
#         productVariant = ProductVariant.objects.get(product_id=product_id, size=size, color=color)
#         cart = Cart()
#         cart.made_by=request.user
#         cart.variant=productVariant
#         cart.qty = qty
#         cart.save()
#     return render(request, 'home/index.html')   
#     return render(request,'home/index.html',{'product':product})
def index(request):
    menus = MainMenus.objects.filter(status=1).order_by('priority')
    return render(request, 'home/index.html',{'menus':menus,'current_url':'index'})  

def main_products(request,menu):
    
    original_menu = menu.replace("-"," ")
    products = Product.objects.filter(main_menu__name__iexact='tshirt')
  
    return render(request,'home/selected-products.html',{'current_url':menu,'products':products}) 
def sub_products(request,main_menu,sub_menu):
    original_menu = main_menu.replace("-"," ")
    original_sub_menu = sub_menu.replace("-"," ")
    products = Product.objects.filter(main_menu__name__iexact=original_menu,sub_menu__name__iexact=original_sub_menu)
    return render(request,'home/selected-products.html',{'current_url':main_menu,'products':products}) 

def about_us(request):
    return render(request,'home/about.html')
def contact_us(request):
    return render(request,'home/contact.html')
def customer_login(request):

    if request.method == 'POST':
        mobile = request.POST.get('mobile', '')
        password = request.POST.get('password', '')
        
        user = authenticate(request,mobile_no=mobile, password=password)
        print(user)
        
        if user and user.is_active:
            login(request, user)
            return HttpResponse("Logged in")
        else:
            return HttpResponse('failed')


    return render(request,'home/login.html')
def customer_signup(request):
    if request.method == 'POST':
       new_user =  User()
       new_user.first_name = request.POST.get('firstname','').strip()
       new_user.mobile_no = request.POST.get('mobile','').strip()
       new_user.email = request.POST.get('email','').strip()
       new_user.password = make_password(request.POST.get('password','').strip())
       new_user.is_password_set =1
       new_user.save()

    return render(request,'home/signup.html')
def products(request):
    return render(request,'home/product.html')
def product_details(request,name):
    original_name = name.replace("-"," ")
    product = Product.objects.filter(name__iexact=original_name).last()
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        size_name = request.POST.get('size')
        
        color_name =request.POST.get('color')
       
        qty =request.POST.get('qty')
        size = Size.objects.get(name=size_name,status=1)
        color = Color.objects.get(name=color_name,status=1)
        productVariant = ProductVariant.objects.get(product_id=product_id, size=size, color=color)
        cart = Cart()
        cart.made_by=request.user
        cart.variant=productVariant
        cart.qty = qty
        cart.save()
    return render(request,'home/product-details.html',{'product':product})
def shopping_cart(request):
    carts = Cart.objects.filter(made_by=request.user)
    return render(request,'home/shopping-cart.html',{'carts':carts})
def blog(request):
    return render(request,'home/blog.html')
def blog_details(request):
    return render(request,'home/blog-details.html')

def cart(request):
    carts = Cart.objects.filter(made_by=request.user)
    return render(request,'home/cart.html',{'carts':carts})
