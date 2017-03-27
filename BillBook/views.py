from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse
import xlsxwriter

#################################################################################################
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
        print(bill.bill_id)
        return HttpResponseRedirect(reverse("viewbill",kwargs={"bill_id":bill.bill_id}))
#################################################################################################


class ViewBill(LoginRequiredMixin,View):

    def get(self,request,bill_id):
        try:
            customer = Customer.objects.get(bill_id=bill_id)
            bill = Bill.objects.filter(bill_no = customer)
        except Exception as e:
            return HttpResponse("Not Found.")
        else:
            return render(request, "Bill/viewbill.html", {"customer":customer,"bill":bill})

#################################################################################################


def printBill(request):
    bill_id = request.POST.get('bill_id')
    customer_name = request.POST.get('customer_name')
    mobile_number1 = request.POST.get('mobile1')

    product_list = request.POST.getlist('product_name')
    quantity_list = request.POST.getlist('quantity')
    price_list = request.POST.getlist('price')
    total = request.POST.getlist('totalprice')
    # print(quantity_list)
    # print(price_list)
    # print(total)
    filename = str(customer_name)+" "+str(bill_id)+".xlsx"
    # print(filename)
    workbook = xlsxwriter.Workbook(filename=filename)
    worksheet = workbook.add_worksheet()
    worksheet.write(0,0,"Bill ID")
    worksheet.write(0,1,bill_id)
    worksheet.write(2, 0, "Customer Name")
    worksheet.write(2, 1, customer_name)
    worksheet.write(4, 0, "Mobile")
    worksheet.write(4, 1, mobile_number1)

    worksheet.write(6, 0, "Product")
    worksheet.write(6,1,"Quantity")
    worksheet.write(6, 2, "Price")
    worksheet.write(6, 3, "Total")

    row = 8
    col = 0

    for i in range(len(product_list)):
        worksheet.write(row, col, product_list[i])
        worksheet.write(row, col+1, quantity_list[i])
        worksheet.write(row, col+2, price_list[i])
        worksheet.write(row, col+3, total[i])
        row+=1

    # worksheet.write(row+1, col+3, S)
    workbook.close()

    return render(request,"Bill/homepage.html")

#################################################################################################
