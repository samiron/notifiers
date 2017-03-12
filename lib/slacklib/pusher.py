from .slackclient import SlackClient
from urlparse import urlparse
import json

class SlackWebHook():
    
    _slack_client = None
    _hook_link = None
    _hostname = None
    _path = None
    
    def __init__(self, hook_link):
        self._hook_link = hook_link
        link_obj = urlparse(self._hook_link)
        self._hostname = link_obj.netloc
        self._path = link_obj.path
        
        self._slack_client = SlackClient(self._hostname)

    def push(self, message):
        content = {
            'text': message,
            "icon_emoji": ":snowman:"
        }
        message = json.dumps(content)
        self._slack_client.POST(self._path, message)
        
