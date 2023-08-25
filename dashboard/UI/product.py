from django.shortcuts import render, HttpResponse, redirect
from domain.models import Category, Product, Size, Color, ProductVariant

def add_product(request):
    categories = Category.objects.filter(status=1).all()
    sizes = Size.objects.filter(status=1).all()
    colors = Color.objects.filter(status=1).all()
    product = Product()
    if request.method == "POST":
        product.name= request.POST.get('name','').strip()
        product.description = request.POST.get('description','').strip()
        product.category_id = request.POST.get('category')
        product.price = request.POST.get('price','').strip()
        product.save()
        #product.image = request.POST.get('','').strip()
        selected_colors = request.POST.getlist('color')
        selected_sizes = request.POST.getlist('size')
        for color_id in selected_colors:
            
            for size_id in selected_sizes:
                product_sku = ProductVariant()
                product_sku.color = Color.objects.get(id=color_id)
                product_sku.size = Size.objects.get(id=size_id)
                product_sku.product = product
                product_sku.save()

    return render(request, 'product/add_product.html', {'categories':categories,'sizes':sizes,'colors':colors})


def list_product(request):
    products = Product.objects.filter(status=1).all()
    return render(request, 'product/list_product.html',{'products': products})

def edit_product(request,id):
    categories = Category.objects.filter(status=1).all()
    sizes = Size.objects.filter(status=1).all()
    colors = Color.objects.filter(status=1).all()
    product = Product.objects.get(id=id)
    if request.method == "POST":
        product.name= request.POST.get('name','').strip()
        product.description = request.POST.get('description','').strip()
        product.category_id = request.POST.get('category')
        product.price = request.POST.get('price','').strip()
        product.save()
        #product.image = request.POST.get('','').strip()
        selected_colors = request.POST.getlist('color')
        selected_sizes = request.POST.getlist('size')
        old_variants = ProductVariant.objects.filter(product=product).all()
        for old in old_variants:
            old.status=0
            old.save()
        for color_id in selected_colors: 
            for size_id in selected_sizes:
                color = Color.objects.get(id=color_id)
                size = Size.objects.get(id=size_id)
                check_variant = ProductVariant.objects.filter(product=product, color=color,size=size).exists()
                if not check_variant:
                    variant = ProductVariant.objects.create(product=product, size=size, color=color,status=1)
                else:
                    variant = ProductVariant.objects.get(product=product, color=color,size=size)
                    variant.status=1
                    variant.save()
                    
                
                            

                

    return render(request, 'product/edit_product.html',{'product': product,'categories':categories,'sizes':sizes,'colors':colors})

def delete_product(request,id):
    product = Product.objects.get(id=id)
    product.status = 0
    product.save()
    return redirect(list_product)