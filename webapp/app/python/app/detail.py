from django.shortcuts import get_object_or_404, render

from app.models import *


def detail(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    fixed_comment = "100px"
    #check xem phải admin không
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
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
    form = CommentForm()
    id = request.GET.get('id', '') # lấy id khi người dùng vlick vào sản phẩm nào đó
    user = request.user
    products = get_object_or_404(Product, id=id)
    comment = Comment.objects.filter(product=products) # lấy đúng cái cmt của cái sp đó
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['title']
            comments = Comment(user=user, product=products, title=content)
            comments.save()
    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    context = {'form': form,
               'comments': comment,
               'products': products,
               'items': items,
               'order': order,
               'user_login': user_login,
               'user_not_login': user_not_login,
               'categories': categories,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'fixed_comment': fixed_comment,
               'show_manage': show_manage,
               }
    return render(request, 'app/detail.html', context)
