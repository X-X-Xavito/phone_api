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