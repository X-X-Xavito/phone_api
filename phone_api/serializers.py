from rest_framework import serializers
from phone_api.models import Company, Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'value']

class CompanySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = ['company_id', 'products']