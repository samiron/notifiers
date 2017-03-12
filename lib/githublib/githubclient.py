from urlparse import urlparse
import urllib
import traceback
import httplib
import json

class GitHubClient(object):
    
    DEFAULT_HEADERS = {'User-Agent': 'github-data-puller'}
    
    def __init__(self):
        self.conn = httplib.HTTPSConnection("api.github.com")
        
    def _parse_json(self, data):
        return json.loads(data)

    def search_repositories(self, params):
        path = '/search/repositories'
        query_s = urllib.urlencode(params)
        link = "%s?%s" % (path, query_s)
        try:
            self.conn.request("GET", link, None, {'User-Agent': 'github-data-puller'})
            response = self.conn.getresponse()
            return self._parse_json(response.read())
        except Exception as err:
            traceback.print_exc()
        
        
        

        