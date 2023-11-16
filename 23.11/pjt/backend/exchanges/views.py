import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view


api_key = "RZTrSGYN7RnSDdMdZI57R2rWwGYEXTAD"


# Create your views here.
@api_view(['GET'])
def exchange_calculator(request, cur_unit):
    api_url = f"https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&data=AP01"
    response = requests.get(api_url).json()

    for exchange_info in response:
        if exchange_info['cur_unit'] == cur_unit:
            string_won = exchange_info['bkpr']
            
            if ',' in string_won:
                new_won = int("".join(string_won.split(',')))
            else:
                new_won = int(string_won)
            data = {'rate': new_won}

            return Response(data)
