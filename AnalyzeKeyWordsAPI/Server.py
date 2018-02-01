"""一个简单的获取关键词的本地 API 实现"""

# ringsaturn
# 2018-01-30 -> GET
# 2018-01-31 -> POST

from flask import Flask, request

from AnalyzeKeyWords import get_key_words

APP = Flask(__name__)

@APP.route("/get_key_words", methods=['POST'])
def get_key_words_api():
    """the API"""
    # 判断是否调用后台模式
    if 'back_ground' in request.json:
        if int(request.json['back_ground']) == 1:
            keywords = get_key_words(back_ground=True)
        else:
            input_notes_content = str(request.json['notes_content'])
            keywords = get_key_words(input_notes_content)
    else:
        # API 模式需要前台处理笔记内容的传入和关键词穿出
        input_notes_content = str(request.json['notes_content'])
        keywords = get_key_words(input_notes_content)
    return keywords

if __name__ == "__main__":
    APP.run('127.0.0.1', 5050)
