import os

import yaml


def analyze_yaml(file_name, keyword):
    # file_path = os.path.join(os.path.dirname(os.getcwd()), "data", file_name)
    file_path = os.path.join(os.getcwd(), "data", file_name)
    print(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        dict_data = data[keyword]
        list_data = list()
        for i in dict_data.values():
            list_data.append(i)
    return list_data





if __name__ == "__main__":
    print(analyze_yaml("login_data.yaml"))
