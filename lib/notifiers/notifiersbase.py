
class NotifiersBase(object):
    """
        The base notifier class that basically fetches data from a point and pushes
        to another point. The souce must  implement a "pull" method and destination
        must implement push method.
        
        Base classes are mainly responsible to process the data received from source
        and return a string data that can be directly fed to the destination. 
        By default a string representation of source data will be pushed to the destination.
    """

    datasource = None
    datadestination = None

    def run(self):
        if self.datasource is None or self.datadestination is None:
            raise Exception("Missing source or destination. Failed to Notify.")
        sourcedata = self.datasource.pull()
        feedingdata = self.processData(sourcedata)
        self.datadestination.push(feedingdata)
        
    def processData(self, data):
        return str(data)

