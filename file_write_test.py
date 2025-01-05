import json

if __name__ == "__main__":
    with open("./ofcunnington_data_format.json") as f:
        parsed = json.load(f)
        test_code = parsed["submissions"][0]["code"]
        print(test_code)
        with open(
            parsed["submissions"][0]["challenge"].lower().replace(" ", "_") + "." + parsed["submissions"][0]["language"], 
            "w"
            ) as file:
            file.write(test_code)