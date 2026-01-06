from django.http import JsonResponse
from .models import Product

def product_list(request):
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)

def product_create(request):
    product = Product.objects.create(
        name="Sample",
        price=10.00
    )
    return JsonResponse({"id": product.id})