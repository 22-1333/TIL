from django.http import JsonResponse
from rest_framework.decorators import api_view
import pandas as pd
import heapq

@api_view(['GET'])
def top_ten(request):
    df = pd.read_csv("data/test_data_has_null.CSV", encoding='cp949')
    df["나이"] = df["나이"].fillna("NULL")
    datas = df.to_dict("records")

    total_age = 0
    total_people = 0

    for data in datas:
        if data["나이"] == "NULL":
            continue 

        total_age += data["나이"]
        total_people += 1

    average_age = total_age / total_people

    heap = []
    age_list = []
    for index, data in enumerate(datas):
        if data["나이"] == "NULL":
            continue
        
        heapq.heappush(heap, (abs(average_age - data["나이"]), index))

    age_list.sort()

    top_10 = []
    for _ in range(10):
        age, index = heapq.heappop(heap)
        
        top_10.append(datas[index])

    return JsonResponse({'dat': top_10})
