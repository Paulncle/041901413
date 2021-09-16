import re
import os
import sys
import pypinyin
import zhconv
from cnradical import Radical, RunOption
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag
radical = Radical(RunOption.Radical)


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


def form_re(word: str):
    if word.encode("utf-8").isalpha():
        # 判断是不是英文
        alpha = []
        for i in word:  # 得到每个字母
            alpha.append(i)
        return '.{0,20}'.join(alpha)
    else:
        wordlist = []
        # 同音字
        dagparams = DefaultDagParams()
        tyz = [''.join(p.path) for p in dag(dagparams, pypinyin.lazy_pinyin(word), path_num=500)]  # 找全部同音字

        for index in range(len(word)):
            i = word[index]
            # 偏旁
            a = [i, radical.trans_ch(i)]
            # 拼音
            py = pypinyin.lazy_pinyin(i)[0]
            a.append(py)
            a.append(py[0])
            # 繁体字
            traditional = zhconv.convert(i, 'zh-tw')
            if traditional != i:
                # 判断繁体是否与原中文不同
                a.append(traditional)
            # 同音字
            for w in tyz:
                a.append(w[index])

            wordlist.append("(?:"+"|".join(a)+")")
        return '.{0,20}?'.join(wordlist)


def main():
    path_words = str(sys.argv[1])  # 敏感词库的绝对路径
    path_org = str(sys.argv[2])  # 待检测文件的绝对路径
    if not os.path.exists(path_words):
        print("file doesn't exist")
        exit()
    if not os.path.exists(path_org):
        print("file doesn't exist")
        exit()
    path_ans = str(sys.argv[3])  # 输出结果的ans文件
    words = get_words(path_words)
    contents = get_org(path_org)
    re_s = [form_re(i) for i in words]  # 生成敏感词的所有re表达式
    result = []
    for line_index in range(len(contents)):
        line = contents[line_index]
        line_index = line_index + 1
        for j in range(len(words)):
            re_ = re_s[j]
            for p in re.findall(re_, line, re.IGNORECASE):  # 遍历用正则表达式查找出每句中的敏感词
                result.append(f"Line{line_index}: <{words[j]}> {p}\n")
    with open(path_ans, 'w', encoding='utf-8') as f:  # 将结果写入输出文件
        f.write(f'Total: {len(result)}\n')
        for i in result:
            f.write(i)
        f.close()


if __name__ == '__main__':
    main()
