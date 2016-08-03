# pyneurovault_upload
Python library for interfacing with http://neurovault.org upload API


## Installation

```
git clone https://github.com/ljchang/pyneurovault_upload.git
cd pyneurovault_upload
python setup.py install
```

## Example Useage

<em>Initialize a Client instance</em>
<p>
First, we need to create an instance of the Client class.  This requires adding your neurovault api key which can be found under 'Personal Access tokens' tab in the Account Settings.
</p>

``` python
from pyneurovault_upload.api import Client

api = Client(api_key='Your_Neurovault_API_Key')
```

<em>Create a Collection</em>
<p>
To create a new collection in neurovault you need to pass a dictionary of all of the metadata you would like to specify in the collection.  At a minimum you must specify a collection name.  Creating a collection will automatically store the collection id in the object instance to help with further methods.
</p>

``` python
r = api.post(data={'name':'name_of_new_collection'})
```

<em>Add Image to Collection</em>
<p>
Once a collection is created you can add images to it using the 'add_image()' method.  You need to pass a string indicating the path to the file you would like to upload.  You also need to pass a few parameters as a dictionary, which include the image name, the image modality, and the map type.
</p>

``` python
image_file='path_to_image_file'
image_data={'name':'Parcellation_k25','modality':'Other','map_type':'Pa'}
r2 = api.add_image(image_file=image_file,image_data=image_data)
```

<em>Delete a Collection</em>
<p>
To delete the same collection you can simply run the delete method.  You can also delete any collection that you own by passing a 'collection id'.  Be careful with this as you will be unable to recover any collections that you delete!
</p>

``` python
r3 = api.delete(collection_id=collection_id)
```
