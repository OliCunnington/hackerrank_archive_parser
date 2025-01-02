import json

'''
take archive - arg
get uniq list string names / languages
replace " " and "/" with "_"
create dir for ea
take challenge name
replace " " and "/" with "_"
create/write code file
done?
'''

if __name__ == "__main__":
    with open("ofcunnington_data.json") as f:
        parsed = json.load(f)
    with open("ofcunnington_data_format.json", "w") as f:
        f.write(json.dumps(parsed, indent=4))