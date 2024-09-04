from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

app = Flask(__name__)

# Initialize multiple pre-trained transformer models
models = {
    'BART': pipeline('zero-shot-classification', model='facebook/bart-large-mnli'),
    'DistilBERT': pipeline('zero-shot-classification', model='cross-encoder/nli-distilroberta-base')
}

# Function to scrape news articles from Google News
def fetch_news():
    url = 'https://news.google.com/rss'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    articles = []
    for item in soup.find_all('item'):
        articles.append({
            'title': item.title.text,
            'link': item.link.text,
            'description': item.description.text
        })
    return articles

# Function to rank articles based on user preferences using multiple models
def rank_articles(articles, user_preferences):
    results = {}
    
    for model_name, classifier in models.items():
        ranked_articles = []
        for article in articles:
            result = classifier(article['title'], user_preferences)
            score = max(result['scores'])
            ranked_articles.append((score, article))
        
        ranked_articles.sort(reverse=True, key=lambda x: x[0])
        results[model_name] = [article for score, article in ranked_articles]

    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    user_preferences = []
    if request.method == 'POST':
        user_preferences = request.form['preferences'].split(',')
    
    articles = fetch_news()
    ranked_articles_by_model = {}
    
    if user_preferences:
        ranked_articles_by_model = rank_articles(articles, user_preferences)
    
    return render_template('index.html', ranked_articles_by_model=ranked_articles_by_model)

if __name__ == '__main__':
    app.run(debug=True)