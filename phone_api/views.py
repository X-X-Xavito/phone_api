from phone_api.models import Company, Product
from phone_api.serializers import CompanySerializer, ProductSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_object(self):
        company_id = self.kwargs.get('company_id')
        print('company_id', company_id)
        try:
            return Company.objects.get(company_id=company_id)
        except Company.DoesNotExist:
            raise Http404
        
    def update(self, request,  *args, **kwargs):
        company = self.get_object()
        company.company_id=request.data.get('company_id')
        company.save()

        serializer = self.get_serializer(company, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)


        return Response(serializer.data)

    
class CreateProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(company_id=self.kwargs.get('company_id'))

    # def post(self, request, *args, **kwargs):
    #     company_id = self.kwargs.get('company_id')
    #     print('reques data', request.data)        
        
        
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)






























# from django.http import Http404

# from phone_api.models import Company, Product
# from phone_api.serializers import CompanySerializer, ProductSerializer
# from rest_framework import mixins
# from rest_framework import generics

# class CompanyList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class CompanyDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#     def get_object(self):
#         company_id = self.kwargs.get('company_id')
#         try:
#             return Company.objects.get(company_id=company_id)
#         except Company.DoesNotExist:
#             raise Http404

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



















# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser

# from phone_api.models import Company, Product
# from phone_api.serializers import CompanySerializer, ProductSerializer

# @csrf_exempt
# def company_list(request):
#     """
#     List all companies, or create a new one.
#     """
#     if request.method == 'GET':
#         companies = Company.objects.all()
#         company_serializer = CompanySerializer(companies, many=True)
#         return JsonResponse(company_serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         company_serializer = CompanySerializer(data=data)
#         if company_serializer.is_valid():
#             company_serializer.save()
#             return JsonResponse(company_serializer.data, status=201)
#         return JsonResponse(company_serializer.errors, status=400)


# @csrf_exempt
# def company_detail(request, company_id):
#     """
#     Retrieve, update or delete a company.
#     """
#     try:
#         company = Company.objects.get(company_id=company_id)
#     except Company.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         company_serializer = CompanySerializer(company)
#         return JsonResponse(company_serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         company_serializer = CompanySerializer(company, data=data)
#         if company_serializer.is_valid():
#             company_serializer.save()
#             return JsonResponse(company_serializer.data)
#         return JsonResponse(company_serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         company.delete()
#         return HttpResponse(status=204)