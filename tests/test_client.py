import os

import betamax

from pyneurovault_upload import Client

ACCESS_TOKEN = os.environ.get('NEUROVAULT_ACCESS_TOKEN')


def test_my_collections():
    client = Client(access_token=ACCESS_TOKEN)

    recorder = betamax.Betamax(client.session)
    with recorder.use_cassette('my_collections'):
        collection_list = client.my_collections()

    assert collection_list == []

