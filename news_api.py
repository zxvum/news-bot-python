from newsapi import NewsApiClient

import config

newsapi = NewsApiClient(api_key=config.NEWS_API_KEY)


def get_article(query):
    all_articles = newsapi.get_everything(q=query, language='ru', sort_by='relevancy')
    article = all_articles['articles'][0]
    return article

