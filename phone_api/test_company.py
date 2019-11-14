import pytest

from .models import Company, Product, Recharge


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
    company = test_company()
    product = Product(product_id="test_product", company_id=company, value=10.0)
    return product

def test_company_company_id(test_company):
    assert test_company.company_id is str