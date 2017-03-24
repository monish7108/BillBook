from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="homepage"),
    url(r'^add/bill/$', views.AddBill.as_view(), name="addnewbill"),
]
