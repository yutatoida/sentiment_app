class TextRewriter:
    def __init__(self):
        # 簡単な変換ルールの辞書
        self.polite_dict = {
            "です": "でございます",
            "ます": "ます",
            "する": "いたします",
            "ありがとう": "ありがとうございます",
            "こんにちは": "こんにちは",
            "こんばんは": "こんばんは",
            "おはよう": "おはようございます",
            "すみません": "申し訳ございません",
            "わかりました": "承知いたしました",
            "ない": "ございません"
        }

    def to_polite(self, text):
        for casual, polite in self.polite_dict.items():
            text = text.replace(casual, polite)
        return text
