from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse

@login_required
def index(request):
    return render(request,"Bill/homepage.html")

class AddBill(LoginRequiredMixin,View):

    def get(self,request):
        return render(request,"Bill/addnewbill.html")

    def post(self,request):
        customer_name = request.POST.get('name')
        mobile_number1= request.POST.get('mobile1')
        mobile_number2 = request.POST.get('mobile2')
        product_list = request.POST.getlist('product')
        quantity_list = request.POST.getlist('quantity')
        price_list = request.POST.getlist('price')

        bill = Customer.objects.create(customer_name=customer_name,mobile_no_1= mobile_number1,mobile_no_2= mobile_number2)

        for i in range(len(price_list)):

            a = Bill.objects.create(bill_no=bill,product_name = product_list[i],quantity = int(quantity_list[i]),product_price = int(price_list[i]), total_price = int(quantity_list[i])*int(price_list[i]))

        # Bill.objects.bulk_create(querylist)
        return HttpResponse("asjdbasjbd")
