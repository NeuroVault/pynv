import os

import betamax

from pyneurovault_upload import Client

ACCESS_TOKEN = os.environ.get('NEUROVAULT_ACCESS_TOKEN')


def test_my_collections():
    client = Client(access_token=ACCESS_TOKEN)

    recorder = betamax.Betamax(client.session)
    with recorder.use_cassette('my_collections'):
        result_dict = client.my_collections()

    assert result_dict['count'] == len(result_dict['results'])

    for collection in result_dict['results']:
        assert len(collection['name']) > 0
