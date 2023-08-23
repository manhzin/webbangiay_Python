from django.shortcuts import render

from app.models import *


def searchProduct(request):
    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    slide_hidden = "hidden"
    fixed_height = "20px"
    # check xem phải admin không
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    if request.user.is_authenticated: # neu da xac thuc
        user_not_login = "none"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "none"

    if request.method == "POST":
        search = request.POST["searched"]
        keys = Product.objects.filter(name__contains=search)
        if request.user.is_authenticated:
            customer = request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            for item in items:
                item.total = item.product.price * item.quantity
        else:
            order = None
            items = []
    return render(request, "app/search.html",
                  {'categories': categories,
                   'user_login': user_login,
                   'user_not_login': user_not_login,
                   "search": search,
                   "keys": keys,
                   'items': items,
                   'order': order,
                   'slide_hidden': slide_hidden,
                   'fixed_height': fixed_height,
                   'show_manage': show_manage,
                   })
