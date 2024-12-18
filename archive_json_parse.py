import json

if __name__ == "__main__":
    with open("ofcunnington_data.json") as f:
        parsed = json.load(f)
    with open("ofcunnington_data_format.json", "w") as f:
        f.write(json.dumps(parsed, indent=4))