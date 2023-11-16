from .models import Product
from .serializers import ProductSerializer
import requests

from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


api_key = "e5e0736b9ac19664efbcdfffd52e7e29"


def initial_deposit_list(request):
    page_num = 1
    api_url = f"https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={page_num}"
    response = requests.get(api_url).json()

    max_page = response['result']['max_page_no']

    for page in range(1, max_page + 1):
        page_num = page
        response = requests.get(api_url).json()

        for product in response['result']['baseList']:
            serializer = ProductSerializer(data=product)
            if serializer.is_valid(raise_exception=True):
                serializer.save(product_type=0)


def initial_installment_saving_list(request):
    page_num = 1
    api_url = f"https://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={page_num}"
    response = requests.get(api_url).json()

    max_page = response['result']['max_page_no']

    for page in range(1, max_page + 1):
        page_num = page
        response = requests.get(api_url).json()

        for product in response['result']['baseList']:
            serializer = ProductSerializer(data=product)
            if serializer.is_valid(raise_exception=True):
                serializer.save(product_type=1)


# Create your views here.
@api_view(['GET'])
def deposit_list(request):
    page_num = 1
    api_url = f"https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={page_num}"
    response = requests.get(api_url).json()
    max_page = response['result']['max_page_no']

    for page in range(1, max_page + 1):
        page_num = page
        response = requests.get(api_url).json()

        for product in response['result']['baseList']:
            try:
                existed_product = Product.objects.get(fin_prdt_cd=product['fin_prdt_cd'])
                continue
            except:
                product["product_type"] = 0
                serializer = ProductSerializer(data=product)
                if serializer.is_valid():
                    serializer.save()
    
    serializer = ProductSerializer(get_list_or_404(Product, product_type=0), many=True)

    return Response(serializer.data)


@api_view(['GET'])
def installment_saving_list(request):
    page_num = 1
    api_url = f"https://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={page_num}"
    response = requests.get(api_url).json()
    max_page = response['result']['max_page_no']

    for page in range(1, max_page + 1):
        page_num = page
        response = requests.get(api_url).json()

        for product in response['result']['baseList']:
            try:
                existed_product = Product.objects.get(fin_prdt_cd=product['fin_prdt_cd'])
                continue
            except:
                product["product_type"] = 1
                serializer = ProductSerializer(data=product)
                if serializer.is_valid():
                    serializer.save()
    
    serializer = ProductSerializer(get_list_or_404(Product, product_type=1), many=True)

    return Response(serializer.data)


@api_view(['GET'])
def detail(request, fin_prdt_cd):
    serializer = ProductSerializer(get_object_or_404(Product, fin_prdt_cd=fin_prdt_cd))

    return Response(serializer.data)
