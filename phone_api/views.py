from phone_api.models import Company, Product
from phone_api.serializers import CompanySerializer, ProductSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyRetDesAPIView(generics.RetrieveDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_object(self):
        company_id = self.kwargs.get('company_id')
        print('company_id', company_id)
        try:
            return Company.objects.get(company_id=company_id)
        except Company.DoesNotExist:
            raise Http404
        
class CompanyCreateAPIView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
class ProductCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(company_id=self.kwargs.get('company_id'))

class ProductUpdateAPIView(generics.UpdateAPIView):
    lookup_field = 'product_id'
    lookup_url_kwarg = 'product_id'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        serializer.save(product_id=self.kwargs.get('product_id'))


class ProductDeleteAPIView(generics.DestroyAPIView):
    lookup_field = 'product_id'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer