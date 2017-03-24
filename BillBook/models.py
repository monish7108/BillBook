from django.db import models

class Customer(models.Model):
    bill_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=30)
    mobile_no_1 = models.IntegerField(null=True, blank=True)
    mobile_no_2 = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.customer_name

class Bill(models.Model):
    bill_no = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    product_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    product_price = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return str(self.total_price)