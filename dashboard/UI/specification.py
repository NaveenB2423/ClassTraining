from django.shortcuts import render, HttpResponse, redirect
from domain.models import Category, Color, Size




def category(request):
    categories = Category.objects.filter(status=1).all()
    if request.method == 'POST':
        new_category = Category()
        new_category.name = request.POST.get('name','').strip()
        new_category.priority = request.POST.get('priority_no','').strip()
        new_category.save()
    return render(request, 'specification/category.html',{'categories':categories})

def edit_category(request,id):
    categories = Category.objects.filter(status=1).all()
    selected_category = Category.objects.get(id=id)
    if request.method == 'POST':
        selected_category.name = request.POST.get('name','').strip()
        selected_category.priority = request.POST.get('priority_no','').strip()
        selected_category.save()
        return redirect(category)
    return render(request, 'specification/edit_category.html',{'categories':categories,'selected_category':selected_category})

def delete_category(request, id):
    selected_category = Category.objects.get(id=id)
    selected_category.status = 0
    selected_category.save()
    return redirect(category)
    
def color(request):
    colors = Color.objects.filter(status=1).all()
    if request.method == 'POST':
        new_color = Color()
        new_color.name = request.POST.get('name','').strip()
        new_color.priority = request.POST.get('priority_no','').strip()
        new_color.save()
    return render(request, 'specification/color.html',{'colors':colors})

def edit_color(request,id):
    colors = Color.objects.filter(status=1).all()
    selected_color = Color.objects.get(id=id)
    if request.method == 'POST':
        selected_color.name = request.POST.get('name','').strip()
        selected_color.priority = request.POST.get('priority_no','').strip()
        selected_color.save()
        return redirect(color)
    return render(request, 'specification/edit_color.html',{'colors':colors,'selected_color':selected_color})

def delete_color(request, id):
    selected_color = Color.objects.get(id=id)
    selected_color.status = 0
    selected_color.save()
    return redirect(color)
    
def size(request):
    sizes = Size.objects.filter(status=1).all()
    if request.method == 'POST':
        new_size = Size()
        new_size.name = request.POST.get('name','').strip()
        new_size.priority = request.POST.get('priority_no','').strip()
        new_size.save()
    return render(request, 'specification/size.html',{'sizes':sizes})

def edit_size(request,id):
    sizes = Size.objects.filter(status=1).all()
    selected_size = Size.objects.get(id=id)
    if request.method == 'POST':
        selected_size.name = request.POST.get('name','').strip()
        selected_size.priority = request.POST.get('priority_no','').strip()
        selected_size.save()
        return redirect(size)
    return render(request, 'specification/edit_size.html',{'sizes':sizes,'selected_size':selected_size})

def delete_size(request, id):
    selected_size = Size.objects.get(id=id)
    selected_size.status = 0
    selected_size.save()
    return redirect(size)
    