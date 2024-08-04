from django.shortcuts import render, HttpResponse, redirect
from domain.models import MainMenus, SubMenus, Color, Size



#Main Menu
def create_main_menu(request):
    main_menus = MainMenus.objects.filter(status=1).all()
    if request.method == 'POST':
        main_menu = MainMenus()
        main_menu.name = request.POST.get('name','').strip()
        main_menu.priority = request.POST.get('priority_no','').strip()
        main_menu.save()
    return render(request, 'admin_page/category/menus/main_menus/add_main_menu.html',{'main_menus':main_menus})

def edit_main_menu(request,id):
    main_menus = MainMenus.objects.filter(status=1).all()
    selected_main_menu = MainMenus.objects.get(id=id)
    if request.method == 'POST':
        selected_main_menu.name = request.POST.get('name','').strip()
        selected_main_menu.priority = request.POST.get('priority_no','').strip()
        selected_main_menu.save()
        return redirect(create_main_menu)
    return render(request, 'admin_page/category/menus/main_menus/edit_main_menu.html',{'main_menus':main_menus,'selected_main_menu':selected_main_menu})

def delete_main_menu(request, id):
    selected_category = MainMenus.objects.get(id=id)
    selected_category.status = 0
    selected_category.save()
    return redirect(create_main_menu)
    
#End
# Sub Menu
def create_sub_menu(request):
    sub_menus = SubMenus.objects.filter(status=1).all()
    main_menus = MainMenus.objects.filter(status=1).all()
    if request.method == 'POST':
        sub_menu = SubMenus()
        sub_menu.main_menu_id = request.POST.get('main_menu')
        sub_menu.name = request.POST.get('name','').strip()
        sub_menu.save()
    return render(request, 'admin_page/category/menus/sub_menus/add_sub_menu.html',{'sub_menus':sub_menus,'main_menus':main_menus})

def edit_sub_menu(request,id):
    sub_menus = SubMenus.objects.filter(status=1).all()
    main_menus = MainMenus.objects.filter(status=1).all()
    selected_sub_menu = SubMenus.objects.get(id=id)
    if request.method == 'POST':
        selected_sub_menu.main_menu_id = request.POST.get('main_menu')
        selected_sub_menu.name = request.POST.get('name','').strip()
        selected_sub_menu.save()
        return redirect(create_sub_menu)
    return render(request, 'admin_page/category/menus/sub_menus/edit_sub_menu.html',{'sub_menus':sub_menus,'main_menus':main_menus,'selected_sub_menu':selected_sub_menu})

    
#End

def add_color(request):
    colors = Color.objects.filter(status=1).all()
    if request.method == 'POST':
        new_color = Color()
        new_color.name = request.POST.get('name','').strip()
        new_color.save()
    return render(request, 'admin_page/category/color/add_color.html',{'colors':colors})

def edit_color(request,id):
    colors = Color.objects.filter(status=1).all()
    selected_color = Color.objects.get(id=id)
    if request.method == 'POST':
        selected_color.name = request.POST.get('name','').strip()
        selected_color.save()
        return redirect(add_color)
    return render(request, 'admin_page/category/color/edit_color.html',{'colors':colors,'selected_color':selected_color})

def delete_color(request, id):
    selected_color = Color.objects.get(id=id)
    selected_color.status = 0
    selected_color.save()
    return redirect(add_color)
    
def add_size(request):
    sizes = Size.objects.filter(status=1).all()
    if request.method == 'POST':
        new_size = Size()
        new_size.name = request.POST.get('name','').strip()
        new_size.save()
    return render(request, 'admin_page/category/size/add_size.html',{'sizes':sizes})

def edit_size(request,id):
    sizes = Size.objects.filter(status=1).all()
    selected_size = Size.objects.get(id=id)
    if request.method == 'POST':
        selected_size.name = request.POST.get('name','').strip()
        selected_size.save()
        return redirect(add_size)
    return render(request, 'admin_page/category/size/add_size.html',{'sizes':sizes,'selected_size':selected_size})

def delete_size(request, id):
    selected_size = Size.objects.get(id=id)
    selected_size.status = 0
    selected_size.save()
    return redirect(add_size)
    