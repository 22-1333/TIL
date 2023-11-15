from .models import Product
from .serializers import ProductSerializer
import requests

from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework import status



# Create your views here.
def deposit_list(request):
    api_key = ""
    api_url = f"http://finlife.fss.or.kr/finlife/fdrmDpstApi/list.json?auth={api_key}&topFinGrpNo=020000&pageNo={page_num}"
    page_num = 1
    response = requests.get(api_url).json()

    max_page = response.result.max_page_no

    product_list = get_list_or_404(Product)

    for page in range(1, max_page + 1):
        page_num = page
        response = request.get(api_url).json()

        for product in response.baseList:
            try:
                product_list.get(fin_prdt_cd=product.fin_prdt_cd)
                continue
            except:
                serializer = ProductSerializer(data=product.baseList)
                if serializer.is_valid():
                    serializer.save(product_type=0)

    serializer = ProductSerializer(get_list_or_404(Product), many=True)
    return Response(serializer.data)
    

def installment_saving_list(request):
    pass
