from django.urls import reverse, resolve


def test_company_products_url():
    path = reverse('company-products')
    assert resolve(path).view_name == 'company-products'