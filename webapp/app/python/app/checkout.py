from django.shortcuts import render

from app.models import *


def checkout(request):
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    slide_hidden = "hidden"
    fixed_height = "20px"
    categories = Category.objects.filter(is_sub=False)  # lấy các danh mục lớn
    form = AddressForm()
    total_all = 0
    count = 0
    if request.user.is_authenticated:
        customer = request.user
        allAddress = Adress.objects.filter(customer=customer)
        items = Cart.objects.filter(user=customer)
        user_not_login = "none"
        user_login = "show"
        for item in items:
            print(item)
            item.total = item.product.price * item.quantity
            total_all += item.product.price * item.quantity
            count += item.quantity
    else:
        allAddress = None
        order = None
        items = []
        user_not_login = "show"
        user_login = "none"

    if allAddress is not None and allAddress.exists():
        # Ẩn form thêm địa chỉ
        form_hidden = "hidden"
        form_show = "show"
    else:
        # Hiển thị form thêm địa chỉ
        form_hidden = "show"
        form_show = "hidden"
    context = {'categories':categories,
               'items': items,
               'total_all': total_all,
               'count': count,
               'user_login': user_login,
               'user_not_login': user_not_login,
               'form': form, 'allAddress': allAddress,
               'form_hidden': form_hidden,
               'form_show': form_show,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'show_manage': show_manage,
               }
    return render(request, 'app/checkout.html', context)

