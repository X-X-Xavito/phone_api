from django.db import models


class Company(models.Model):
    company_id = models.CharField(max_length=50, primary_key=True)

    class Meta:
        ordering = ['company_id']

    def __str__(self):
        return self.company_id

class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=50, primary_key=True)
    value = models.IntegerField()

    class Meta:
        ordering = ['product_id']

    def __str__(self):
        return self.product_id