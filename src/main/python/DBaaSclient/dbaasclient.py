import os
from RESTclient import RESTclient

import logging
logger = logging.getLogger(__name__)

logging.getLogger('urllib3.connectionpool').setLevel(logging.CRITICAL)

DBAAS_HOST = 'dbaas-cost.cloud.intel.com'


class DBaaSclient(RESTclient):

    def __init__(self, hostname, **kwargs):
        """ class constructor

            Args:
                kwargs (dict): arbritrary number of key word arguments

            Returns:
                DBaaSclient: instance of DBaaSclient
        """
        logger.debug('executing DBaaSclient constructor')

        if 'api_key' not in kwargs:
            raise ValueError('an api_key must be provided to DBaaSclient')

        super(DBaaSclient, self).__init__(hostname, **kwargs)

    def get_iap_cost(self):
        """ return iap cost data

            Args:

            Returns:
                dict: iap cost information
        """
        logger.debug('getting iap cost data')
        return self.get('/v1/cost')

    @classmethod
    def get_DBaaSclient(cls, hostname=None, api_key=None):
        """ return instance of DBaaSclient

            Args:
                hostname (str): the host and endpoint for the DBaaS REST API
                api_key (str): the DBaaS REST API key

            Returns:
                DBaaSclient: instance of DBaaSclient
        """
        if not hostname:
            hostname = os.environ.get('DBAAS_H')
            if not hostname:
                hostname = DBAAS_HOST

        if not api_key:
            api_key = os.environ.get('DBAAS_K')
            if not api_key:
                raise ValueError('api_key must be specified or set as DBAAS_K environment variable')

        return DBaaSclient(hostname, api_key=api_key)
