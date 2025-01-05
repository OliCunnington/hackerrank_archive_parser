import json
import os


if __name__ == "__main__":
    type_dict = {}
    with open("./hackerrank_archive_parser/ofcunnington_data_format.json") as f:
        parsed = json.load(f)
        for k in parsed["submissions"]:
            lang = k["language"].replace("[", "").replace("]", "").replace("\\", "").replace(" ", "_").replace(",", "").replace("\"", "")
            if lang not in type_dict.keys():
                type_dict[lang] = [k["challenge"].lower().replace(" ", "_")]
            else:
                type_dict[lang] += [k["challenge"].lower().replace(" ", "_")]
        print(json.dumps(type_dict, indent=4))
        for d in type_dict.keys():
            print(d, ": ", len(type_dict[d]))
            path = "./hackerrank/" + d
            if not os.path.exists(path):
                os.makedirs(path)
        # for k in parsed["submissions"]:
            # type_dict[k["language"]].append(k["code"])
        # print(json.dumps(type_dict, indent = 4))