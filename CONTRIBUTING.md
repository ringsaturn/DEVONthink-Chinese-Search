欢迎帮助完善 DEVONthink-Chinese-Search
===

<!-- TOC -->

- [未来的期待](#未来的期待)
- [整体架构](#整体架构)
- [后台](#后台)
- [前台 API 调用](#前台-api-调用)
    - [后台模式](#后台模式)
        - [后台模式 范例](#后台模式-范例)
    - [API 模式](#api-模式)
        - [API 模式 范例](#api-模式-范例)
        - [请求参数](#请求参数)
            - [Header Parameters](#header-parameters)
            - [Body Parameters](#body-parameters)

<!-- /TOC -->

# 未来的期待

* 有更好的交互方式
* 和 Apple Script 联动，做到能批量读取笔记内容并添加索引
* 尝试用 JavaScript 实现 DEVONthink 的脚本，方便没有 Alfred 的用户使用
* 更好的 Shell 脚本
* 更好的提取关键词算法

努力让 DEVONthink 的中文用户更舒服地使用这款软件

# 整体架构

后台提供解析 + 前台发出请求

前台调用有两种工作模式

- [后台模式](#后台模式)
- [API 模式](#api-模式)


# 后台

Flask 架起的服务，在 [`AnalyzeKeyWordsAPI/Server.py`](https://github.com/ringsaturn/DEVONthink-Chinese-Search/blob/master/AnalyzeKeyWordsAPI/Server.py) 中

调用 [提取关键词](https://github.com/ringsaturn/DEVONthink-Chinese-Search/blob/master/AnalyzeKeyWordsAPI/AnalyzeKeywords.py) 基于结巴分词的 `jieba.analyse` 模块，函数及说明请参见代码

# 前台 API 调用

前台调用有两种模式

* 后台模式：服务端调用本地剪贴板（需要服务端和用户端都在同一台电脑上）
* API 模式：通过 API 传递内容

## 后台模式

后台模式只需要在 POST 时，在 Body 部分 `back_ground` 值为 `True`

```python
{
    "back_ground": True
}
```

### 后台模式 范例

在这个模式下，向服务端发出请求即可以调用剪贴板

由 Paw 生成如下代码

Python 3

```python

import requests
import json

response = requests.post(
            url="http://127.0.0.1:5050/get_keywords",
            headers={
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({
                "back_ground": True
            })
        )

```

cURL

```sh
## Request
# 基于结巴分词的关键词提取服务器 API 请求
curl -X "POST" "http://127.0.0.1:5050/get_keywords" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "back_ground": True
}'
```

## API 模式

### API 模式 范例

Python 3

```python
"""通过 API 获取关键词"""
# ringsaturn

import json

import pyperclip as clip
import requests

def get_from_api(notes_content):
    """get keywords from API"""
    # Generate by Paw
    keywords = requests.post(
        url="http://127.0.0.1:5050/get_keywords",
        headers={
            "Content-Type": "application/json; charset=utf-8",
        },
        data=json.dumps({
            "notes_content": notes_content
        })
    ).text
    return keywords

if __name__ == '__main__':
    CONTENT = str(clip.paste())
    clip.copy(get_from_api(CONTENT))
```

cURL

```sh
notes_content=`pbpaste | tr '\n' ',' `
notes_content=${notes_content// /.}
notes_content=${notes_content//\"/.}
post_data="${notes_content}"
echo "$post_data"
curl -H "Content-Type: application/json" -X POST -d '{"notes_content":"'""$notes_content""'"}' http://127.0.0.1:5050/get_keywords | pbcopy
```

Shell 脚本这块我并不熟练只能说写出了一个马马虎虎能用的实现方式


### 请求参数

本部分由 Paw 生成

#### Header Parameters

- **Content-Type** should respect the following schema:

```
{
  "type": "string",
  "enum": [
    "application/json; charset=utf-8"
  ],
  "default": "application/json; charset=utf-8"
}
```

#### Body Parameters

- **body** should respect the following schema:

```
{
  "type": "string",
  "default": "{\"notes_content\":\"clipboard\"}"
}
```

