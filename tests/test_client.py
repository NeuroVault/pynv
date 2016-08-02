from pyneurovault_upload import Client


def test_client():
    upload = Client()
    assert upload.post
