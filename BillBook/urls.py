from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="homepage"),
    url(r'^add/bill/$', views.AddBill.as_view(), name="addnewbill"),
    url(r'^view/bill/(?P<bill_id>\d+)/', views.ViewBill.as_view(), name="viewbill"),
    url(r'^print/bill/$', views.printBill, name="printbill")
]
