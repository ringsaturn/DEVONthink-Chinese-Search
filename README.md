DEVONthink 中文索引生成程序
===

<!-- TOC -->

- [使用须知](#使用须知)
- [原理](#原理)
- [用法](#用法)
- [安装及准备工作](#安装及准备工作)
    - [准备后台服务](#准备后台服务)
    - [准备前台服务 Alfred Workflow](#准备前台服务-alfred-workflow)
- [其他](#其他)
- [待完成](#待完成)
- [重要更新记录](#重要更新记录)

<!-- /TOC -->

## 使用须知

这个方法并不能解决 DEVONthink 面对中文文本时孱弱的语义理解能力，只能做到**改善** DEVONthink 的索引能力

## 原理

一句话解释：调用结巴分词从文本中提取关键词，并手动把关键词填入 Comments 中，供 DEVONthink 索引
结巴分词详情：[fxsjy/jieba: 结巴中文分词](https://github.com/fxsjy/jieba)

具体解释如下：
DEVONthink 的索引文件是一个个形如 `......-126376F59F4F.dtp2` 的文件，其中包含了文件的元数据与可供索引的信息。由于 DEVONthink 不支持对中文等非拉丁语言进行分词，所以无法直接搜索关键词。对于 DEVONthink 而言，每一句话（前后是标点符号的即分割为一句话）就是一个单词，这对于中文肯定是不行的。我知道有一种变通的方法通过用 `*` 来分开每隔汉字，从而获得较好的搜索结果体验。这种方法带来的问题是，搜索起来太不直观了。解决方法就是尽可能完善相应项目的 Spotlight Comments，把可供 DEVONthink 索引的词填入进去即可。这也正是这个程序的目的，生成搜索关键词

<!-- 结巴提供了两种关键词提取的方法
* [基于 TF-IDF 算法的关键词抽取](https://github.com/fxsjy/jieba#基于-tf-idf-算法的关键词抽取)
* [基于 TextRank 算法的关键词抽取](https://github.com/fxsjy/jieba#基于-textrank-算法的关键词抽取)

本程序在此基础上增加了一个简单的过滤功能，试图去除掉不能有效改进搜索的词 -->

* 默认关键词都是名词
* 计算相邻的两个词权重下降幅度即斜率是否小于阈值

<!-- 并且在提取关键词后进行了再分词，提高召回率 -->


## 用法

* 初始化后台服务: 运行一个小型服务器，提供基于[结巴分词](https://github.com/fxsjy/jieba)的关键词提取 API
* 复制笔记内容
* 前台调用 API 并把结果返回到剪贴板
* 在相应笔记的 Spotlight Comments 处粘贴剪贴板内容（可以通过 `Command+Shift+I` 打开）

需要注意的是，程序默认提取的关键词都是名词，如果有别的需要，则需要修改[对应部分](https://github.com/ringsaturn/DEVONthink-Chinese-Search/blob/master/AnalyzeKeyWordsAPI/AnalyzeKeyWords.py#L75)的词性

## 安装及准备工作

### 准备后台服务
<!--生成: `pipreqs . `-->
所有路径均默认在用户的根目录下

```bash
git clone https://github.com/ringsaturn/DEVONthink-Chinese-Search

cd DEVONthink-Chinese-Search

# 安装依赖
pip3 install -r requirements.txt

# 启动服务器
# 默认使用 5050 端口
# 重启/注销后需要再次执行这个命令
screen python3 AnalyzeKeyWordsAPI/Server.py
```

### 准备前台服务 Alfred Workflow

推荐使用 `get keywords 后台模式.alfredworkflow`

## 其他

* 如果想提建议，发 issues 即可
* 如果向帮助改进/增加其他的入口，还请移步 [CONTRIBUTING](https://github.com/ringsaturn/DEVONthink-Chinese-Search/blob/master/CONTRIBUTING.md) 了解具体的参数
* 也欢迎发邮件 ringsaturn.me@gmail.com

## 待完成

- [ ] 简化安装工作

## 重要更新记录

**2018-01-31 更新 2.0**

实现了一个简单的 POST 接口，通过后台运行一个小型服务器，大幅降低提取关键词耗时（主要是结巴分词初始化耗时）

----
**2018-01-31 晚间更新 2.1**

利用 shell 脚本和 cURL 实现了一个更好的获取请求速度

----
**2018-02-01 更新 2.2**

增加一个后台功能，在后台读取剪贴板内容并把关键词粘贴回剪贴板

----
**2018-02-21 更新 2.3b**

从 2.3 开始，提取关键词流程做了改变

- 输入文本整体进行分词并标注词性
- 过滤出名词词性
- 搜索引擎模式再分词

做出这个改变的原因是，在测试中发现结巴分词的提取关键词功能是基于词频的，语义上重要的词语并没有提取出来，故不进行根据权重的提取，试图用搜索引擎模式提高召回率

更新后的效果还有待观察。

----
**2018-03-01 更新 2.3**

- 移除搜索引擎模式
    - 如果有一天找到了直接修改 DEVONthink 索引文件的方法就直接修改索引文件了
    - Spotlight Comments 应当留给自己做一些备忘性质的记录。使用搜索引擎模式太乱了
- 修复词性过滤问题，默认过滤出：
    - nr 人名
    - ns 地名
    - nt 机构团体
    - nz 其他专名

参考：词性简介参见 [jieba（结巴）分词种词性简介](http://blog.csdn.net/suibianshen2012/article/details/53487157)
