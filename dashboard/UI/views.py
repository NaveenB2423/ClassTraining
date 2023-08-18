from django.shortcuts import render, HttpResponse

# Create your views here.
def dashboard1(request):
    return render(request,'dashboard1.html')

def dashboard2(request):
    return render(request,'dashboard2.html')


def dashboard3(request):
    return render(request,'dashboard3.html')


def widgets(request):
    return render(request,'pages/widgets.html')


def chartjs(request):
    return render(request,'pages/charts/chartjs.html')

def flot(request):
    return render(request,'pages/charts/flot.html')

def inline(request):
    return render(request,'pages/charts/inline.html')

def uplot(request):
    return render(request,'pages/charts/uplot.html')

def ui_buttons(request):
    return render(request,'pages/UI/buttons.html')

def ui_general(request):
    return render(request,'pages/UI/general.html')

def ui_icons(request):
    return render(request,'pages/UI/icons.html')

def ui_modals(request):
    return render(request,'pages/UI/modals.html')

def ui_navbar(request):
    return render(request,'pages/UI/navbar.html')

def ui_ribbons(request):
    return render(request,'pages/UI/ribbons.html')

def ui_sliders(request):
    return render(request,'pages/UI/sliders.html')

def ui_timeline(request):
    return render(request,'pages/UI/timeline.html')

def forms_advanced(request):
    return render(request,'pages/forms/advanced.html')

def forms_editors(request):
    return render(request,'pages/forms/editors.html')

def forms_general(request):
    return render(request,'pages/forms/general.html')


def forms_validation(request):
    return render(request,'pages/forms/validation.html')


def tables_data(request):
    return render(request,'pages/tables/data.html')


def tables_jsgrid(request):
    return render(request,'pages/tables/jsgrid.html')

def tables_simple(request):
    return render(request,'pages/tables/simple.html')

def examples_project_add(request):
    return render(request,'pages/examples/project-add.html')

def examples_project_detail(request):
    return render(request,'pages/examples/project-detail.html')


def examples_project_edit(request):
    return render(request,'pages/examples/project-edit.html')

def examples_projects(request):
    return render(request,'pages/examples/projects.html')

def karban(request):
    return render(request, 'pages/kanban.html')

def iframe(request):
    return render(request,'iframe.html')

