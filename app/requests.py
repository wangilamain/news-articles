import urllib.request,json
from .models import NewsArticles, NewsSources

api_key = None
base_url = None


def configure(app):
    global api_key, base_url
    base_url = app.config['BASE_URL']
    api_key = app.config['NEWS_API_KEY']


def get_article(endpoint, filter):
    '''
    '''
    get_article_url = base_url.format(endpoint, api_key, filter)

    with urllib.request.urlopen(get_article_url) as url:
        response = json.loads(url.read())
        results = None

        if response:
            articles_lists = response['articles']
            results = process_articles(articles_lists)
    return results


def process_articles(articles_lists):
    processed_articles = []
    for article in articles_lists:
        source = article.get('source')
        title = article.get('title')
        author = article.get('author')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')

        if content and urlToImage:
            article_object = NewsArticles(
                source, author, title, description, url, urlToImage, publishedAt, content)
            processed_articles.append(article_object)
    return processed_articles


def get_sources(endpoint):
    get_sources_url = base_url.format(endpoint,api_key,'')

    with urllib.request.urlopen(get_sources_url) as url:
        response = json.loads(url.read())
        results = None

        if response:
            sources_lists = response['sources']
            results = process_sources(sources_lists)
    return results        

def process_sources(sources_lists):
    processed_sources = []

    for source in sources_lists:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        language = source.get('language')
        country = source.get('country')

        sources_object = NewsSources(id,name,description,url,category,language,country)
        processed_sources.append(sources_object)
    return processed_sources