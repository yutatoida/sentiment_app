import spacy

class TextAnalyzer:
    def __init__(self):
        # 日本語モデルを読み込みます
        self.nlp = spacy.load('ja_core_news_sm')

    def analyze(self, text):
        doc = self.nlp(text)
        analysis_result = {
            'subjects': [],
            'verbs': [],
            'adverbs': [],
            'adjectives': [],
            'auxiliary_verbs': [],
            'others': []
        }

        for token in doc:
            if token.pos_ == 'NOUN':  # 名詞は主語として分類
                analysis_result['subjects'].append(token.text)
            elif token.pos_ == 'VERB':  # 動詞は動詞として分類
                analysis_result['verbs'].append(token.text)
            elif token.pos_ == 'ADV':  # 副詞
                analysis_result['adverbs'].append(token.text)
            elif token.pos_ == 'ADJ':  # 形容詞
                analysis_result['adjectives'].append(token.text)
            elif token.pos_ == 'AUX':  # 助動詞
                analysis_result['auxiliary_verbs'].append(token.text)
            else:  # それ以外のもの
                analysis_result['others'].append(token.text)

        return analysis_result
