#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# 置換用の辞書
replace_dict = {
    '@token1': 'replacement1',
    '@token2': 'replacement2',
    '@token3': 'replacement3',
    # 追加のトークンと置換文字列をここに追加
}

# テスト用の文字列
text = """
This is a sample text with @token1, some @token2 and also @token3.
We need to replace these tokens correctly.
"""

# トークンを置換する関数
def replace_tokens(text, replace_dict):
    # 置換関数
    def replace(match):
        token = match.group(0)
        return replace_dict.get(token, token)  # 辞書にないトークンはそのままにする

    # トークンを検出する正規表現パターン
    pattern = re.compile(r'(@\w+)(?=[,.\s\n])')

    # 置換処理
    return pattern.sub(replace, text)

# 置換実行
new_text = replace_tokens(text, replace_dict)

print(text)
print(new_text)

