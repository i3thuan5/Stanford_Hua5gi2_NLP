from nltk.parse.corenlp import CoreNLPParser


# 句法分析
try:
    句法分析器 = CoreNLPParser()
except Warning as 錯誤:
    print('Warning=', 錯誤)

# 印字串
#結果 = list(句法分析器.parse("我 喜欢 豬".split()))
#print('結果=', 結果)

# 印圖表
next(next(
    句法分析器.parse("猴子 喜欢 吃 香蕉 。".split())
)).pretty_print()
