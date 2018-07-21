from flask import Flask
import json
from Stanford華語句法分析器.句法分析器 import 提華語句法樹

app = Flask(__name__)

@app.route('/<bunji>')
def 服務(bunji):
    樹 = 提華語句法樹(bunji)
    print('樹=', str(樹))
    return json.dumps(str(樹), ensure_ascii=False)

if __name__ == "__main__":
    app.run(host='0.0.0.0')