import json
from domain.models import MainMenus, SubMenus, User, Cart


def insert_nav_bar_data(request):
    # menus = MainMenus.objects.filter(status=1).order_by('priority')
    # if request.user:
    #     cart_counts = Cart.objects.filter(made_by=request.user).count()
    # else:
    #     cart_counts=0
    cart_counts=0
    menus={}

    return dict(menus=menus,cart_counts=cart_counts)
