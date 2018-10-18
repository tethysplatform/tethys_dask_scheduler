from distributed.diagnostics.plugin import SchedulerPlugin
from tornado.httpclient import AsyncHTTPClient


class TethysSchedulerPlugin(SchedulerPlugin):

    def __init__(self, endpoint='http://localhost:8000', scheduler=None):
        """
        Constructor.
        """
        self.endpoint = endpoint
        self.scheduler = scheduler

    def transition(self, key, start, finish, *args, **kwargs):
        """
        Hook that is called each time a task changes status. Push status of jobs Tethys is tracking to Tethys.
        """

        # Construct URL
        # get the client from scheduler
        tracked_key = self.scheduler.get_metadata(keys=[key], default=False)

        if tracked_key:
            combined_status = '{}-{}'.format(start, finish)
            url = self.endpoint + '/update-dask-job-status/' + key + '/?status=' + combined_status

            http_client = AsyncHTTPClient()

            # Prevent deadlock
            if start != 'released':
                http_client.fetch(url, method='GET')
