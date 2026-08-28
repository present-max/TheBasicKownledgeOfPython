import json

user={
    "name": "John",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript"],
    "is_student": False
}
#将字典转换为JSON字符串
json_string = json.dumps(user)
print(json_string)
#将JSON字符串转换为字典
user_dict = json.loads(json_string)
print(user_dict)

#将字典转换为JSON字符串并保存到文件
with open("user.json", "w", encoding="utf-8") as f:
    json.dump(user, f)
print("JSON数据已保存到user.json文件中")
#从文件中读取JSON数据并转换为字典
with open("user.json", "r", encoding="utf-8") as f:
    user_dict = json.load(f)
print(user_dict)

