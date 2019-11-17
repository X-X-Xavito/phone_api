import pytest

from phone_api.models import Company, Product, Recharge

pytestmark = pytest.mark.django_db

@pytest.fixture
def test_company():
    """
        Return a company instance
    """
    company = Company(company_id="test_company")
    return company

@pytest.fixture
def test_product():
    """
        Return a product instance
    """
    company = Company(company_id="test_company")
    product = Product(product_id="test_product", company_id=company, value=10.0)
    return product


@pytest.fixture
def test_recharge():
    """
        Return a recharge instance
    """
    company = Company(company_id="test_company")
    product = Product(product_id="test_product", company_id=company, value=10.0)
    recharge = Recharge(company_id=company, product_id=product, phone_number="5511999999999", value=product.value)
    return recharge

def test_company_company_id(test_company):
    assert type(test_company.company_id) is str

def test_product_product_id(test_product):
    assert type(test_product.product_id) is str

def test_recharge_attr(test_recharge):
    assert type(test_recharge.phone_number) is str
    assert type(test_recharge.value) is float
