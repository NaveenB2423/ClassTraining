from django.shortcuts import render
from domain.models import Product, ProductVariant, Cart, Color, Size

# Create your views here.
def index(request):
    print(request.user.id)
    product = Product.objects.filter(status=1).last()
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
        
    return render(request,'home/product.html',{'product':product})


def cart(request):
    carts = Cart.objects.filter(made_by=request.user)
    return render(request,'home/cart.html',{'carts':carts})
