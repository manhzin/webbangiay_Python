from django.shortcuts import render

from app.models import *


def information_address(request):
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
    address_infor = Adress.objects.filter(customer=request.user)
    if request.user.is_authenticated:
        user = request.user

    form = AddressForm()
    context = {'address_infor': address_infor,
               'fixed_height': fixed_height,
               'slide_hidden': slide_hidden,
               'form': form,
               'show_manage': show_manage,
               }
    return render(request, 'app/information_address.html', context)
