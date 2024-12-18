import json

if __name__ == "__main__":
    type_dict = {}
    with open("./ofcunnington_data_format.json") as f:
        parsed = json.load(f)
        for k in parsed["submissions"]:
            type_dict[k["language"]] = []
        print(type_dict)

        for k in parsed["submissions"]:
            type_dict[k["language"]].append(k["code"])
        print(json.dumps(type_dict, indent = 4))