def test_create_collection_for_anonymous_user():
    pass


def test_create_collection_with_missing_fields():
    pass


def test_create_collection():
    pass


def test_read_collection():
    pass


def test_update_collection_for_anonymous_user():
    pass


def test_update_collection():
    pass


def test_delete_collection_for_anonymous_user():
    pass


def test_delete_collection():
    pass


def test_my_collections(client, recorder):
    with recorder.use_cassette('my_collections'):
        result_dict = client.my_collections()

    assert result_dict['count'] == len(result_dict['results'])

    for collection in result_dict['results']:
        assert len(collection['name']) > 0


def test_my_collections_for_anonymous_user():
    pass
