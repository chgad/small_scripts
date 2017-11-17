import json

# This skript is made to parse a file containing a JSON Array of objects like
#this :
#       {"header": <string>,
#        "description":<string>,
#        "id":<string>}
#To a form like the dummy_object where the fields are description, header and
#examples.

with open("glossary_json.json") as json_data:
    d = json.load(json_data)

container = list()

for obj in d:
    new = dummy_object = {
        "model": "stein.glossaryentry",
        "pk": "",
        "fields": {}
        }

    new["pk"] = obj["id"]
    del obj["id"]
    if "list" in obj:
        del obj["list"]

    new["fields"] = obj
    if "examples" in obj:
        new["fields"]["examples"] = obj["examples"]
    container.append(new)

ret = json.dumps(container)

with open("glossary_16_11_2017.json", "w") as file:
    file.write(ret)


