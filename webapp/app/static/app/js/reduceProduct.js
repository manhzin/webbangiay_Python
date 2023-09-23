document.addEventListener("DOMContentLoaded", function () {
    var reduceBtns = document.getElementsByClassName('reduce-btn');
    
    for (var i = 0; i < reduceBtns.length; i++) {
        reduceBtns[i].addEventListener('click', function () {
            var productId = this.dataset.product;
            var action = this.dataset.action;
            var size = this.dataset.size

            console.log(productId);
            console.log('action: ', action);
            console.log('size: ', size);
            if (user === "AnonymousUser") {
                console.log("User not login");
            } else {
                updateUserOrder(productId, action, size);
            }
        });
    }
    
    function updateUserOrder(productId, action, size) {
        console.log("User login ok");
        console.log("id: ", productId);
        console.log("action 2: ", action);
        var url = '/update_item/';
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'productId': productId,
                'action': action,
                'size': size,
            })
        }).then(function (response) {
            return response.json();
        }).then(function (data) {
            console.log('data: ', data);
            location.reload();
        });
    }

    // Lắng nghe sự kiện khi người dùng ấn nút "Thêm vào giỏ hàng"
    var addToCartButton = document.querySelector(".add-btn");
    addToCartButton.addEventListener("click", function () {
        // Lấy giá trị của kích cỡ đã chọn
        var selectedSize = document.querySelector("input[name='optionsRadios']:checked").value;

        // Sử dụng selectedSize để thêm vào giỏ hàng (đây là nơi bạn xử lý logic thêm vào giỏ hàng)
        addToCart(selectedSize);
    });

    // Hàm xử lý logic thêm vào giỏ hàng
    function addToCart(size) {
        // Gửi yêu cầu AJAX hoặc chuyển đến trang xử lý để lưu sản phẩm và kích cỡ vào giỏ hàng
        // Ví dụ sử dụng AJAX để gửi dữ liệu đến máy chủ Django:
        $.ajax({
            url: '/update_item/', // Điều này cần phải được thay đổi thành URL xử lý thêm vào giỏ hàng của bạn
            method: 'POST',
            data: {
                'size': size,
                'product_id': '{{ products.id }}', // Sử dụng template tag để lấy ID sản phẩm
                'csrfmiddlewaretoken': '{{ csrf_token }}', // Sử dụng template tag để lấy CSRF token
            },
            success: function (response) {
                // Xử lý phản hồi từ máy chủ sau khi thêm vào giỏ hàng thành công
                // Ví dụ: hiển thị thông báo, cập nhật giỏ hàng trên giao diện người dùng, v.v.
            },
            error: function (error) {
                // Xử lý lỗi nếu có
            }
        });
    }
});
