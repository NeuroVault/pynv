import os

import betamax

from pyneurovault_upload import Client

ACCESS_TOKEN = os.environ.get('NEUROVAULT_ACCESS_TOKEN')


def test_create_image_with_missing_fields():
    pass


def test_create_image():
    client = Client(access_token=ACCESS_TOKEN)

    recorder = betamax.Betamax(client.session)
    with recorder.use_cassette('add_image'):
        result_dict = client.add_image(1167)

    print result_dict

    assert result_dict == {
        'number_of_subjects': None,
        'figure': None,
        'file': 'http://neurovault.org/media/images/1167/motor_lips_1.nii.gz',
        'map_type': 'Z',
        'id': 24369,
        'contrast_definition_cogatlas': None,
        'cognitive_paradigm_cogatlas': None,
        'add_date': '2016-08-03T23:32:51.999164Z',
        'smoothness_fwhm': None,
        'modality': 'fMRI-BOLD',
        'is_valid': False,
        'polymorphic_ctype': 23,
        'brain_coverage': 82.00785178766034,
        'reduced_representation': None,
        'perc_bad_voxels': 75.00733967111626,
        'thumbnail': None,
        'description': '',
        'statistic_parameters': None,
        'collection': 1167,
        'cognitive_contrast_cogatlas': None,
        'ignore_file_warning': False,
        'data': {},
        'not_mni': False,
        'analysis_level': None,
        'name': 'test image from cli',
        'contrast_definition': None,
        'modify_date': '2016-08-03T23:32:51.999183Z',
        'perc_voxels_outside': 16.94083540566778,
        'is_thresholded': False
    }


def test_read_image():
    pass


def test_update_image():
    pass


def test_delete_image():
    pass
