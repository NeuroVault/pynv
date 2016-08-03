import requests

from . import API_BASE_URL


class Client(object):

    def __init__(self,
                 access_token=None,
                 api_base_url=None):

        self.api_base_url = api_base_url or API_BASE_URL

        self.session = requests.Session()

        self.session.headers = (
            {'Authorization': 'Bearer %s' % access_token}
            if access_token else None
        )

    def my_collections(self):
        url = '%s%s' % (self.api_base_url, 'my_collections/')
        return self.session.get(url).json()
