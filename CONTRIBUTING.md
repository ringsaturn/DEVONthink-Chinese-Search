欢迎帮助完善 DEVONthink-Chinese-Search
---

[TOC]

# 未来的期待

* 有更好的交互方式
* 和 Apple Script 联动，做到能批量读取笔记内容并添加索引 
* 尝试用 JavaScript 实现 DEVONthink 的脚本，方便没有 Alfred 的用户使用
* 更好的 Shell 脚本
* 更好的提取关键词算法

努力让 DEVONthink 的中文用户更舒服地使用这款软件

# 整体架构

我考虑过在后台部署一个服务，使用时发出一个特定的请求，自动获取剪贴板并把关键词粘贴到剪贴板中，但是这样做的实现方式与逻辑我没有想好，所以就使用了中规中矩的 API 调用的办法

API 使用 POST 是考虑到我的部分笔记文字数量大，用 GET 就容易超出限制

# 后台

Flask 架起的服务，在 [`AnalyzeKeyWordsAPI/Server.py`](https://github.com/ringsaturn/DEVONthink-Chinese-Search/blob/master/AnalyzeKeyWordsAPI/Server.py) 中

调用 [提取关键词](https://github.com/ringsaturn/DEVONthink-Chinese-Search/blob/master/AnalyzeKeyWordsAPI/AnalyzeKeyWords.py) 基于结巴分词的 `jieba.analyse` 模块，函数及说明请参见代码

# 前台 API 调用

## cURL + Python 3范例

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
        url="http://127.0.0.1:5050/get_key_words",
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
curl -H "Content-Type: application/json" -X POST -d '{"notes_content":"'""$notes_content""'"}' http://127.0.0.1:5050/get_key_words | pbcopy
```

Shell 脚本这块我并不熟练只能说写出了一个马马虎虎能用的实现方式

## 请求参数

本部分由 Paw 生成

### Header Parameters

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

### Body Parameters

- **body** should respect the following schema:

```
{
  "type": "string",
  "default": "{\"notes_content\":\"clipboard\"}"
}
```

