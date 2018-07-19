from nltk.parse.corenlp import CoreNLPParser
from mafan import simplify
from nltk.tree import Tree

# 句法分析
try:
    句法分析器 = CoreNLPParser()
except Warning as 錯誤:
    print('Warning=', 錯誤)

分析結果指標 = 句法分析器.parse(simplify("我 喜歡 豬").split())
該句結果字串 = next(分析結果指標)

# 印字串
# (ROOT (IP (NP (PN 我)) (VP (VV 喜欢) (NP (NN 猪)))))
print('該句結果字串=', 該句結果字串)

# 照字串印樹仔圖
# ROOT        
#      |           
#      IP         
#   ___|____       
#  |        VP    
#  |    ____|___   
#  NP  |        NP
#  |   |        |  
#  PN  VV       NN
#  |   |        |  
#  我   喜欢       猪 
該句結果字串.pretty_print()

