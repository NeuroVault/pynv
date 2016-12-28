import os

import pytest
import betamax
from betamax_serializers import pretty_json

from pynv import Client

ACCESS_TOKEN = os.environ.get('NEUROVAULT_ACCESS_TOKEN', '** secret token **')

betamax.Betamax.register_serializer(pretty_json.PrettyJSONSerializer)

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = 'tests/cassettes'
    config.default_cassette_options['serialize_with'] = 'prettyjson'
    config.define_cassette_placeholder('<ACCESS_TOKEN>', ACCESS_TOKEN)


@pytest.fixture(scope='function')
def anonymous_client():
    return Client()


@pytest.fixture(scope='function')
def client():
    return Client(access_token=ACCESS_TOKEN)


@pytest.fixture(scope='function')
def recorder(client):
    return betamax.Betamax(client.session)
