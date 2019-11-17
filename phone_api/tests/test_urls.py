from django.urls import reverse, resolve


def test_company_products_url():
    path = reverse('company-products')
    print('oi', resolve(path).view_name)
    assert resolve(path).view_name == 'company-products'