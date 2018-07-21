# Stanford_Hua5gi2_NLP
Stanford的華語NLP服務，斷詞華語句->華語句法樹

## 執行
```
docker run -ti --rm -p 5000:5000 stanford_hua5gi2_server
```

再開啟Stanford華語句法分析器
```
docker run -ti --rm -p 9000:9000 a8568730/stanford_hua5gi2_nlp
```
