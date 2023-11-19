from django.urls import path
from . import specification
from . import product
from . import views 

urlpatterns = [
    path('',views.admin_login, name='admin_login'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('category', specification.category, name='category'),
    path('edit-category/<int:id>',specification.edit_category, name='edit_category'),
    path('delete-category/<int:id>',specification.delete_category, name='delete_category'),
    path('color', specification.color, name='color'),
    path('edit-color/<int:id>',specification.edit_color, name='edit_color'),
    path('delete-color/<int:id>',specification.delete_color, name='delete_color'),
    path('size', specification.size, name='size'),
    path('edit-size/<int:id>',specification.edit_size, name='edit_size'),
    path('delete-size/<int:id>',specification.delete_size, name='delete_size'),
    path('add-product', product.add_product, name='add_product'),
    path('list-products', product.list_product, name='list_product'),
    path('edit-product/<int:id>',product.edit_product, name='edit_product'),
    path('delete-product/<int:id>',product.delete_product, name='delete_product'),
    path('update-home-item',product.update_home_item,name="update_home_item"),
    path('ecommerce',product.ecommerce, name='ecommerce'),
    
]