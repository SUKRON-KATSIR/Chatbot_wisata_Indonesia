import json
with open('./dataset/d.json', encoding="utf-8") as content:
    data = json.load(content)

print(data)
