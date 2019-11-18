from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from phone_api.views import CompanyListAPIView


def test_company_products_methods():
    path = reverse('company-products')
    request = RequestFactory().get(path)
    request.user = User

    response = CompanyListAPIView()
    assert response.allowed_methods == ['GET', 'OPTIONS']

