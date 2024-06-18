# 感情分析Webアプリケーション

このアプリケーションは、Hugging Face transformersライブラリの事前訓練済みモデルを使用して、ユーザーが入力したテキストの感情分析を行うシンプルなWebアプリケーションです。Flaskという軽量のWSGI Webアプリケーションフレームワークを使用して構築されています。

## 特徴

- ユーザーフレンドリーなWebインターフェースを提供。
- 入力されたテキストに対して感情分析を実行。
- 感情ラベルと信頼スコアを表示。

## 必要要件

- Python 3.x
- Flask
- transformers
- torch

## インストール

### ステップ 1: リポジトリをクローン

```bash
git clone https://github.com/your-username/sentiment_app.git
cd sentiment_app
