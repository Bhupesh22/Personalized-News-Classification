# Flask News Article Ranker

This Flask web application scrapes news articles from Google News and ranks them based on user preferences using multiple pre-trained transformer models.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This application allows users to input their preferences and have news articles ranked according to those preferences using two different NLP models: BART and DistilBERT. The application scrapes news articles from Google News RSS feed and leverages the power of pre-trained transformer models for zero-shot classification.

## Features
- Scrapes the latest news articles from Google News.
- Supports ranking articles using user-defined preferences.
- Utilizes two different pre-trained transformer models:
  - BART (facebook/bart-large-mnli)
  - DistilBERT (cross-encoder/nli-distilroberta-base)
- Displays ranked articles on a simple web interface.

## Installation
Follow these steps to set up and run the application locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/flask-news-ranker.git
   cd flask-news-ranker

2. ** Set up a virtual environment (optional but recommended): **

    ```bash
    Copy code
    python3 -m venv venv
    source venv/bin/activate
    Install the required dependencies:

    bash
    Copy code
    pip install -r requirements.txt
    Run the application:

    bash
    Copy code
    python app.py
    Access the application: Open your web browser and go to http://127.0.0.1:5000.


## Usage
Home Page:
Enter your preferences in the text box separated by commas (e.g., "technology, politics, sports").
Click "Submit" to rank the news articles based on your preferences.
Results:
The page will display the articles ranked by two different models: BART and DistilBERT.
Each model's results will be shown separately, allowing you to compare how each model ranks the articles.
How It Works
Scraping News Articles:

The application scrapes the latest news articles from Google News using the RSS feed.
BeautifulSoup is used to parse the XML content and extract the titles, links, and descriptions of the articles.
Ranking Articles:

The articles are ranked based on user preferences using two different transformer models:
BART: A model by Facebook AI that excels in zero-shot classification tasks.
DistilBERT: A smaller, faster version of BERT fine-tuned for zero-shot classification.

Each model scores the articles based on how well they match the user's preferences, and the articles are then ranked accordingly.
Displaying Results:

The ranked articles are displayed on the web page under the corresponding model's section.
This allows users to see how different models prioritize content based on their input.

Dependencies
Flask: A lightweight WSGI web application framework.
Requests: A simple HTTP library for Python.
BeautifulSoup: A library for parsing HTML and XML documents.
Transformers: Hugging Face's library for state-of-the-art NLP models.

The specific versions of these dependencies can be found in the requirements.txt file.

### Explanation of the Code

1. **Flask Setup:**
   - The `Flask` app is initialized and configured to serve a simple web application.

2. **Model Initialization:**
   - Two pre-trained models are loaded using Hugging Face's `transformers` library. These models will be used for zero-shot classification of news articles.

3. **Fetching News Articles:**
   - The `fetch_news` function scrapes the latest articles from Google News using the RSS feed. It extracts the title, link, and description of each article.

4. **Ranking Articles:**
   - The `rank_articles` function takes the scraped articles and ranks them based on user-defined preferences using the two models.
   - Each model scores how well the article titles match the user's preferences and sorts the articles accordingly.

5. **Web Interface:**
   - The `index` route handles GET and POST requests. It fetches the news articles, ranks them if preferences are provided, and renders the `index.html` template with the ranked articles.

6. **Running the Application:**
   - The app is run in debug mode locally, which is useful for development purposes.