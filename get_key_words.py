#coding=utf-8
#! /usr/local/bin/python3

import string
import jieba.analyse
import pyperclip
import re

# 过滤
def filter_chinese(text):
	#r = re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\\\！\@\#\\\&\*\%]", "", s)
	r = re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\：\。\，\“\“\_\-\”\▃\？\、\/n\─\;\'\,\[\]\.\<\>\/\?\~\\《\》\）\\\（\\！\@\#\\\&\*\%]", "", text)
	r = r.replace(' ', '')
	return r

def copy_to_clipboard(keywords,method=','):
	# 可以用 其他标点符号替换 替换
	method = ",";
	#print(str.join( seq ))
	output_str = method.join(str(keywords[0]))
	return output_str

#TODO
# 完善分词方式，可以自由使用 THULAC ／ 结巴分词，这个也要变成一个函数
# 根据字符串长度先估计运行时间，再执行分词程序的初始化 2017-04-21 22:06:18

# 这部分根据个人需求修改 2017-04-25 10:27:16
# 0 → 增加一步清华分词
# 其他 → 结巴分词直接提取关键词，没有区别
def cut(content, method=1):
	if method == 0:
		import thulac
		thu1 = thulac.thulac(seg_only=True,filt=True)
		words = thu1.cut(content, text=True)  #进行一句话分词
	else:
		words = content
	return words

#TODO
# 优化关键词过滤方式
# 参数可更改
def filter_keywords(keywords):
	final_keywords = []
	loop_times = len(keywords)
	#print(loop_times)
	#print(keywords)

	count = 0
	bias = 0
	for words in keywords:
		if count+4 <= len(keywords)/2:
			k = -(keywords[count+4][1]-words[1])/3
			if k < 0.003:
				bias = words[1]
				print(bias)
				break

		count = count + 4

	for item in keywords:
		if item[1]>bias:
			final_keywords.append(item[0])
			print(item[0],item[1])
	return final_keywords


def get_key_words(content):

	# 冲洗字符串，只留下汉字
	content = filter_chinese(content) # 过滤

	# 假设单词平均长度2 估计最多有多少词，
	text_length = len(content)
	words_num_max = int(text_length/2)

	# 分词
	words = cut(content,method=1)

	# 获取关键词
	keywords = jieba.analyse.extract_tags(words, topK=words_num_max, withWeight=True, allowPOS=( ))

	# 对关键词进行筛选
	final_keywords = filter_keywords(keywords)

	# 去除无用的符号
	final_keywords = str(final_keywords).replace('\'','')
	final_keywords = str(final_keywords).replace('[','')
	final_keywords = str(final_keywords).replace(']','')

	# 拷贝到剪贴板
	pyperclip.copy(final_keywords)

if __name__ == '__main__':
	content = str(pyperclip.paste())
	get_key_words(content)
