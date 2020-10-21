from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_articles, get_sources, topheadlines
from ..models import NewsSources
                 
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
    #business = get_article('top-headlines')
    #health = get_article('sources')
    #entertainment = get_article('top-headlines')
    top = topheadlines()
    return render_template('index.html', general =general_news, business =business_news,technology = technology_news, health = health_news,entertainment = entertainment_news,sports = sports_news,top = top)

    # return render_template('index.html', title = title,general=general,health=health)
    
@main.route('/sources/<id>')
def articles(id):
    '''
    View articles page function
    '''
    articles = get_articles(id)
    title = f'News Updates || {id}'
    return render_template('articles.html',articles = articles, title= title)