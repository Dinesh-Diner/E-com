from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
# Create your views here.

def home(request):
    # return HttpResponse("homepage")

    customer=Customer.objects.all()
    order=Order.objects.all()

    Total_customer=customer.count()

    Total_orders=order.count()
    Total_delivered=order.filter(status="Delivered").count()
    Total_Pending=order.filter(status="pending").count()

    context={
        'cus':customer,
        'ord':order,
        'Total_orders':Total_orders,
        'Total_delivered':Total_delivered,
        'Total_Pending':Total_Pending,

    }
    return render(request,'accounts/dashboard.html',context)

def product(request):
    # return HttpResponse ("Product details")

    product1=Product.objects.all()
    return render(request,'accounts/product.html',{'pro':product1})

def customer(request,pk):
    # return HttpResponse("Customer details")

    cus = Customer.objects.get(id=pk)
    ord=cus.order_set.all()
    to_ord=ord.count()
    context={
        'cus1':cus,
        'ord1':ord,
        'to_or':to_ord
    }
    return render(request,'accounts/customer.html',context)


def createOrder(request):
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form1': form
    }

    return render(request,'accounts/order_form.html',context)

def Update(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=="POST":
        form=OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form1': form
    }
    return render(request,'accounts/order_form.html',context)

def delete(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect ('/')
    context={
        'item':order
        }
    return render(request,'accounts/delete.html',context)
