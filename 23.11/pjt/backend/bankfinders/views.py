import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def nearest_bank(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')

    # 카카오 API를 사용하여 가장 가까운 은행 찾기
    SEARCH_API_URL = 'https://dapi.kakao.com/v2/local/search/category.json'
    headers = {'Authorization': 'KakaoAK [REST_API_KEY]'}
    params = {
        'category_group_code': 'BK9',  # 은행 카테고리 코드
        'x': longitude,
        'y': latitude,
        'radius': 2000,  # 2km 내에서 검색
        'sort': 'distance'  # 거리순 정렬
    }

    response = requests.get(SEARCH_API_URL, headers=headers, params=params)
    if response.status_code != 200:
        return JsonResponse({"error": "은행을 찾는데 실패했습니다."}, status=response.status_code)

    bank_data = response.json().get('documents', [])
    return JsonResponse(bank_data, safe=False)