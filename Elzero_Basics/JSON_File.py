# #  JSON => JavaScript Object Notation
# # json.loads() String to Dict : Load String
# # json.dumps() Dict to String : Dump String
# # json.load() String to Dict : Load String => write to file.json
# # json.dump() Dict to String : Dump String => read from file.json
# with open("data.json", "w") as f:
#     json.dump(my_dict, f)
import json
from datetime import datetime

#
# # JSON String => '{"srt":"str".......}'
# json_text = '{"name": "Tesla", "year": 2024}'
#
# car_dict = json.loads(json_text)
# # print(car_dict["name"])
# for key, value in car_dict.items():
#     print(f"{key}: {value}")
# #  Convert Dict To JSON String
# new_json = json.dumps(car_dict)
# print(type(new_json))  # <class 'str'>
# print(new_json)
# # Try | Except | JSON
# bad_json = '{"name": "Ahmad", "age": 23 '
# try:
#     data = json.loads(bad_json)
# except json.JSONDecodeError:
#     print("Error: This is not a valid JSON string!")
# # Test
car_json = '{"brand": "Tesla", "production_date": "2020-01-01"}'
car_dict = json.loads(car_json)
# print(car_dict["production_date"])
car_time = car_dict.get("production_date")
date_object = datetime.strptime(car_time, "%Y-%m-%d")
# print(date_object)
# print(type(date_object))  # <class 'datetime.datetime'>
time_now = datetime.now()
car_lunch = time_now - date_object
print(f"Car Lunched {car_lunch.days} day(s) Ago ")
# -------------------------------------------------

data = {"brand": "Tesla", "model": "S", "year": 2024}

#  indent: {"brand": "Tesla", "model": "S", "year": 2024}
#  indent=4
print(json.dumps(data, indent=4))
print(json.dumps(data, indent=4, sort_keys=True))
# lowest size
print(json.dumps(data, separators=(',', ':')))
