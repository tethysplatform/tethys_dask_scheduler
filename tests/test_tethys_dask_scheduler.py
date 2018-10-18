"""
********************************************************************************
* Name: test_dask_scheduler
* Author: nswain, tran, teva
* Created On: October 15, 2018
* Copyright: (c) Aquaveo 2018
********************************************************************************
"""
import unittest
import mock
from tethys_dask_scheduler.tethys_scheduler_plugin import TethysSchedulerPlugin


class SchedulerPluginTest(unittest.TestCase):
    def set_up(self):
        pass

    def tear_down(self):
        pass

    def test_init(self):

        tds_plugin = TethysSchedulerPlugin(endpoint='http://localhost:8080')

        # Check result
        self.assertEqual('http://localhost:8080', tds_plugin.endpoint)

    @mock.patch('tornado.util.Configurable')
    @mock.patch('tornado.httpclient.AsyncHTTPClient')
    def test_transition(self, mock_http_client, _):
        # TODO: Need to check with Nathan
        pass
        # mock_scheduler = mock.MagicMock()
        # tds_plugin = TethysSchedulerPlugin(endpoint='http://localhost:8080', scheduler=mock_scheduler)
        # mock_scheduler.get_metadata.return_value = True
        # mock_http_client.return_value = mock.MagicMock()
        #
        #
        # # Call the method
        # tds_plugin.transition(key='sum-4a062-d246-11e8-9aec-e33e562837e2', start='start', finish='complete')
        #
        # call_args = mock_http_client.call_args_list
        #
        # self.assertIs('', call_args)
