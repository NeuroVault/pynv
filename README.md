# pyneurovault_upload
Python library for interfacing with http://neurovault.org upload API


## Installation
```
git clone https://github.com/ljchang/neurolearn
python setup.py install
```
   
## Example Useage

<em>Initialize an Upload instance</em>

``` python
from pyneurovault_upload.api import Upload

api = Upload(api_key='Your_Neurovault_API_Key')
```

<em>Create a Collection</em>
``` python
r = api.post(data={'name':'name_of_new_collection'})
```

<em>Delete a Collection</em>
``` python
r2 = api.post(collection_id=collection_id)
```

<em>Add Image to Collection</em>
``` python
image_file='path_to_image_file'
image_data={'name':'Parcellation_k25','modality':'Other','map_type':'Pa'}
r3 = api.add_image(image_file=image_file,image_data=image_data)
```
