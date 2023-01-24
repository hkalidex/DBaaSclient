
import unittest
from mock import patch
# from mock import mock_open
from mock import call
from mock import Mock

from DBaaSclient import DBaaSclient
from DBaaSclient.dbaasclient import DBAAS_HOST

import sys
import logging
logger = logging.getLogger(__name__)

consoleHandler = logging.StreamHandler(sys.stdout)
logFormatter = logging.Formatter("%(asctime)s %(threadName)s %(name)s [%(funcName)s] %(levelname)s %(message)s")
consoleHandler.setFormatter(logFormatter)
rootLogger = logging.getLogger()
rootLogger.addHandler(consoleHandler)
rootLogger.setLevel(logging.DEBUG)


class TestDBaaSclient(unittest.TestCase):

    def setUp(self):

        pass

    def tearDown(self):

        pass

    @patch('DBaaSclient.dbaasclient.os.environ.get', return_value=None)
    @patch('DBaaSclient.dbaasclient.DBaaSclient')
    def test__get_DBaaSclient_Should_SetDefaultHostname_When_HostnameNotSpecifiedAndNotInEnvironment(self, dbaasclient_patch, *patches):
        DBaaSclient.get_DBaaSclient(api_key='--api_key--')
        self.assertTrue(call(DBAAS_HOST, api_key='--api_key--') in dbaasclient_patch.mock_calls)

    @patch('DBaaSclient.dbaasclient.os.environ.get', return_value='--api_key--')
    @patch('DBaaSclient.dbaasclient.DBaaSclient')
    def test__get_DBaaSclient_Should_GetApiKeyFromEnvironment_When_ApiKeyNotSpecified(self, dbaasclient_patch, *patches):
        DBaaSclient.get_DBaaSclient(hostname='hostname')
        self.assertTrue(call('hostname', api_key='--api_key--') in dbaasclient_patch.mock_calls)

    @patch('DBaaSclient.dbaasclient.os.environ.get', return_value=None)
    def test__get_DBaaSclient_Should_RaiseValueError_When_ApiKeyNotSpecifiedAndNotInEnvironment(self, *patches):
        with self.assertRaises(ValueError):
            DBaaSclient.get_DBaaSclient(hostname='hostname')

    def test__init_Should_RaiseValueError_When_ApiKeyNotSpecified(self, *patches):
        with self.assertRaises(ValueError):
            DBaaSclient('hostname')

    @patch('DBaaSclient.DBaaSclient.get')
    def test__get_iap_cost_Should_CallExpected_When_Called(self, get_patch, *patches):
        client = DBaaSclient('api-hostname', api_key='--api-key--')
        client.get_iap_cost()
        self.assertTrue(call('/v1/cost') in get_patch.mock_calls)

    @patch('DBaaSclient.DBaaSclient.get')
    def test__get_iap_cost_Should_ReturnExpected_When_Called(self, get_patch, *patches):
        client = DBaaSclient('api-hostname', api_key='--api-key--')
        result = client.get_iap_cost()
        self.assertEqual(result, get_patch.return_value)
