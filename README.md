Devonthink 中文索引生成程序
===

<!-- TOC -->

- [原理](#原理)
- [安装及准备工作](#安装及准备工作)
    - [准备后台服务](#准备后台服务)
    - [准备前台服务 Alfred Workflow](#准备前台服务-alfred-workflow)
        - [关于 Python 2.X 的说明](#关于-python-2x-的说明)
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

<!--生成: `pipreqs . `-->

### 准备后台服务

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
* 没有购买 Alfred PowerPack 的，可以把 `Terminal Command` 中的代码添加为文本替换。

```bash
python3 ~/DEVONthink-Chinese-Search/get_key_words.py
osascript -e 'tell app "Terminal" to close front window'
```

如果默认使用 iTerm 作为终端的话，则 Apple Script 部分要做适当的修改

```bash
python3 ~/DEVONthink-Chinese-Search/get_key_words.py
osascript -e 'tell app "iTerm2" to close front window'
```

#### 关于 Python 2.X 的说明

由于 macOS 的二进制保护限制，直接使用 pip 指定安装模块是不会成功的，所以我没有采用 2.x ，而是采用我能随意使用的 3.x。
代码（稍作修改？）应该可以在 2.x 下运行，并且 2.x 下的代码有 Alfred 的直接支持，[Alfred 在 macOS 有系统集成 3.x 之前不考虑支持 3.x](http://alfredworkflow.readthedocs.io/en/latest/supported-versions.html#why-no-python-3-support)，我也没办法。


## 重要更新记录

> 2018-01-31 更新

2.0 更新啦
实现了一个简单的 POST 接口，通过后台运行一个小型服务器，大幅降低提取关键词耗时（主要是结巴分词初始化耗时）

## 待完成

- [ ] 简化安装工作


