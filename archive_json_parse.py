import json
import os
import re


ext_dict = {
    "java" : ".java",
    "java8" : ".java",
    "python3" : ".py",
    "python" : ".py",
    "text" : ".txt",
    "[\"html\", \"js\", \"css\"]" : ".html",
    "mysql" : ".sql",
    "cobol" : ".cob",
    "oracle" : ".sql",
    "javascript" : ".js",
    "haskell" : ".hs"
}

if __name__ == "__main__":
    type_dict = {}
    with open("./hackerrank_archive_parser/ofcunnington_data_format.json") as f:
        parsed = json.load(f)
        for k in parsed["submissions"]:
            lang = k["language"].replace("[", "").replace("]", "").replace("\\", "").replace(" ", "_").replace(",", "").replace("\"", "")
            c_name = k["challenge"].lower().replace(" ", "_").replace("\"", "").replace("\'", "").replace("?", "").replace("!", "").replace(",", "").replace(".", "").replace("\\", "").replace("\\\"", "").replace(":", "-").replace("/", "-") + ext_dict[k["language"]]
            if lang not in type_dict.keys():
                type_dict[lang] = {c_name : k["code"]}
            else:
                if c_name not in type_dict[lang].keys():
                    type_dict[lang][c_name] = k["code"]
                else:
                    c_name_num = k["challenge"].lower().replace(" ", "_").replace("\"", "").replace("\'", "").replace("?", "").replace("!", "").replace(",", "").replace(".", "").replace("\\", "").replace("\\\"", "").replace(":", "-").replace("/", "-") + str(len(re.findall(c_name, str(type_dict[lang].keys())))) + ext_dict[k["language"]]
                    type_dict[lang][c_name_num] = k["code"]
        

        for d in type_dict.keys():
            print(d, ": ", len(type_dict[d]))
            path = "./hackerrank/" + d
            ### make dirs
            if not os.path.exists(path):
                os.makedirs(path)
            ### make & write files
            for f in type_dict[d]:
                with open(path + "/" + f, "w") as file:
                    file.write(type_dict[d][f])