from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)

# 感情分析パイプラインの初期化
sentiment_pipeline = pipeline("sentiment-analysis")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    result = sentiment_pipeline(text)[0]
    return render_template('index.html', text=text, result=result)

if __name__ == '__main__':
    app.run(debug=True)

