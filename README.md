# Stanford_Hua5gi2_NLP
Stanford的華語NLP服務，斷詞華語句->華語句法樹

## 執行

```
docker build -t flask_server -f ServerDockerfile .
```

開啟Stanford華語句法分析器

```
docker run -ti --rm --name stanford a8568730/stanford_hua5gi2_nlp
```

開啟本專案服務

```
docker run -ti --rm --name flask_server -p 5000:5000 --link stanford flask_server
```

