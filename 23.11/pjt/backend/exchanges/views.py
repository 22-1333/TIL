import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view


api_key = "RZTrSGYN7RnSDdMdZI57R2rWwGYEXTAD"


# Create your views here.
@api_view(['GET'])
def exchange_calculator(request):
    api_url = f"https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&data=AP01"
    response = requests.get(api_url).json()

    for index, exchange_info in enumerate(response):
        string_money = exchange_info['bkpr']

        if ',' in string_money:
            new_money = int("".join(string_money.split(',')))
        else:
            new_money = int(string_money)
        
        response[index]['bkpr'] = new_money

    return Response(response)
