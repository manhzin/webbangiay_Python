from django.shortcuts import render

from app.models import *


def base(request):
    user = request.user
    if user.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    slide = Slide.objects.all()
    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    context = {
        'slide': slide,
        'categories': categories,
        'show_manage': show_manage,
    }
    return render(request, 'app/base.html', context)

def getHome(request):
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
    return render(request, 'app/home.html', context)


def show_manage(request):
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'

    return show_manage