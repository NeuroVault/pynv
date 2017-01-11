[![build status](https://travis-ci.org/neurolearn/pynv.svg?branch=master)](https://travis-ci.org/neurolearn/pynv)
[![Coverage Status](https://coveralls.io/repos/github/neurolearn/pyneurovault_upload/badge.svg?branch=master&1)](https://coveralls.io/github/neurolearn/pyneurovault_upload?branch=master)

# pynv
Python library for interfacing with http://neurovault.org API


## Installation

1. Method 1 (Recommended)
    ```
    pip install pynv
    ```
 
2. Method 2 (Latest Development Version)
    ```
    git clone https://github.com/neurolearn/pynv.git
    cd pynv
    python setup.py install
    ```

## Example Usage

### Initialize a Client instance

First, we need to create an instance of the Client class. This requires adding your NeuroVault personal access token which can be found under [“Personal Access tokens”](http://neurovault.org/accounts/tokens/) tab in the Account Settings.

```python
from pynv import Client

api = Client(access_token='your_neurovault_personal_access_token')
```

### Create a Collection

To create a new collection in NeuroVault you need to pass a dictionary of all of the metadata you would like to specify in the collection. At a minimum you must specify a collection name.

```python
collection = api.create_collection('a name of a new collection')
```

### Add an image to a collection

Once a collection is created you can add images to it using the `add_image()` method. You need to pass a string indicating the path to the file you would like to upload. You also need to pass a few mandatory parameters, which include the **image name**, the **image modality**, and the **map type**.

Here are tables containing the corresponding to the values required by Neurovault for various image parameters.

| Map Type  | Neurovault Value |
| ------------- | ------------- |
| T map | T |
| Z map  | Z |
| F map | F |
| Chi squared map  | X2 |
| P map (given null hypothesis) | P |
| Multivariate-beta map  | M |
| Univariate-beta map  | U |
| ROI/Mask  | R |
| Parcellation | Pa |
| Anatomical | A |
| Other | OTHER |

| Analysis Level  | Neurovault Value |
| ------------- | ------------- |
| Single-Subject | S |
| Group  | G |
| Meta-Analysis | M |
| Other | OTHER |

| Image Modality  | Neurovault Value |
| ------------- | ------------- |
| fMRI-BOLD | fMRI_BOLD |
| fMRI-CBF  | fMRI_CBF |
| fMRI-CBV | fMRI_CBV |
| Diffusion MRI  | Diffusion_MRI |
| Structural MRI | Structural_MRI |
| PET FDG  | PET_FDG |
| PET [15O]-water  | PET_15O |
| PET Other | PET_OTHER |
| MEG | MEG |
| EEG | EEG |
| Other | OTHER |

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

### Get a collection

You can get information about a collection using the `get_collection()` method.

```python
c = api.get_collection(collection_id=collection)
```

### Get Collection images

To get information about images within a collection, use the `get_collection_images()` method.  You can use the limit and offset keywords to set the pagination.  Here is an example using pagination to get information about collection images into a pandas data frame.

```python
import pandas as pd

offset = 0
limit = 10
i = api.get_collection_images(collection_id=collection, limit=limit,offset=offset)
dat = pd.DataFrame(columns=i['results'][0].keys())
while int(offset) < int(i['count']):
    for x in i['results']:
        dat = dat.append(x,ignore_index=True)
    offset = offset + limit
    i = api.get_collection_images(collection_id=collection, limit=limit, offset=offset)
```
