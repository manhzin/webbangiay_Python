import json
from django.http import JsonResponse
from app.models import Cart, Product

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    selectedSize = data.get('size', None)  # Lấy kích cỡ từ dữ liệu yêu cầu
    customer = request.user
    product = Product.objects.get(id=productId)
    
    # Tìm giỏ hàng có sản phẩm và kích thước cụ thể
    try:
        order = Cart.objects.get(user=request.user, product=product, size=selectedSize)
        print(order.size)
        print(order.quantity)
        print(order.product.name) 
    except Cart.DoesNotExist:
        order = None
    
    if action == 'addProduct':
        # Bạn phải kiểm tra xem 'order' đã được tạo hay chưa và thêm mới nếu chưa
        if order is None:
            order = Cart(user=request.user, product=product, size=selectedSize, quantity=1)
        else:
            order.quantity = 1
    
    if action == 'add':
        order.quantity += 1
    
    if action == 'remove':
        order.quantity -= 1

    if order and order.quantity <= 0:
        order.delete()
    elif order:
        order.save()
        
    return JsonResponse('added', safe=False)
