import requests

from . import API_BASE_URL

from .exceptions import APIError, AuthenticationError, ValidationError


class Client(object):

    def __init__(self,
                 access_token=None,
                 api_base_url=None):

        self.api_base_url = api_base_url or API_BASE_URL

        self.session = requests.Session()

        if access_token:
            self.session.headers.update(
                {'Authorization': 'Bearer %s' % access_token}
            )

    def request(
            self,
            method,
            endpoint,
            data=None,
            json=None,
            files=None,
            suffix='/'):
        url = '%s%s%s' % (self.api_base_url, endpoint, suffix)

        response = getattr(self.session, method)(
            url, json=json, data=data, files=files
        )

        if response.ok:
            return response
        elif response.status_code == 400:
            raise ValidationError(response)
        elif response.status_code == 401:
            raise AuthenticationError(response)
        else:
            raise APIError(response)

    def create_collection(self, name, **data):
        data['name'] = name

        return self.request('post', 'collections', json=data).json()

    def get_collection(self, collection_id):
        raise NotImplementedError()

    def update_collection(self, collection_id, **data):
        raise NotImplementedError()

    def delete_collection(self, collection_id):
        return self.request('delete', 'collections/%s' % collection_id)

    def my_collections(self):
        return self.request('get', 'my_collections').json()

    def add_image(self, collection_id, file_object_or_string, **data):
        files = {'file': open(file_object_or_string, 'rb')}

        return self.request(
            'post',
            'collections/%s/images' % collection_id,
            data=data,
            files=files
        ).json()
