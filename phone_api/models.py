from django.db import models


class Company(models.Model):
    company_id = models.CharField(max_length=50, primary_key=True)

    class Meta:
        ordering = ['company_id']

    def __str__(self):
        return self.company_id

class Product(models.Model):
    company = models.ForeignKey(Company, related_name='products', on_delete=models.CASCADE)
    product_id = models.CharField(max_length=50, primary_key=True)
    value = models.FloatField()

    class Meta:
        ordering = ['product_id']

    def __str__(self):
        return "'id': '{}','value':{}".format(self.product_id, self.value)

class Recharge(models.Model):
    created_at = models.DateTimeField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
    value = models.FloatField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return "Recharge {} - Phone_number{} - value {}".format(id, self.phone_number, self.value)