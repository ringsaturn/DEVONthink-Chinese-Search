# Devonthink 中文索引生成程序说明

## 用法

1. 复制笔记内容（有图片，英文，等都可以，反正会被过滤掉）
2. 运行程序
3. 在相应笔记的 Spotlight Comments 处粘贴剪贴板内容（可以通过 Command+Shift+I 打开）

## 依赖

1.python 3.x<br>
2.[结巴分词](https://github.com/fxsjy/jieba): `pip3 install jieba` <br>
3.[pyperclip](https://github.com/asweigart/pyperclip): `pip3 install pyperclip`<br>

可选：根据个人需求而定，一般不用，详情见代码<br>
[thulac](https://github.com/thunlp/THULAC-Python): `pip install thulac`

关于 Python 2.x 的说明：

由于 macOS 的二进制保护限制，直接使用 pip 指定安装模块是不会成功的，所以我没有采用 2.x ，而是采用我能随意使用的 3.x。
代码（稍作修改？）应该可以在 2.x 下运行，并且 2.x 下的代码有 Alfred 的直接支持，[Alfred 在 macOS 有系统集成 3.x 之前不考虑支持 3.x](http://alfredworkflow.readthedocs.io/en/latest/supported-versions.html#why-no-python-3-support)，我也没办法。

## 函数说明

- `filter_chinese` 对输入的字符串，除掉英文字母，数字，空格，换行
- `copy_to_clipboard`：keywords 实际上是一个数组，所以输出的的格式应当调整成 Spotlight Comments 的格式，如 采用, 二进制, ......
- `cut` ：分词。这个⊂个人需求。比如一段文本，容易一起歧义的词汇较多，这时就需要用比较精准的分词方式先把词会分好，再提取关键词。不同的分词方式处理出的结果是不一样的，如图：

![](/jieba%20vs%20thulac.jpg)

- `filter_keywords`：对结巴分词提取出来的关键词进行过滤
- `get_key_words`：在这个函数里调用上述函数并传递变量

## 待完成

1. 代码中的 TODO 部分
2. 发布到 pip 中方便使用
