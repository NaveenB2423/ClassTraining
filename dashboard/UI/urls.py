from django.urls import path
from .views import *

urlpatterns = [
    path('',dashboard1, name='dashboard1'),
    path('dashboard2',dashboard2, name='dashboard2'),
    path('dashboard3',dashboard3, name='dashboard3'),
    path('iframe',iframe, name='iframe'),
    path('pages/widgets',widgets, name='widgets'),
    path('pages/karban',karban, name='karban'),
    path('pages/charts/chartjs',chartjs, name='chartjs'),
    path('pages/charts/flot',flot, name='flot'),
    path('pages/charts/inline',inline, name='inline'),
    path('pages/charts/uplot',uplot, name='uplot'),
    path('pages/ui/buttons',ui_buttons, name='ui_buttons'),
    path('pages/ui/general',ui_general, name='ui_general'),
    path('pages/ui/icons',ui_icons, name='ui_icons'),
    path('pages/ui/modals',ui_modals, name='ui_modals'),
    path('pages/ui/navbar',ui_navbar, name='ui_navbar'),
    path('pages/ui/ribbons',ui_ribbons, name='ui_ribbons'),
    path('pages/ui/sliders',ui_sliders, name='ui_sliders'),
    path('pages/ui/timeline',ui_timeline, name='ui_timeline'),
    path('pages/forms/advanced',forms_advanced, name='forms_advanced'),
    path('pages/forms/editors',forms_editors, name='forms_editors'),
    path('pages/forms/general',forms_general, name='forms_general'),
    path('pages/forms/validation',forms_validation, name='forms_validation'),
    path('pages/tables/data',tables_data, name='tables_data'),
    path('pages/tables/jsgrid',tables_jsgrid, name='tables_jsgrid'),
    path('pages/tables/simple',tables_simple, name='tables_simple'),
    path('pages/tables/project-add',examples_project_add, name='examples_project_add'),
    path('pages/tables/project-detail',examples_project_detail, name='examples_project_detail'),
    path('pages/tables/project-edit',examples_project_edit, name='examples_project_edit'),
    path('pages/tables/projects',examples_projects, name='examples_projects'),
    

    



]