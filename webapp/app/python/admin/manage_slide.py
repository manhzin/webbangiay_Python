from django.shortcuts import render

from app.models import *


def manageSlide(request):
    slides = Slide.objects.all()
    context ={'slides': slides}
    return render(request, 'admin/managementSlide.html', context)

def addProduct(request):
    form = AddSlide()
    if request.method == 'POST':
        form = AddSlide(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product saved successfully!')
            return redirect('manageProduct')

    context = {'form': form,
               'messages': messages,
               }
    return render(request, 'admin/addProduct.html', context)


def editProduct(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    slide = get_object_or_404(slide, id=id)
    if request.method == 'POST':
        form = AddSlide(request.POST, request.FILES, instance=slide)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('manageSlide')
    form = AddSlide(instance=slide,
                      initial={'name': slide.name,
                               'detail': slide.detail,
                               'image': slide.image})

    context = {'product': slide,
               'form': form}
    return render(request, 'admin/editProduct.html', context)

def deleteProduct(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    slide = get_object_or_404(Slide, id=id)
    if request.method == 'POST':
        slide.delete()
        messages.success(request, 'Category deleted successfully!')
        return redirect('manageProduct')
    context ={'slide': slide}
    return render(request, 'admin/deleteProduct.html', context)
