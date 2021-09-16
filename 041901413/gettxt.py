import os


def get_words(path):
    string = ''
    file = open(path, 'r', encoding='UTF-8')
    words = []
    word = file.readline()
    while word:  # 循环读取words文件中的敏感词库
        string += word
        string = string.strip("\n")
        words.append(string)
        word = file.readline()
        string = ''
    file.close()
    return words


def get_org(path):
    file = open(path, 'r', encoding='UTF-8')
    org = []
    line = file.readline()
    while line:  # 循环读入文本
        string = line.strip("\n")  # 过滤掉换行符并将文本转为字符串
        org.append(string)
        line = file.readline()
    file.close()
    return org


def main():
    path_words = input("Path of words.txt：")
    path_org = input("Path of org.txt：")
    if not os.path.exists(path_words):
        print("There is no words file.")
        exit()
    if not os.path.exists(path_org):
        print("There is no org file.")
        exit()
    path_ans = input("Path of ans.txt:")
    context = get_org(path_org)
    words = get_words(path_words)


if __name__ == '__main__':
    main()
