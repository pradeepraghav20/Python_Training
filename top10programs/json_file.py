# import json
# #
# # file_name = 'example.json'
# #
# # with open(file_name, 'r', encoding='utf-8') as f:
# #     # print(f)
# #     my_data = list(json.load(f))
# #     print(my_data)
# x={"id": 1, "name": "Alice", "age": 30}
# res=json.load(x)
# print(res)
# # import json
# #
# # data = [json.loads(line) for line in open('example.json', 'r', encoding='utf-8')]
# #
# # # 👇️ [{'id': 1, 'name': 'Alice', 'age': 30}, {'id': 2, 'name': 'Bob', 'age': 35}, {'id': 3, 'name': 'carl', 'age': 40}]
# # print(my_data)



import json

# some JSON:
# x =  '{"name":"John", "age":30, "city":"New York"}'
# x='{"id":'1', "name": "Alice", "age": '30'}'

# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# # parse x:
# y=json.dumps(x)
# print(y)
# # y = json.loads(x)
# # print(y)

import json
data = [json.loads(line) for line in open('example.json', 'r', encoding='utf-8')]
print(data[0])

import array



