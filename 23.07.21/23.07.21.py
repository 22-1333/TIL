# 1 
'''
import requests

url = "https://fakestoreapi.com/carts"
response = requests.get(url)

print(response.json())
'''

# 2
'''
import json

# json data
json_data = """
{
    "name" : "ssafy kim",
    "age" : 28,    
    "hobbies" : [
        "study", 
        "review"
        ]
}
"""

# JSON data parsing
data = json.loads(json_data)

# JSON 데이터에서 원하는 데이터만 가져오기
name = data.get("name")

print(name)
'''

