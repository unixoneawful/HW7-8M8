
from django.shortcuts import render, redirect
from .models import ProductCl, TagCL, OrderCL, CustomerCL
from .forms import OrderForm

def tag_view(request, tag_name):
    tag = TagCL.objects.get(name=tag_name)
    products = ProductCl.objects.filter(tags=tag)
    context = {'products': products, 'tag': tag}
    return render(request, 'cloth/tag.html', context)

def create_order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('cloth:order_success', order_id=order.pk)
    else:
        form = OrderForm()
    context = {'form': form}
    return render(request, 'cloth/create_order.html', context)

def order_success_view(request, order_id):
    order = OrderCL.objects.get(pk=order_id)
    return render(request, 'cloth/order_success.html', {'order': order})
