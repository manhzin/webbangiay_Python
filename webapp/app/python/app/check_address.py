from django.contrib import messages
from django.shortcuts import render

from app.models import *


def Continue1(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    # lấy các sản phẩm
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

    # lấy địa chỉ
    form = AddressForm()
    allAddress = Adress.objects.all()
    if request.user.is_authenticated:
        user = request.user
        shipping = Adress.objects.filter(customer=user)

    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            mobile = form.cleaned_data['mobile']
            shipping = Adress(customer=request.user, address=address, city=city, state=state, mobile=mobile)
            shipping.save()
            messages.success(request, 'Address saved successfully!')
        else:
            messages.error(request, 'Failed to save address.')
    else:
        form = AddressForm()

    context = {'shipping': shipping,
               'items': items,
               'order': order,
               'user_login': user_login,
               'user_not_login': user_not_login,
               'allAddress': allAddress,
               'messages': messages,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'show_manage': show_manage
               }
    return render(request, 'app/address.html', context)
