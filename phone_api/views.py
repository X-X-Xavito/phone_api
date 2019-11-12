from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from phone_api.models import Company, Product
from phone_api.serializers import CompanySerializer, ProductSerializer

@csrf_exempt
def company_list(request):
    """
    List all companies, or create a new one.
    """
    if request.method == 'GET':
        companies = Company.objects.all()
        company_serializer = CompanySerializer(companies, many=True)
        return JsonResponse(company_serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        company_serializer = CompanySerializer(data=data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse(company_serializer.data, status=201)
        return JsonResponse(company_serializer.errors, status=400)


@csrf_exempt
def company_detail(request, company_id):
    """
    Retrieve, update or delete a company.
    """
    try:
        company = Company.objects.get(company_id=company_id)
    except Company.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        company_serializer = CompanySerializer(company)
        return JsonResponse(company_serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        company_serializer = CompanySerializer(company, data=data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse(company_serializer.data)
        return JsonResponse(company_serializer.errors, status=400)

    elif request.method == 'DELETE':
        company.delete()
        return HttpResponse(status=204)