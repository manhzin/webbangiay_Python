from django.contrib.auth.models import User
from django.shortcuts import render


def manageUser(request):
    users = User.objects.all()  # lay cac damh muc lon
    context = {'users': users}
    return render(request, 'admin/manageUser.html', context)
