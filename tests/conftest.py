import os

import betamax
from betamax_serializers import pretty_json

access_token = os.environ.get('NEUROVAULT_ACCESS_TOKEN')

betamax.Betamax.register_serializer(pretty_json.PrettyJSONSerializer)

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = 'tests/integration/cassettes'
    config.default_cassette_options['serialize_with'] = 'prettyjson'
    config.define_cassette_placeholder('<ACCESS_TOKEN>', access_token)
