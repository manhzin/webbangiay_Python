# from itertools import product
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import *

from .python.app.base import *
from .python.app.information_address import information_address
from .python.app.cart import cart
from .python.app.category import category
from .python.app.check_address import Continue1
from .python.app.checkout import checkout
from .python.app.detail import detail
from .python.app.information import Information
from .python.app.login import loginPage, logoutPage
from .python.app.register import register
from .python.app.search import searchProduct
from .python.app.updateItem import updateItem
from .python.app.contact import contact
from .python.app.manage_address import addAddress, editAddress, deleteAddress
from .python.admin.manage import Manage
from .python.admin.manage_slide import manageSlide
from .python.admin.manage_user import manageUser
from .python.admin.manage_category import manageCategory, addCategory, editCategory, deleteCategory
from .python.admin.manage_product import manageProduct, addProduct, editProduct, deleteProduct, viewProduct


def shop(request):
    user = request.user
    if user.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    products = Product.objects.all()
    slide = Slide.objects.all()
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        user_not_login = "none"
        user_login = "show"
        for item in items:
            item.total = item.product.price * item.quantity
    else:
        order = None
        items = []
        user_not_login = "show"
        user_login = "none"

    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    active_category = request.GET.get('category', '')
    context = {'products': products,
               'slide': slide,
               'items': items,
               'order': order,
               'user_login': user_login,
               'user_not_login': user_not_login,
               'categories': categories,
               'active_category': active_category,
               'show_manage': show_manage}
    return render(request, 'app/shop.html', context)


def about(request):
    context={}

    return render(request, 'app/about.html', context)