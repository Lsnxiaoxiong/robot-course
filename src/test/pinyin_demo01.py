from pypinyin import pinyin, Style, lazy_pinyin


def quick_check(text, keyword):
    """最简单高效的方法（2-3字关键词）"""
    keyword_len = len(keyword)
    keyword_pinyin = ''.join(lazy_pinyin(keyword, style=Style.TONE3))

    for i in range(len(text) - keyword_len + 1):
        if ''.join(lazy_pinyin(text[i:i + keyword_len], style=Style.TONE3)) == keyword_pinyin:
            return True
    return False


# 使用
text = "这是反对上级指示或者对上级指示代工的最妙方法"
print(quick_check(text, "怠工"))  # True