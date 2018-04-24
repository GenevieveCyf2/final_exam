from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home_page(request):

    if request.method == 'POST':
        order = request.POST.get('order')
        address = request.POST.get("address")

        return render(request, 'order/home_page.html', {'order': order, 'address': address})

    return render(request, 'order/home_page.html')