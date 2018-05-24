from flask import render_template
from . import main
from ..requests import get_sources,get_articles



# Views

@main.route('/articles/<article_id>')
def articles(article_id):

    articles = get_articles(article_id)
    title = article_id.replace("-"," ")

    return render_template('articles.html',articles=articles,title=title)




@main.route('/')
def index():
    categories=["business" ,"entertainment", "general" ,"health", "science", "sports", "technology"]
    news=[get_sources(i) for i in categories]
    categories_items=dict(zip(categories,news))
    print(news)
    # title = 'WORLD OVERVIEW - Spy-Witness news'
    #
    return render_template('index.html',business=categories_items['business'], entertainment=categories_items['entertainment'], general=categories_items['general'], health=categories_items['health'], science=categories_items['science'], sports=categories_items['sports'], technology=categories_items['technology'])
