import pytest

from pynv.exceptions import (
    APIError, AuthenticationError, ValidationError
)


def test_create_collection_for_anonymous_user(anonymous_client, recorder):
    with pytest.raises(APIError) as excinfo:
        anonymous_client.create_collection('Anonymous2020')

    assert excinfo.value.errors == {
        'detail': 'Authentication credentials were not provided.'
    }


def test_create_collection_with_missing_fields(client, recorder):
    with pytest.raises(TypeError):
        client.create_collection()


def test_create_collection_with_blank_name(client, recorder):
    with recorder.use_cassette('create_collection_with_blank_name'):
        with pytest.raises(ValidationError) as excinfo:
            client.create_collection('')

    assert excinfo.value.errors == {'name': ['This field may not be blank.']}


def test_create_collection(client, recorder):
    with recorder.use_cassette('create_collection'):
        collection = client.create_collection('NV Test Collection2020')

    subset_dict = {
        'name': 'NV Test Collection2020'
    }

    assert subset_dict.items() <= collection.items()


def test_read_collection(client, recorder):
    with recorder.use_cassette('read_collection'):
        collection = client.get_collection(8477)

    subset_dict = {
        'name': 'First test collection'
    }

    assert subset_dict.items() <= collection.items()


def test_update_collection_for_anonymous_user(anonymous_client):
    with pytest.raises(AuthenticationError):
        anonymous_client.update_collection(8477, name='New Name')


def test_update_collection(client, recorder):
    with recorder.use_cassette('update_collection'):
        collection = client.update_collection(8477, name='New Name 2020')

    assert collection['name'] == 'New Name 2020'


def test_my_collections(client, recorder):
    with recorder.use_cassette('my_collections'):
        result_dict = client.my_collections()

    assert result_dict['count'] == len(result_dict['results'])

    for collection in result_dict['results']:
        assert len(collection['name']) > 0


def test_my_collections_for_anonymous_user(anonymous_client):
    with pytest.raises(AuthenticationError):
        anonymous_client.my_collections()
