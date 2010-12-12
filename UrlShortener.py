'''
Created on Nov 21, 2010

@author: H.Haidoura
'''
import urllib
import simplejson

TINY_URL_API = "http://tinyurl.com/api-create.php";
GOOGL_URL_API = "http://goo.gl/api/url";
BITLY_URL_API = "http://api.bit.ly/v3/expand";


class UrlShortener(object):
    
    
    '''
    Shortens long url using thirdparty API e.g: goo.gl, tinyurl, bit.ly, ...
    '''
    def __init__( self , aName):
        '''
        Constructor
        '''
        self.name = aName
 
    def shorten(self, url):
        raise NotImplementedError
        

class TinyUrl(UrlShortener):

    def shorten(self , long_url):
        ret = None
        try:
            if (long_url != None):
                #apiurl = "http://tinyurl.com/api-create.php"
                url_data = urllib.urlencode({'url':long_url})
                urlObj = urllib.urlopen(TINY_URL_API, data=url_data)
                ret = urlObj.read().strip()
                
        except IOError:
            print "Failed to connect the tinylinks server", long_url
            ret = long_url
            
        return ret
    
    
class Googl(UrlShortener):
        
    def shorten(self , long_url):
        ret = None
        try:
            if (long_url != None):
                #apiurl = "http://goo.gl/api/shorten"
                params = urllib.urlencode({'security_token': None, 'url': long_url})  
                urlObj = urllib.urlopen( GOOGL_URL_API, params )  
                result = urlObj.read().strip()
                ret = simplejson.loads(result)['short_url']
                
                

        except IOError:
            print "Failed to connect the tinylinks server", long_url
            ret = long_url
            
        return ret
    
        
class Bitly(UrlShortener):
        
    def shorten(self):
        
        #username = BITLY_USERNAME
        #password = BITLY_PASSWORD
        #bitly_url = "http://api.bit.ly/v3/shorten?login={0}&apiKey={1}&longUrl={2}&format=txt"
        #req_url = urlencode(bitly_url.format(username, password, long_url)
        #short_url = urlopen(req_url).read()
        #return short_url
        return None
