from nltk.parse.corenlp import CoreNLPParser
from mafan import simplify

# 句法分析
try:
    句法分析器 = CoreNLPParser()
except Warning as 錯誤:
    print('Warning=', 錯誤)

# 印字串
結果 = 句法分析器.parse(simplify("我 喜歡 豬").split())
next(結果).pretty_print()
# 印圖表
# next(
#     句法分析器.parse("猴子 喜欢 吃 香蕉 。".split())
# ).pretty_print()
