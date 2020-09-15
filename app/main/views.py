from flask import render_template
from . import main
from ..requests import get_article, get_sources
​
# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    general = get_article('top-headlines')
    #business = get_article('top-headlines')
    #health = get_article('sources')
    #entertainment = get_article('top-headlines')
    title = 'Home- News Updates'
    return render_template('index.html', title = title,general=general)
    # return render_template('index.html', title = title,general=general,health=health)
    
​
@main.route('/sources')
@main.route('/sources/<id>')
def news(id=None):
    '''
    view news articles page that is detailed
    '''
    title = 'Sources'
    sources = get_sources('sources')
    news_from_source = get_article('top-headlines')
    if id:
        return render_template('sources.html', title=title,news=news_from_source,id=id )
    else:
        return render_template('sources.html', title=title,sources_list = sources)
