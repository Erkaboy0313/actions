import pytest
from .models import Product

pytestmark = pytest.mark.django_db

def test_product_creation():
    product = Product.objects.create(
        name="Test Product",
        price=25.50
    )
    assert product.id is not None
    assert product.name == "Test Product"

def test_product_list(client):
    Product.objects.create(name="P1", price=10)
    response = client.get("/products/")
    assert response.status_code == 200
    assert len(response.json()) == 1
