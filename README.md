[![build status](https://api.travis-ci.org/neurolearn/pyneurovault_upload.svg?branch=master)](https://travis-ci.org/neurolearn/pyneurovault_upload)
[![Coverage Status](https://coveralls.io/repos/github/neurolearn/pyneurovault_upload/badge.svg?branch=master)](https://coveralls.io/github/neurolearn/pyneurovault_upload?branch=master)

# pyneurovault_upload
Python library for interfacing with http://neurovault.org upload API


## Installation

```
git clone https://github.com/neurolearn/pyneurovault_upload.git
cd pyneurovault_upload
python setup.py install
```

## Example Usage

### Initialize a Client instance

First, we need to create an instance of the Client class. This requires adding your NeuroVault personal access token which can be found under [“Personal Access tokens”](http://neurovault.org/accounts/tokens/) tab in the Account Settings.

```python
from pyneurovault_upload.api import Client

api = Client(access_token='your_neurovault_personal_access_token')
```

### Create a Collection

To create a new collection in NeuroVault you need to pass a dictionary of all of the metadata you would like to specify in the collection. At a minimum you must specify a collection name.

```python
collection = api.create_collection('a name of a new collection')
```

### Add an image to a collection

Once a collection is created you can add images to it using the `add_image()` method. You need to pass a string indicating the path to the file you would like to upload. You also need to pass a few mandatory parameters, which include the image name, the image modality, and the map type.

```python
image_file_path = 'path/to/image/file.nii.gz'

image = api.add_image(
    collection['id'],
    image_file_path,
    name='Parcellation_k25',
    modality='Other',
    map_type='Pa'
)
```

You can also annotate an image with custom metadata:

```python
image = api.add_image(
    collection['id'],
    image_file_path,
    name='Parcellation_k25',
    modality='Other',
    map_type='Pa',
    custom_metadata_field=42
)
```

### Update an image

```python
api.update_image(
    image['id'], 
    map_type='T',
    custom_metadata_field=42
)
```

### Delete an image

```python
api.delete_image(image['id'])
```

### Delete a collection

To delete a collection you can simply run the `delete_collection()` method. You can delete any collection that you own.  Be careful with this as you will be unable to recover any collections that you delete!

```python
api.delete_collection(collection.id)
```
