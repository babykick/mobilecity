#coding=utf-8
import requests

class DoubanAPI(object):
    """
      图书 http://developers.douban.com/wiki/?title=book_v2
      电影 http://developers.douban.com/wiki/?title=movie_v2
      音乐 http://developers.douban.com/wiki/?title=music_v2
    """
    BOOK_SEARCH = 'https://api.douban.com/v2/book/search'
    MOVIE_SEARCH = ''
    MUSIC_SEARCH = ''
    
    def querybook(self, **kargs):
        r = requests.get(self.BOOK_SEARCH, params=kargs)
        if r.status_code == 200:
            return r.content
    
    def queryMovie(self, **kargs):
        pass
    
    def queryMusic(self, **kargs):
        pass
    
    
    
if __name__ == '__main__':
    dban = DoubanAPI()
    data = dban.querybook(q='乌合之众')
    print data