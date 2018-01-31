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
    input_notes_content = str(request.json['notes_content'])
    key_words = get_key_words(input_notes_content)
    return key_words

if __name__ == "__main__":
    APP.run('127.0.0.1', 5050)
