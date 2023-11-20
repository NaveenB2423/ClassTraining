from django.shortcuts import render, HttpResponse, redirect
from domain.models import MainMenus, SubMenus



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