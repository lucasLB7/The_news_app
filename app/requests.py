import urllib.request,json
from .models import Source,Article


# We get the API key

api_key = None
news_url = None
news_article = None

def configure_requests(app):
    global api_key , news_url, news_article
    api_key = app.config['NEWS_API_KEY']
    news_url = app.config['NEWS_SOURCES_URL']
    news_article = app.config['NEWS_ARTICLES_URL']

def get_sources(category):
    get_news_url = news_url.format(category,api_key)
    print(get_news_url)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
    if get_news_response['sources']:
        news_result_list = get_news_response['sources']
        news_results = process_sources(news_result_list)
    return news_results

def process_sources(news_result_list):
    source_results = []
    for source in news_result_list:
        id=source.get("id")
        name= source.get('name')
        description = source.get('description')
        url = source.get('url')
        if name:
            news_object = Source(id,name,description,url)
            source_results.append(news_object)
    return source_results



def get_articles(source_id):
        get_article_url = news_article.format(source_id,api_key)
        with urllib.request.urlopen(get_article_url) as url:
            get_news_data_art = url.read()
            get_news_response_art = json.loads(get_news_data_art)
            news_results_art = None

        if get_news_response_art['articles']:

            news_result_list_art = get_news_response_art['articles']
            news_results_art = process_articles(news_result_list_art)
        return news_results_art

def process_articles(news_result_list_art):
    article_results = []
    for article in news_result_list_art:

        author = article.get('author')
        title= article.get('title')
        description=article.get('description')
        url=article.get('url')
        url_image=article.get('urlToImage')

        if title:
            news_object = Article(author,title, description , url, url_image)

            article_results.append(news_object)
    return article_results
