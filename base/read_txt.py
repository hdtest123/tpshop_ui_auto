import  os
def read_txt(file_name):
    file_path = os.path.join(os.getcwd(),"data", file_name)
    file_path = os.path.join(os.path.dirname(os.getcwd()), "data", file_name)
    print(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()


# 外借可以调用此方法，出入要解析的txt文件即可
def get_data(file):
    arr = []
    for data in read_txt(file):
        arr.append(tuple(data.strip().split(",")))
    return  arr[1:]

if __name__ == "__main__":
    print(get_data("user.txt"))






