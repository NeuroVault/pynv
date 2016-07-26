
'''
    pyneurovault_upload API Classes
    ===============================
    Classes for interfacing with http://neurovault.org upload api
'''

__all__ = ['Upload']
__author__ = ["Luke Chang"]
__license__ = "MIT"

import urllib2
import requests
import json
import warnings

class Upload(object):
    def __init__(self, url=None, api_key=None, data=None, name=None, metadata=None, collection_id=None, **kwargs):
        
        if url is not None:
            self.url = url
        else:
            self.url='http://neurovault.org/api/collections/'
        
        if api_key is not None:
            self.api_key=api_key
        else:
            self.api_key=None
        
        if name is not None:
            self.name=name
        else:
            self.name=[]            
    
        if collection_id is not None:
            self.collection_id=collection_id
        else:
            self.collection_id=None
        
        self.data_fields = {u'DOI',u'acquisition_orientation',u'authors',u'autocorrelation_model',
                            u'b0_unwarping_software',u'contributors',u'coordinate_space',u'description',
                            u'doi_add_date',u'echo_time',u'field_of_view',u'field_strength',u'flip_angle',
                            u'full_dataset_url',u'functional_coregistered_to_structural',
                            u'functional_coregistration_method',u'group_comparison',u'group_description',
                            u'group_estimation_type',u'group_inference_type',u'group_model_multilevel',
                            u'group_model_type',u'group_modeling_software',u'group_repeated_measures',
                            u'group_repeated_measures_method',u'handedness',u'hemodynamic_response_function',
                            u'high_pass_filter_method',u'inclusion_exclusion_criteria',u'interpolation_method',
                            u'intersubject_registration_software',u'intersubject_transformation_type',
                            u'intrasubject_estimation_type',u'intrasubject_model_type',
                            u'intrasubject_modeling_software',u'journal_name',u'length_of_blocks',u'length_of_runs',
                            u'length_of_trials',u'matrix_size',u'motion_correction_interpolation',
                            u'motion_correction_metric',u'motion_correction_reference',u'motion_correction_software',
                            u'name',u'nonlinear_transform_type',u'number_of_experimental_units',
                            u'number_of_imaging_runs',u'number_of_rejected_subjects',u'object_image_type',
                            u'optimization',u'optimization_method',u'order_of_acquisition',
                            u'order_of_preprocessing_operations',u'orthogonalization_description',u'paper_url',
                            u'parallel_imaging',u'proportion_male_subjects',u'pulse_sequence',u'quality_control',
                            u'repetition_time',u'resampled_voxel_size',u'scanner_make',u'scanner_model',
                            u'skip_distance',u'slice_thickness',u'slice_timing_correction_software',u'smoothing_fwhm',
                            u'smoothing_type',u'software_package',u'software_version',u'subject_age_max',
                            u'subject_age_mean',u'subject_age_min',u'target_resolution',u'target_template_image',
                            u'transform_similarity_metric',u'type_of_design',u'used_b0_unwarping',
                            u'used_dispersion_derivatives',u'used_high_pass_filter',u'used_intersubject_registration',
                            u'used_motion_correction',u'used_motion_regressors',u'used_motion_susceptibiity_correction',
                            u'used_orthogonalization',u'used_reaction_time_regressor',u'used_slice_timing_correction',
                            u'used_smoothing',u'used_temporal_derivatives'}
        
        if data is not None:
            if isinstance(data,dict):
                for key, value in data.iteritems():
                    if key in self.data_fields:
                        self.data[key]=value
                    else:
                        raise ValueError('%s is not a valid neurovault field'% key)
            else:
                raise ValueError('Must supply dictionary of valid neurovault keys')
        else:
            self.data={}
            
    def post(self, data=None, api_key=None):
        ''' Create a new neurovault collection.
        
            Create collection -> POST /api/collections/
            curl -X POST --data name="test collection vis" -H "Authorization: Bearer poR5rbFmymWdT4mxbiENaCW74ZD04YeTLCxGE6dJ" http://neurovault.org/api/collections/
       
        params:
        
            api_key: Neurovault API personal access token
            data: dictionary of neurovault fields to add
        
        returns:
        
            r: requests object
            
         '''
        
        if api_key is not None:
            self.api_key = api_key
        elif self.api_key is None:
            raise ValueError('Must use api-key to put data.')     
        headers = {'Authorization':'Bearer %s' % self.api_key}

        if data is not None:
            if isinstance(data,dict):
                for key, value in data.iteritems():
                    if key in self.data_fields:
                        self.data[key]=value
                    else:
                        raise ValueError('%s is not a valid neurovault field'% key)
            else:
                raise ValueError('Must supply dictionary of valid neurovault keys')
        else:
            raise warnings.warn('Creating new neurovault collection without any new values.')

        r = requests.post(self.url, json=self.data, headers=headers)
        
        # notify of any errors
        r.raise_for_status()
        
        # add new fields to self
        self.json_data = json.loads(r.content)
        self.collection_id = self.json_data['id']
        
        return r
        
    def put(self, collection_id=None, api_key=None):
        '''
        Update all collection properties (e.g. every collection property: name, description, etc.)  -> PUT /api/collections/<COLLECTION_ID>/
        curl --request PUT --data name="test collection" -H "Authorization: Bearer Qv3hafU46d2vXbHtCtOJyFhNX1ta8zTOd36UesMW" http://neurovault.org/api/collections/1165/
        '''
        
        if collection_id is not None:
            self.collection_id = collection_id
        else:
            if self.collection_id is None:
                raise ValueError('Must provide valid collection ID.')
            
        if api_key is not None:
            self.api_key = api_key
        elif self.api_key is None:
            raise ValueError('Must use api-key to put data.')     
        headers = {'Authorization':'Bearer %s' % self.api_key}
                
        r = requests.get(self.url + self.collection_id, params=params, headers=headers)

#         url = 'https://api.github.com/some/endpoint'
#         payload = {'some': 'data'}
#         headers = {'content-type': 'application/json'}
#         r = requests.post(url, data=json.dumps(payload), headers=headers)
        
        
    def patch(self, collection_id=None):
        '''
        Partial update (e.g. a single property or multiple properties) -> PATCH /api/collections/<COLLECTION_ID>/
        curl --request PATCH --data name="test collection" -H "Authorization: Bearer Qv3hafU46d2vXbHtCtOJyFhNX1ta8zTOd36UesMW" http://neurovault.org/api/collections/1165/
        '''
        
    def delete(self, collection_id=None, api_key=None):
        '''
        Delete -> DELETE /api/collections/<COLLECTION_ID>/
        curl -X DELETE -H "Authorization: Bearer Qv3hafU46d2vXbHtCtOJyFhNX1ta8zTOd36UesMW" http://neurovault.org/api/collections/1165/
        Careful with this one. There's no confirmation or undo.
        '''
        
        if api_key is not None:
            self.api_key = api_key
        elif self.api_key is None:
            raise ValueError('Must use api-key to put data.')     
        headers = {'Authorization':'Bearer %s' % self.api_key}

        if collection_id is not None:
            self.collection_id = collection_id
        elif self.collection_id is None:
            raise ValueError('Must specify valid neurovault collection ID.')     
        if not isinstance(self.collection_id,str):
            self.collection_id = str(self.collection_id)
    
        r = requests.delete(self.url + self.collection_id, headers=headers)

        return r

