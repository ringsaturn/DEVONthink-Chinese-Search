"""一个简单的获取关键词的本地 API 实现"""

# ringsaturn
# 2018-01-30 -> GET
# 2018-01-31 -> POST

from flask import Flask, request

from AnalyzeKeywords import get_keywords

APP = Flask(__name__)

@APP.route("/get_keywords", methods=['POST'])
def get_keywords_api():
    """the API"""
    # 判断是否调用后台模式
    if 'back_ground' in request.json:
        if bool(request.json['back_ground']):
            keywords = get_keywords(back_ground=True)
        else:
            input_notes_content = str(request.json['notes_content'])
            keywords = get_keywords(input_notes_content)
    else:
        # API 模式需要前台处理笔记内容的传入和关键词穿出
        input_notes_content = str(request.json['notes_content'])
        keywords = get_keywords(input_notes_content)
    return keywords

if __name__ == "__main__":
    APP.run('127.0.0.1', 5050)
