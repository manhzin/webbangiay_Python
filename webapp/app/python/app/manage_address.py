from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

from app.models import *


def deleteAddress(request):
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    address = get_object_or_404(Adress, id=id)
    if request.method == 'POST':
        address.delete()
        return redirect('information')
    context = {}
    return render(request, 'app/delete_address.html', context)

def addAddress(request):
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    slide_hidden = "hidden"
    fixed_height = "20px"
    form = AddressForm()
    user = request.user
    if request.method == 'POST':
        form = AddressForm(request.POST)
        print('vao dc dảyoi')
        if form.is_valid():
            user_name = form.cleaned_data['name_user']
            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['adress']
            city = form.cleaned_data['city']
            district = form.cleaned_data['district']
            commune = form.cleaned_data['commune']

            add_address_user = Adress(customer=user, name_user=user_name, adress=address, city=city, mobile=mobile, district=district, commune=commune)
            print(add_address_user)
            add_address_user.save()
            print('Address saved successfully!')
            return redirect('information')
        else:
            print(form.errors)
            print('Address saved successfully no no no no')

    context = {'form': form,
               'messages': messages,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'show_manage': show_manage,
               }
    return render(request, 'app/add_address.html', context)

def editAddress(request):
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

    id = request.GET.get('id', '')
    address_user = get_object_or_404(Adress, id=id)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address_user)
        if form.is_valid():
            user_name = form.cleaned_data['name_user']
            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['adress']
            city = form.cleaned_data['city']
            district = form.cleaned_data['district']
            commune = form.cleaned_data['commune']

            address_user.customer = request.user
            address_user.name_user = user_name
            address_user.adress = address
            address_user.city = city
            address_user.mobile = mobile
            address_user.district = district
            address_user.commune = commune
            print(address_user)
            address_user.save()
            print('Address saved successfully!')
            return redirect('information')
        else:
            print("Form is not valid")
    else:
        form = AddressForm(instance=address_user)

    context = {'form': form,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'show_manage': show_manage,
               }
    return render(request, 'app/edit_address.html', context)
