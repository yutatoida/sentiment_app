from flask import Flask, render_template, request, jsonify
from transformers import pipeline
from analyzer import TextAnalyzer
from rewriter import TextRewriter

app = Flask(__name__)

# 感情分析パイプラインの初期化
classifier = pipeline('sentiment-analysis')

# テキスト解析クラスの初期化
text_analyzer = TextAnalyzer()

# テキスト書き換えクラスの初期化
text_rewriter = TextRewriter()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    response_message = ""
    text = ""
    analysis = None

    if request.method == 'POST':
        text = request.form['text']
        analysis_result = classifier(text)[0]
        label = analysis_result['label']
        score = analysis_result['score']

        # スコアに基づいたメッセージの生成
        if label == 'POSITIVE':
            response_message = "この文章はポジティブな感情を含んでいます。"
        elif label == 'NEGATIVE':
            response_message = "この文章はネガティブな感情を含んでいます。"
        else:
            response_message = "この文章は中立的な感情を持っています。"

        # テキスト解析を実行
        analysis = text_analyzer.analyze(text)

        # HTMLテンプレートに渡すデータを準備
        result = {
            'label': label,
            'score_text': "高い" if score > 0.5 else "低い"
        }

    return render_template('index.html', result=result, response_message=response_message, text=text, analysis=analysis)

@app.route('/rewrite', methods=['POST'])
def rewrite():
    data = request.get_json()
    text = data['text']
    analysis_result = classifier(text)[0]
    label = analysis_result['label']

    rewritten_text = text_rewriter.to_polite(text)

    if rewritten_text == text:
        rewritten_text = "書き換えなし"

    return jsonify({'rewritten_text': rewritten_text})

if __name__ == '__main__':
    app.run(debug=True)
