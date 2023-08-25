import requests

black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

dummy_data = []

for n in range(1, 11):

    # 무작위 유저 정보 요청 경로
    api_url = f'https://jsonplaceholder.typicode.com/users/{n}'
    # API 요청
    response = requests.get(api_url)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()

    lat = float(parsed_data["address"]["geo"]["lat"])
    lng = float(parsed_data["address"]["geo"]["lng"])

    if lat < 80 and lat > -80 and lng < 80 and lng > -80:
        name = parsed_data["name"]
        company_name = parsed_data["company"]["name"]

        dummy_dict = {"company" : company_name, "lat" : lat, "lng" : lng, "name" : name}

        dummy_data.append(dummy_dict)




def create_user(create_arg):
    censored_user_list = dict()
    user_list = dict()

    for user in create_arg:
        user_dict = {user["company"] : [user["name"]]}

        company = user["company"]
        name = user["name"]
        
        user_list.update(user_dict)

        if censorship(company, name):
            censored_user_list.update(user_dict)

    return censored_user_list

def censorship(company, name):
    
    if company in black_list:
        print(f"{company} 소속의 {name} 은/는 등록할 수 없습니다.")
        return False
    
    else:
        print("이상 없습니다.")
        return True

print(create_user(dummy_data))
