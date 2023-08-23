from django.shortcuts import redirect, render

from app.models import CreateUserForm


def register(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    from_register = CreateUserForm()
    user_not_login = "show"
    user_login = "none"
    context = {'from': from_register,
               'user_login': user_login,
               'user_not_login': user_not_login,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height}

    # khi người dùng ấn nút đăng kí
    if request.method == 'POST':
        from_register = CreateUserForm(request.POST)
        if from_register.is_valid(): # kiểm tra đúng yêu cầu thì lưu cái form đó lại
            from_register.save()
            return redirect('login')
    return render(request, "app/register.html", context)
