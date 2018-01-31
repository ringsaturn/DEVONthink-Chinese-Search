Devonthink 中文索引生成程序
===

<!-- TOC -->

- [原理](#原理)
- [安装及准备工作](#安装及准备工作)
    - [准备后台服务](#准备后台服务)
    - [准备前台服务 Alfred Workflow](#准备前台服务-alfred-workflow)
- [重要更新记录](#重要更新记录)
- [待完成](#待完成)

<!-- /TOC -->

## 原理

一句话解释：调用结巴分词从文本中提取关键词，详情：[fxsjy/jieba: 结巴中文分词](https://github.com/fxsjy/jieba)

* 初始化后台服务: 运行一个小型服务器，提供基于[结巴分词]((https://github.com/fxsjy/jieba))的关键词提取 API
* 复制笔记内容
* 前台调用 API 并把结果返回到剪贴板
* 在相应笔记的 Spotlight Comments 处粘贴剪贴板内容（可以通过 `Command+Shift+I` 打开）


## 安装及准备工作

### 准备后台服务
<!--生成: `pipreqs . `-->
所有路径均默认在用户的根目录下 如果在 `git clone` 这一步是在别的路径下执行的，则需要手动修改 Alfred Workflow 的相应的路径

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


