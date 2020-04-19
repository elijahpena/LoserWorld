from django.shortcuts import render

# Create your views here.

def orderView(request):
    return render(request, 'order/order.html')
