import os
import re
import pypinyin
import zhconv
from cnradical import Radical, RunOption
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag
radical = Radical(RunOption.Radical)


def form_re(word: str):
    if word.encode("utf-8").isalpha():
        alpha = []
        for i in word:
            alpha.append(i)
        return '.{0,20}'.join(alpha)
    else:
        words = []
        dagparams = DefaultDagParams()
        tyz = [''.join(p.path) for p in dag(dagparams, pypinyin.lazy_pinyin(word), path_num=500)]

        for index in range(len(word)):
            i = word[index]
            a = [i, radical.trans_ch(i)]
            py = pypinyin.lazy_pinyin(i)[0]
            a.append(py)
            a.append(py[0])
            traditional = zhconv.convert(i, 'zh-tw')
            if traditional != i:
                a.append(traditional)
            for w in tyz:
                a.append(w[index])

            words.append("(?:"+"|".join(a)+")")
        return '.{0,20}?'.join(words)
