from githublib.githubclient import GitHubClient

class PullerBase(object):
    _client = None
    
    def __init__(self):
        self._client = GitHubClient();
    
    def pull(self):
        return self._fetchTopRepositories()
        
class RepositoryPuller(PullerBase):

    _oldest_push_time = '2017-01-01'
    _num_repositories = 5
    
    def _fetchTopRepositories(self):
        params = {
            'page': 0,
            'per_page': self._num_repositories,
            'q': 'pushed:>' + self._oldest_push_time,
            'sort': 'updated',
            'order': 'desc'
        }
        repo_feed = self._client.search_repositories(params)
        return repo_feed['items']
        