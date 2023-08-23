from django.shortcuts import render


def Manage(request):
    context ={}
    return render(request, 'admin/manage.html', context)
