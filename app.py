from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)

# 感情分析パイプラインの初期化
sentiment_pipeline = pipeline("sentiment-analysis")

# ラベルを日本語にマッピングする辞書
label_mapping = {
    'LABEL_0': 'ネガティブ',
    'LABEL_1': 'ポジティブ',
    'POSITIVE': 'ポジティブ',
    'NEGATIVE': 'ネガティブ'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    result = sentiment_pipeline(text)[0]
    result['label'] = label_mapping.get(result['label'], '未知のラベル')
    return render_template('index.html', text=text, result=result)

if __name__ == '__main__':
    app.run(debug=True)
