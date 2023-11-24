from .models import Product, Option
from .serializers import ProductSerializer, OptionSerializer
from accounts.models import User

import requests

from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.core import serializers

from rest_framework.response import Response
from rest_framework.decorators import api_view


api_key = "e5e0736b9ac19664efbcdfffd52e7e29"


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

                    for optionInfo in response['result']['optionList']:
                        if optionInfo["fin_prdt_cd"] == product["fin_prdt_cd"]:
                            optionProduct = get_object_or_404(Product, fin_prdt_cd=optionInfo["fin_prdt_cd"])
                            optionSerializer = OptionSerializer(data={'product': optionProduct.id, 'intr_rate_type': optionInfo["intr_rate_type"], 'save_trm': optionInfo["save_trm"], 'intr_rate': optionInfo['intr_rate'], 'intr_rate2': optionInfo['intr_rate2']})
                            if optionSerializer.is_valid(raise_exception=True):
                                optionSerializer.save()

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

                    for optionInfo in response['result']['optionList']:
                        print(optionInfo)
                        if optionInfo["fin_prdt_cd"] == product["fin_prdt_cd"]:
                            optionProduct = get_object_or_404(Product, fin_prdt_cd=optionInfo["fin_prdt_cd"])
                            optionSerializer = OptionSerializer(data={'product': optionProduct.id, 'intr_rate_type': optionInfo["intr_rate_type"], 'save_trm': optionInfo["save_trm"], 'intr_rate': optionInfo['intr_rate'], 'intr_rate2': optionInfo['intr_rate2']})
                            if optionSerializer.is_valid(raise_exception=True):
                                optionSerializer.save()
    
    serializer = ProductSerializer(get_list_or_404(Product, product_type=1), many=True)

    return Response(serializer.data)


@api_view(['GET'])
def detail(request, fin_prdt_cd):
    productSerializer = ProductSerializer(get_object_or_404(Product, fin_prdt_cd=fin_prdt_cd))
    optionSerializer = OptionSerializer(Product.objects.get(fin_prdt_cd=fin_prdt_cd).options.all(), many=True)

    return Response({'product': productSerializer.data, 'option': optionSerializer.data})


@api_view(['GET'])
def get_registered_list(request, type, username):
    user = get_user_model().objects.get(username=username)
    registered_list = []
    for product in user.registered_products.all():
        if product.product_type == type:
            registered_list.append(product.fin_prdt_cd)
    
    return Response({'registered_list': registered_list})


@api_view(['POST'])
def register(request, fin_prdt_cd, username):
    user = get_user_model().objects.get(username=username)
    product = Product.objects.get(fin_prdt_cd=fin_prdt_cd)

    if product in user.registered_products.all():
        user.registered_products.remove(product)
    else:
        user.registered_products.add(product)

    return HttpResponse("")


@api_view(['GET'])
def recommend_deposit_product(request, username):
    user = get_user_model().objects.get(username=username)

    duration = user.duration
    
    if duration < 90000:
        recommended_term = 12  
    elif duration < 180000:
        recommended_term = 24  
    else:
        recommended_term = 36  

    highest_rate_options = Option.objects.filter(save_trm=str(recommended_term)).order_by('-intr_rate2')[:3]

    recommended_product_info = []

    for option in highest_rate_options:
        product = option.product
        recommended_product_info.append({
            'fin_prdt_cd': product.fin_prdt_cd,
            'product_name': product.fin_prdt_nm,
            'company_name': product.kor_co_nm,
            'interest_rate': option.intr_rate2,
            'term': recommended_term
        })

    if recommended_product_info:
        return Response(recommended_product_info)
    else:
        return HttpResponse({"message": "추천할 상품이 없습니다."})


@api_view(['GET'])
def product_detail(request, fin_prdt_cd):
    try:
        product = Product.objects.get(fin_prdt_cd=fin_prdt_cd)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({'message': '상품을 찾을 수 없습니다.'}, status=404)