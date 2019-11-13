from django.http import Http404

from rest_framework import generics, mixins, status, permissions
from rest_framework.response import Response

from phone_api.models import Company, Product, Recharge
from phone_api.serializers import CompanySerializer, ProductSerializer, RechargeSerializer

class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

class CompanyRetDesAPIView(generics.RetrieveDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        company_id = self.kwargs.get('company_id')
        try:
            return Company.objects.get(company_id=company_id)
        except Company.DoesNotExist:
            raise Http404
        
class CompanyCreateAPIView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProductCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(company_id=self.kwargs.get('company_id'))

class ProductUpdateAPIView(generics.UpdateAPIView):
    lookup_field = 'product_id'
    lookup_url_kwarg = 'product_id'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(product_id=self.kwargs.get('product_id'))

class ProductDeleteAPIView(generics.DestroyAPIView):
    lookup_field = 'product_id'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class RechargeCreateAPIView(generics.CreateAPIView):
    queryset = Recharge.objects.all()
    serializer_class = RechargeSerializer
    permission_classes = [permissions.IsAuthenticated]

class RechargeListAPIView(generics.ListAPIView):
    lookup_field='phone_number'
    serializer_class = RechargeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        phone_number = self.kwargs.get('phone_number')
        return Recharge.objects.filter(phone_number=phone_number)

class RechargeRetriveAPIView(generics.RetrieveAPIView):
    lookup_field='id'
    serializer_class = RechargeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        recharge_id = self.kwargs.get('pk')
        try:
            return Recharge.objects.get(id=recharge_id)
        except Recharge.DoesNotExist:
            raise Http404
