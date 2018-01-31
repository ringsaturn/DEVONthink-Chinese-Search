"""通过 API 获取关键词"""

# ringsaturn
# 2018-01-30 -> GET
# 2018-01-31 -> POST

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
