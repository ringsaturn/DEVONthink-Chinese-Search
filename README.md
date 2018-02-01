Devonthink 中文索引生成程序 后台剪贴板分支
===

<!-- TOC -->

- [关于这个分支](#关于这个分支)
- [原理](#原理)
- [安装及准备工作](#安装及准备工作)
    - [准备后台服务](#准备后台服务)
    - [准备前台服务 Alfred Workflow](#准备前台服务-alfred-workflow)
- [重要更新记录](#重要更新记录)
- [待完成](#待完成)

<!-- /TOC -->

## 关于这个分支

这个分支的实现效果是：服务器端收到请求即会调用提取关键词服务，从服务器所在的系统提取关键词


## 原理

一句话解释：调用结巴分词从文本中提取关键词，详情：[fxsjy/jieba: 结巴中文分词](https://github.com/fxsjy/jieba)

* 初始化后台服务: 运行一个小型服务器，提供基于[结巴分词]((https://github.com/fxsjy/jieba))的关键词提取 API
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

* 快捷键需要自定义

## 重要更新记录

> 2018-01-31 更新

2.0 更新啦
实现了一个简单的 POST 接口，通过后台运行一个小型服务器，大幅降低提取关键词耗时（主要是结巴分词初始化耗时）

> 2018-01-31 晚间更新

2.1 更新啦
利用 shell 脚本和 cURL 实现了一个更好的获取请求速度

## 待完成

- [ ] 简化安装工作


