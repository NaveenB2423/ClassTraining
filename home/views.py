from django.shortcuts import redirect, render, HttpResponse
from domain.models import Product, ProductVariant, Cart, Color, Size
from domain.models import MainMenus, SubMenus, User,Customizedesgin,Image
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum


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
    image = Image.objects.filter(describe = "Printed T-Shits")
    women_image = Image.objects.filter(describe = "For Women")
    men_image = Image.objects.filter(describe = "For Men")
    context ={
        'menus':menus,
        'image':image,
        'women_image':women_image,
        'men_image':men_image
    }
    return render(request, 'home/index.html',context)  

def main_products(request, menu):
    original_menu = menu.replace("-", " ")
    products = Product.objects.filter(main_menu__name__iexact=menu)
    if not products.exists():
        # Handle the case where no products are found
        return HttpResponse(f"No products found for {original_menu}")
    return render(request, 'home/selected-products.html', {'current_url': menu, 'products': products})

def sub_products(request, main_menu, sub_menu):
    original_menu = main_menu.replace("-", " ")
    original_sub_menu = sub_menu.replace("-", " ")
    products = Product.objects.filter(main_menu__name__iexact=original_menu, sub_menu__name__iexact=original_sub_menu)
    if not products.exists():
        # Handle the case where no products are found
        return HttpResponse(f"No products found for {original_menu}")
    return render(request, 'home/selected-products.html', {'current_url': main_menu, 'products': products})

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
            return redirect(index)
        else:
            return HttpResponse('failed')


    return render(request,'home/login.html')

def customer_logout(request):
    logout(request)
    return redirect('/')

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
    products = Product.objects.all()
    distinct_sizes = Size.objects.filter(
        productvariant__product__in=products
    ).distinct()

    return render(request, 'home/product.html', {
        "product": products,
        "distinct_sizes": distinct_sizes
    })

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
        cart.price=product.discount_price * float(qty)
        cart.save()
    print(product.__dict__)
    return render(request,'home/product-details.html',{'product':product})

def shopping_cart(request):
    carts = Cart.objects.filter(made_by=request.user)
    total_amount = carts.aggregate(Sum('price'))['price__sum']
    print(total_amount)
    return render(request,'home/shopping-cart.html',{'carts':carts,'total_amount':total_amount})


def update_cart(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        qty = int(request.POST.get('qty'))

        # Get the cart item and update the quantity
        cart = Cart.objects.get(id=cart_id, made_by=request.user)
        cart.qty = qty
        cart.save()

        # Recalculate the total for this cart item
        item_total = cart.qty * cart.variant.product.discount_price
        
        # Recalculate the total amount for the cart
        total_amount = Cart.objects.filter(made_by=request.user).aggregate(Sum('price'))['price__sum']

        return JsonResponse({
            'total_amount': total_amount,
            'item_total': item_total
        })

def blog(request):
    return render(request,'home/blog.html')

def blog_details(request):
    return render(request,'home/blog-details.html')

def cart(request):
    carts = Cart.objects.filter(made_by=request.user)
    return render(request,'home/cart.html',{'carts':carts})

def custompage(request):
    sizes = Size.objects.filter(status=1).all()
    colors = Color.objects.filter(status=1).all()
    
    if request.method == 'POST':
        customize = Customizedesgin()
        customize.Customername = request.POST.get('name', '').strip()
        customize.moblie_no = request.POST.get('mobile_no', '').strip()
        customize.email = request.POST.get('email', '').strip()

        size_id = request.POST.get('size', '').strip()
        color_id = request.POST.get('color', '').strip()
        try:
            customize.size = Size.objects.get(id=size_id)
            customize.color = Color.objects.get(id=color_id)
        except Size.DoesNotExist:
            return HttpResponse("Size not found.", status=400)
        except Color.DoesNotExist:
            return HttpResponse("Color not found.", status=400)
        
        customize.attachment = request.FILES.get('design_image')
        customize.describe = request.POST.get('describe', '').strip()
        customize.save()
    context ={
        'size':sizes,
        'color':colors
    }
    return render(request,'home/Custom-page.html',context)