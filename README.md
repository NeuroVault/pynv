# pyneurovault_upload
Python library for interfacing with http://neurovault.org upload API


## Installation

```
git clone https://github.com/ljchang/pyneurovault_upload.git
cd pyneurovault_upload
python setup.py install
```

## Example Usage

*Initialize a Client instance*

First, we need to create an instance of the Client class. This requires adding your neurovault api key which can be found under ['Personal Access tokens'](http://neurovault.org/accounts/tokens/) tab in the Account Settings.

```python
from pyneurovault_upload.api import Client

api = Client(access_token='your_neurovault_personal_access_token')
```

*Create a Collection*

To create a new collection in neurovault you need to pass a dictionary of all of the metadata you would like to specify in the collection.  At a minimum you must specify a collection name.  Creating a collection will automatically store the collection id in the object instance to help with further methods.

```python
r = api.post(data={'name':'name_of_new_collection'})
```

*Add Image to Collection*

Once a collection is created you can add images to it using the 'add_image()' method.  You need to pass a string indicating the path to the file you would like to upload.  You also need to pass a few parameters as a dictionary, which include the image name, the image modality, and the map type.

```python
image_file='path_to_image_file'
image_data={'name':'Parcellation_k25','modality':'Other','map_type':'Pa'}
r2 = api.add_image(image_file=image_file,image_data=image_data)
```

*Delete a Collection*

To delete the same collection you can simply run the delete method.  You can also delete any collection that you own by passing a 'collection id'.  Be careful with this as you will be unable to recover any collections that you delete!

```python
r3 = api.delete(collection_id=collection_id)
```
