from flask import Flask, render_template, url_for, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import nltk
from collections import Counter
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/nlp', methods=["POST"])
def nlp():
    if request.method == 'POST':
        result = []
        text = request.form['text']
        funct_type = request.form['functiontype']

        def count(text):
            from collections import Counter
            Counter = Counter(text.split())
            most_occur = Counter.most_common(10)
            results = 'The 10 most comment words is %s' % most_occur
            return results

        def sent(text):
            analyzer = SentimentIntensityAnalyzer()
            results = analyzer.polarity_scores(text)
            return 'The Sentiment result is %s' % results

        def tokeniz(text):
            results = nltk.word_tokenize(text)
            return 'The tokenized result is %s' % results

        def freq(text):
            tokens = nltk.word_tokenize(text)
            fdist = tokens_freq = Counter(tokens)
            return 'The frequency of the text is %s' % fdist

        def remove(text):
            word_tokens = nltk.word_tokenize(text)
            stopword = stopwords.words('english')
            removing_stopwords = [word for word in word_tokens if word not in stopword]
            return 'The result of removing stopwords is %s' % removing_stopwords

        def lower_case(text):
            word = text.lower()
            return 'The result of lowering case is %s' % word
        
        def pos_tagging(text):
            words = nltk.word_tokenize(text)
            tagged = nltk.pos_tag(words)
            return 'The result of using pos tagging is %s' & tagged
        
        def remove_pun(text):
            from nltk.tokenize import RegexpTokenizer
            tokenizer = RegexpTokenizer(r'\w+')
            sve = tokenizer.tokenize(text)
            return 'The result of removing punctuation is %s' % sve





        if funct_type == 'count':
            result = count(text)
        elif funct_type == 'sent':
            result = sent(text)
        elif funct_type == 'tokenize':
            result = tokeniz(text)
        elif funct_type == 'freq':
            result = freq(text)
        elif funct_type == 'remove':
            result = remove(text)
        elif funct_type == 'lower_case':
            result = lower_case(text)
        elif funct_type == 'pos_tagging':
            result = pos_tagging(text)
        elif funct_type == 'remove_pun':
            result = remove_pun(text)
        elif funct_type == 'all':
            result1 = count(text)
            result2 = sent(text)
            result3 = tokeniz(text)
            result4 = freq(text)
            result5 = remove(text)
            result6 = lower_case(text)
            result7 = pos_tagging(text)
            result8 = remove_pun(text)
            result = [result1, result2, result3, result4, result5, result6,result7, result8]

        return render_template("index.html", result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)
