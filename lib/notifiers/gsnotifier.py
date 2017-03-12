from .notifiersbase import NotifiersBase
from githublib import puller
from slacklib import pusher


class GSNotifier(NotifiersBase):
    """
        A notifier class that pulls data from GitHub and pushes data to slack 
        using channel web hook.
    """
    
    def __init__(self, slack_hook):
        super(GSNotifier, self).__init__()
        self.datasource = puller.RepositoryPuller()
        self.datadestination = pusher.SlackWebHook(slack_hook)

    def processData(self, githubrepos):
        names = []
        for repo in githubrepos:
            names.append(repo['full_name'])
        return '\n'.join(names)
        