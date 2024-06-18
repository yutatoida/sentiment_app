from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)

# 感情分析パイプラインの初期化
sentiment_pipeline = pipeline("sentiment-analysis")

# ラベルを日本語にマッピングする辞書
label_mapping = {
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

    # 感情に基づいたメッセージを生成
    if result['label'] == 'ポジティブ':
        response_message = "この文章はポジティブな感情を含んでいます。"
    elif result['label'] == 'ネガティブ':
        response_message = "この文章はネガティブな感情を含んでいます。"
    else:
        response_message = "この文章は中立的な感情を持っています。"

    return render_template('index.html', text=text, result=result, response_message=response_message)

if __name__ == '__main__':
    app.run(debug=True)
