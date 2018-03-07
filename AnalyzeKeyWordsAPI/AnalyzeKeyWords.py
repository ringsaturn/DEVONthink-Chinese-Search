"""获取关键词"""
# coding=utf-8
#! /usr/local/bin/python3

import re
from collections import Counter

import jieba.posseg as pseg
import pyperclip


def filter_chinese(text):
    """去除标点符号"""
    get_zh_en = re.compile("[^\u4e00-\u9fa5.^a-z^A-Z^0-9]")
    get_zh = re.compile(("[A-Za-z0]"))
    return get_zh.sub(" ", get_zh_en.sub(" ", text))

def copy_to_clipboard(keywords, method=','):
    """拷贝到剪贴板"""
    # 可以用 空格 替换
    method = ","
    #print(str.join( seq ))
    output_str = method.join(str(keywords[0]))
    return output_str


def cut(content, method=1):
    """seg"""
    if method == 0:
        import thulac
        thu1 = thulac.thulac(seg_only=True, filt=True)
        words = thu1.cut(content, text=True)  # 进行一句话分词
    else:
        words = content
    return words


def filter_keywords(keywords):
    """过滤关键词"""
    final_keywords = []
    print(keywords)

    count = 0
    bias = 0
    for words in keywords:
        # print(words)
        if count + 4 <= len(keywords) / 2:
            k = -(keywords[count + 4][1] - words[1]) / 3
            if k < 0.003:
                bias = words[1]
                # print(bias)
                break

        count = count + 4

    for item in keywords:
        if item[1] > bias:
            final_keywords.append(item[0])
            print(item[0], item[1])
    return final_keywords

def ifin(noun_list, input_str):
    """判断词性是否是目标词性"""
    symbol = 1
    for item in noun_list:
        if item in input_str:
            symbol = symbol*0
    # if symbol = 0:
    return not bool(symbol)

def analyse(input_str):
    """output kws"""
    kws = []
    # 在这里修改词性
    noun = ['nr', 'ns', 'nt', 'nz']
    for pair in pseg.cut(input_str):
        pair = list(pair)
        # if 'n' in str(pair[-1]):
        if ifin(noun, pair[-1]):
            # print(pair[-1])
            kws.append(pair[0])
    # kws = ','.join(kws)
    # kws = jieba.lcut_for_search(kws)
    return kws

def get_keywords(content='', back_ground=False):
    """get_keywords"""
    if back_ground:
        content = str(pyperclip.paste())
    # 冲洗字符串，只留下汉字
    content = filter_chinese(content)
    # print(content)
    searchable = analyse(content)
    searchable = list(dict(Counter(list(searchable))).keys())

    final_kws = []
    for item in searchable:
        if len(item) >= 2:
            # print(item)
            final_kws.append(item)
    searchable = list(final_kws)
    searchable = ','.join(searchable)
    if ', ,' in searchable:
        searchable = searchable.replace(', ,', ',')
    if back_ground:
        # 拷贝到剪贴板
        pyperclip.copy(searchable)
    return searchable

# if __name__ == '__main__':
#   content = str(pyperclip.paste())
#   get_keywords(content)
