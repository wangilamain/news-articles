from flask import render_template
from . import main
from ..requests import get_article, get_sources,topheadlines
​
# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    general_news = get_sources('general')
    business_news = get_sources('business')
    technology_news = get_sources('technology')
    health_news = get_sources('health')
    entertainment_news = get_sources('entertainment')
    sports_news = get_sources('sports')
    top = topheadlines()
    #business = get_article('top-headlines')
    #health = get_article('sources')
    #entertainment = get_article('top-headlines')
    title = 'Home- News Updates'
    return render_template('index.html', general =general_news, business =business_news,technology = technology_news, health = health_news,entertainment = entertainment_news,sports = sports_news, top = top)

    # return render_template('index.html', title = title,general=general,health=health)
    
​
@main.route('/sources')
@main.route('/sources/<id>')
def news(id=None):
    '''
    view news articles page that is detailed
    '''
    general_news = get_sources('general')
    business_news = get_sources('business')
    technology_news = get_sources('technology')
    health_news = get_sources('health')
    entertainment_news = get_sources('entertainment')
    sports_news = get_sources('sports')
    article = get_articles(id)
    if article:
        for i in article:
            name = i.name
    else:
         name = ""
        
    return render_template('article.html',general =general_news, business =business_news,technology = technology_news, health = health_news,entertainment = entertainment_news,sports = sports_news,article = article,name = name)