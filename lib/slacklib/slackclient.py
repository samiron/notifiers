import httplib

class SlackClient(object):
    
    conn = None 
    
    def __init__(self, host=None):
        if host is not None:
            self.conn = httplib.HTTPSConnection(host)
            
            
    def POST(self, path, body):
        self.conn.request('POST', path, body)
        response = self.conn.getresponse()
        return response
        
        
        
