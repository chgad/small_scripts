import json

container = []

dummy_object = {
        "model":"stein.glossaryentry",
        "pk":"",
        "fields":{}
        }

with open("test_json.json") as json_data:
    d = json.load(json_data)

for obj in d:
    new = dummy_object
    new["pk"] = obj["id"]
    del obj["id"]
    new["fields"] = obj
    container.append(new)

print(container)
    
