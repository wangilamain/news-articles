import unittest
from app.models import Top

class ArticleTest(unittest.TestCase):

    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('ABC News','Donald Trump','Arrogance','lorem ipsum','www.wdhd.com','www.whjd.com','2020-08-10')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article,Top))