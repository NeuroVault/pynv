
'''
    pyneurovault_upload API Classes
    ===============================
    Classes for interfacing with http://neurovault.org upload api
'''

__all__ = ['Client']
__author__ = ['Luke Chang']
__license__ = 'MIT'

import requests
import json
import warnings
import os

from . import API_BASE_URL


class Client(object):
    '''
    A python interface into the NeuroVault API

    Example usage
        Import the class
        >>> from pyneurovault_upload import Client

        To create an instance of the Client class, with no
        authentication (anonymous API call):

        >>> upload = Client()

        Or with personal access token authentication:

        >>> upload = Client(access_token='y3o1u4r1a5c9c2e6s5s3t5o8k9e7n9')
    '''

    def __init__(self, url=None,
                 access_token=None,
                 data=None,
                 name=None,
                 metadata=None,
                 collection_id=None,
                 api_base_url=None,
                 **kwargs):
        '''
        Instantiate a new NeuroVault Client object.
        Args:

            access_token: Neurovault API personal access token
            data: dictionary of neurovault fields to add
        '''
        self.api_base_url = api_base_url or API_BASE_URL

        if url is not None:
            self.url = url
        else:
            self.url = '%s%s' % (self.api_base_url, '/collections/')

        if access_token is not None:
            self.access_token = access_token
        else:
            self.access_token = None

        if name is not None:
            self.name = name
        else:
            self.name = []

        if collection_id is not None:
            self.collection_id = collection_id
        else:
            self.collection_id = None

        self.data_fields = {u'DOI', u'acquisition_orientation', u'authors', u'autocorrelation_model',
                            u'b0_unwarping_software', u'contributors', u'coordinate_space', u'description',
                            u'doi_add_date', u'echo_time', u'field_of_view', u'field_strength', u'flip_angle',
                            u'full_dataset_url', u'functional_coregistered_to_structural',
                            u'functional_coregistration_method', u'group_comparison', u'group_description',
                            u'group_estimation_type', u'group_inference_type', u'group_model_multilevel',
                            u'group_model_type', u'group_modeling_software', u'group_repeated_measures',
                            u'group_repeated_measures_method', u'handedness', u'hemodynamic_response_function',
                            u'high_pass_filter_method', u'inclusion_exclusion_criteria', u'interpolation_method',
                            u'intersubject_registration_software', u'intersubject_transformation_type',
                            u'intrasubject_estimation_type', u'intrasubject_model_type',
                            u'intrasubject_modeling_software', u'journal_name', u'length_of_blocks', u'length_of_runs',
                            u'length_of_trials', u'matrix_size', u'motion_correction_interpolation',
                            u'motion_correction_metric', u'motion_correction_reference', u'motion_correction_software',
                            u'name', u'nonlinear_transform_type', u'number_of_experimental_units',
                            u'number_of_imaging_runs', u'number_of_rejected_subjects', u'object_image_type',
                            u'optimization', u'optimization_method', u'order_of_acquisition',
                            u'order_of_preprocessing_operations', u'orthogonalization_description', u'paper_url',
                            u'parallel_imaging', u'proportion_male_subjects', u'pulse_sequence', u'quality_control',
                            u'repetition_time', u'resampled_voxel_size', u'scanner_make', u'scanner_model',
                            u'skip_distance', u'slice_thickness', u'slice_timing_correction_software', u'smoothing_fwhm',
                            u'smoothing_type', u'software_package', u'software_version', u'subject_age_max',
                            u'subject_age_mean', u'subject_age_min', u'target_resolution', u'target_template_image',
                            u'transform_similarity_metric', u'type_of_design', u'used_b0_unwarping',
                            u'used_dispersion_derivatives', u'used_high_pass_filter', u'used_intersubject_registration',
                            u'used_motion_correction', u'used_motion_regressors', u'used_motion_susceptibiity_correction',
                            u'used_orthogonalization', u'used_reaction_time_regressor', u'used_slice_timing_correction',
                            u'used_smoothing', u'used_temporal_derivatives'}

        if data is not None:
            if isinstance(data, dict):
                for key, value in data.iteritems():
                    if key in self.data_fields:
                        self.data[key] = value
                    else:
                        raise ValueError(
                            '%s is not a valid neurovault field' % key)
            else:
                raise ValueError(
                    'Must supply dictionary of valid neurovault keys')
        else:
            self.data = {}

    def post(self, data=None, access_token=None):
        ''' Create a new neurovault collection.

            Create collection -> POST /api/collections/
            curl -X POST --data name="test collection vis" -H "Authorization: Bearer poR5rbFmymWdT4mxbiENaCW74ZD04YeTLCxGE6dJ" http://neurovault.org/api/collections/

        Args:

            access_token: Neurovault API personal access token
            data: dictionary of neurovault fields to add

        Returns:

            r: requests object

         '''

        if access_token is not None:
            self.access_token = access_token
        elif self.access_token is None:
            raise ValueError('Must use api-key to put data.')

        headers = {'Authorization': 'Bearer %s' % self.access_token}

        if data is not None:
            if isinstance(data, dict):
                for key, value in data.iteritems():
                    if key in self.data_fields:
                        self.data[key] = value
                    else:
                        raise ValueError(
                            '%s is not a valid neurovault field' % key)
            else:
                raise ValueError(
                    'Must supply dictionary of valid neurovault keys')
        else:
            raise warnings.warn(
                'Creating new neurovault collection without any new values.')

        r = requests.post(self.url, json=self.data, headers=headers)

        # notify of any errors
        r.raise_for_status()

        # add new fields to self
        self.json_data = json.loads(r.content)
        self.collection_id = self.json_data['id']

        return r

    def put(self, collection_id=None, access_token=None):
        '''
        Update all collection properties (e.g. every collection property: name, description, etc.)  -> PUT /api/collections/<COLLECTION_ID>/
        curl --request PUT --data name="test collection" -H "Authorization: Bearer Qv3hafU46d2vXbHtCtOJyFhNX1ta8zTOd36UesMW" http://neurovault.org/api/collections/1165/
        '''

        raise NotImplementedError()

    def patch(self, collection_id=None):
        '''
        Partial update (e.g. a single property or multiple properties) -> PATCH /api/collections/<COLLECTION_ID>/
        curl --request PATCH --data name="test collection" -H "Authorization: Bearer Qv3hafU46d2vXbHtCtOJyFhNX1ta8zTOd36UesMW" http://neurovault.org/api/collections/1165/
        '''

        raise NotImplementedError()

    def delete(self, collection_id=None, access_token=None):
        ''' Delete a neurovault collection.

            Careful with this one. There's no confirmation or undo.

            curl -X DELETE -H "Authorization: Bearer Qv3hafU46d2vXbHtCtOJyFhNX1ta8zTOd36UesMW" http://neurovault.org/api/collections/1165/

        Args:

            collection_id: a neurovault collection ID
            access_token: Neurovault API personal access token

        Returns:

            r: requests object

        '''

        if access_token is not None:
            self.access_token = access_token
        elif self.access_token is None:
            raise ValueError('Must use api-key to put data.')
        headers = {'Authorization': 'Bearer %s' % self.access_token}

        # We should add a check to see if the collection ID exists
        if collection_id is not None:
            self.collection_id = collection_id
        elif self.collection_id is None:
            raise ValueError('Must specify a neurovault collection ID.')

        r = requests.delete(
            self.url + str(self.collection_id), headers=headers)

        # notify of any errors
        r.raise_for_status()

        return r

    def add_image(self, image_file=None, image_data=None, access_token=None, collection_id=None):
        ''' Add a new image to a neurovault collection

            curl -H "Authorization: Bearer poR5rbFmymWdT4mxbiENaCW74ZD04YeTLCxGE6dJ" -F "map_type=T" -F "name=new_image_name" -F "modality=fMRI-BOLD" -F "file=@/Users/lukechang/Downloads/Test_Brain_Data/visual_test.nii.gz" http://neurovault.org/api/collections/1205/images/

        Args:

            image_file: path to image file to upload
            collection_id: a neurovault collection ID
            access_token: Neurovault API personal access token
            data: dictionary of neurovault fields to add

        Returns:

            r: requests object

        '''

#             MAP_TYPE_CHOICES = (
#         (T, 'T map'),
#         (Z, 'Z map'),
#         (F, 'F map'),
#         (X2, 'Chi squared map'),
#         (P, 'P map (given null hypothesis)'),
#         (M, 'multivariate-beta map'),
#         (U, 'univariate-beta map'),
#         (R, 'ROI/mask'),
#         (Pa, 'parcellation'),
#         (A, 'anatomical'),
#         (OTHER, 'other'),
#     )
#     ANALYSIS_LEVEL_CHOICES = (
#         (S, 'single-subject'),
#         (G, 'group'),
#         (M, 'meta-analysis'),
#         (OTHER, 'other'),
#     )
#     MODALITY_CHOICES = (
#         (fMRI_BOLD, 'fMRI-BOLD'),
#         (fMRI_CBF, 'fMRI-CBF'),
#         (fMRI_CBV, 'fMRI-CBV'),
#         (Diffusion_MRI, 'Diffusion MRI'),
#         (Structural_MRI, 'Structural MRI'),
#         (PET_FDG, 'PET FDG'),
#         (PET_15O, 'PET [15O]-water'),
#         (PET_OTHER, 'PET other'),
#         (MEG, 'MEG'),
#         (EEG, 'EEG'),
#         (Other, 'Other')
#     )

        if access_token is not None:
            self.access_token = access_token
        elif self.access_token is None:
            raise ValueError('Must use api-key to put data.')
        headers = {'Authorization': 'Bearer %s' % self.access_token}

        # we should add check to make sure collection exists
        if collection_id is not None:
            self.collection_id = collection_id
        elif self.collection_id is None:
            raise ValueError('Must specify a neurovault collection ID.')

        if image_data is not None:
            if isinstance(data, dict):
                if set(image_data.keys()).issuperset({'modality', 'name', 'map_type'}):
                    self.image_data = image_data
                else:
                    raise ValueError(
                        '"name", "map_type", and "modality" are required in image_data dictionary.')
            else:
                raise ValueError('image_data must be a dictionary.')
        else:
            raise ValueError(
                'You must include an image_data dictionary including "name", "map_type", and "modality".')

        # requests has difficulty with large files
        # https://toolbelt.readthedocs.io/en/latest/uploading-data.html
        if image_file is not None:
            if os.path.isfile:
                files = {'file': open(image_file, 'rb')}
            else:
                raise ValueError('Image file does not exist.')
        else:
            raise ValueError('Must specify a valid image file to upload.')

        r = requests.post(self.url + str(self.collection_id) +
                          '/images/', files=files, data=self.image_data, headers=headers)

        # notify of any errors
        r.raise_for_status()

        # add new fields to self
        self.json_image_data = json.dumps(r.content)
#         self.image_id = self.json_image_data['id']

        return r
