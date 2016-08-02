from pyneurovault_upload import Upload


def test_client():
    upload = Upload()
    assert upload.post
