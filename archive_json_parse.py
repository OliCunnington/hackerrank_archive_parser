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


def _replace_space_and_slash(inString):
    return inString.replace(" ", "_").replace("/", "_")


'''
need a strategy for dealing with multiple challenge submissions
challegnes to not appear to have a submission date/time nor different scores

look ahead, or take batch...
contains() > 1

'''


'''

tuple for challenge name (with ext) and code breaks the increment for duplicate challenge submissions

dict wont work since keys().count wont return correct
    - seperate arrays?
    []
    []
    with a link between indecies?

    maybe dict with regex?
        count(name + "*") ?

'''