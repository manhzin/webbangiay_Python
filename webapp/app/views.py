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

def myOrder(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    show_manage = 'show'  # Đảm bảo rằng biến show_manage đã được khai báo

    total_all = 0
    count = 0
    if request.user.is_authenticated:
        customer = request.user
        items = Cart.objects.filter(user=customer)
        user_not_login = "none"
        user_login = "show"
        for item in items:
            item.total = item.product.price * item.quantity
            total_all += item.product.price * item.quantity
            count += item.quantity
    else:
        order = None
        items = []
        user_not_login = "show"
        user_login = "none"

    my_orders = Order.objects.filter(customer=request.user)
    order_items = {}  # Tạo một từ điển để lưu trữ các đơn hàng và mặt hàng tương ứng
    order_addresses = {}  # Tạo một từ điển để lưu trữ đơn hàng và thông tin địa chỉ tương ứng
    order_total_amounts = {}

    for order in my_orders:
        items = OrderItem.objects.filter(order=order)
        order_items[order] = items
        total_order_amount = 0
        for item in items:
            total_order_amount += item.total
            print("tong gia order : ")
            print(total_order_amount)
        order_total_amounts[order.id] = total_order_amount

        address = order.address_order  # Truy cập vào đối tượng Address liên kết với đơn hàng
        order_addresses[order.id] = address
        if order.id in order_total_amounts:  # Sửa lại kiểm tra xem order.id có trong order_total_amounts
            print(f"Giá trị đã được lưu cho đơn hàng '{order}': {order_total_amounts[order.id]}")
        else:
            print(f"Không tìm thấy giá trị cho đơn hàng '{order}' trong order_total_amounts.")

    order_total_amounts_list = [(order_id, total_amount) for order_id, total_amount in order_total_amounts.items()]  # Đặt danh sách ngoài vòng lặp

    context = {
        'items': items,
        
        'total_all': total_all,
        'count': count,
        'order_addresses': order_addresses,
        'order_items': order_items,
        'slide_hidden': slide_hidden,
        'fixed_height': fixed_height,
        'show_manage': show_manage,
        'my_order': my_orders,
        'order_total_amounts': order_total_amounts,
        'order_total_amounts_list': order_total_amounts_list,  # Đưa vào context
    }
    return render(request, 'app/my_order.html', context)

def deletemyOrder(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    order = get_object_or_404(Order, id=id)
    print(order)
    items = OrderItem.objects.filter(order=order)
    print(items)
    if request.method == 'POST':
        items.delete()
        order.delete()
        messages.success(request, 'Xóa đơn hàng thành công')
        return redirect('myOrder')

    context = {'product': order
               }

    return render(request, 'app/delete_my_order.html', context)


def manageOrder(request):
    orders = Order.objects.all()


    context = {
        'orders': orders,
    }
    return render(request, 'admin/manageOrder.html', context)

def viewOrder(request):
    id = request.GET.get('id', '')
    order =  get_object_or_404(Order, id=id)
    print('id order: ')
    print(id)
    print(order.address_order)
    order_items = {}
    total = 0
    items = OrderItem.objects.filter(order=order)
    order_items[order] = items
    total_order_amount = 0
    for item in items:
        total += item.total

    context={'order': order,
             'order_items': order_items,
             'items': items,
             'total': total,
             }
    return render(request, 'admin/viewOrder.html', context)

def deleteOrder(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    order = get_object_or_404(Order, id=id)
    print(order)
    items = OrderItem.objects.filter(order=order)
    print(items)
    if request.method == 'POST':
        items.delete()
        order.delete()
        messages.success(request, 'Xóa đơn hàng thành công')
        return redirect('manageOrder')
    context = {'product': order}

    return render(request, 'admin/deleteOrder.html', context)