"""获取关键词"""
# coding=utf-8
#! /usr/local/bin/python3

import re

import jieba.analyse
import jieba
import pyperclip

from collections import Counter


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


def get_key_words(content='', back_ground=False):
    """get_key_words"""
    if back_ground:
        content = str(pyperclip.paste())
    # 冲洗字符串，只留下汉字
    content = filter_chinese(content)

    # 假设单词平均长度 1.5 估计最多有多少词，
    text_length = len(content)
    words_num_max = int(text_length / 1.5)

    # 分词
    words = cut(content, method=1)

    # 获取关键词: textrank or extract_tags
    keywords = jieba.analyse.textrank(words, topK=words_num_max, withWeight=True, allowPOS=(
        'n', 'nr', 'nr1', 'nr2', 'nrj', 'nrf', 'ns', 'nsf', 'nt', 'nz', 'nl', 'ng'))

    # 对关键词进行筛选
    final_keywords = filter_keywords(keywords)
    print('solution')
    print(';'.join(final_keywords))
    final_keywords = ';'.join(final_keywords)

    searchable = list(dict(Counter(list(jieba.cut_for_search(final_keywords)))).keys())
    searchable.remove(';')
    if back_ground:
        # 拷贝到剪贴板
        pyperclip.copy(','.join(searchable))
    return ','.join(searchable)

# if __name__ == '__main__':
#   content = str(pyperclip.paste())
#   get_key_words(content)
