def test_create_image_with_missing_fields():
    pass


def test_create_image(client, recorder):
    with recorder.use_cassette('add_image'):
        result_dict = client.add_image(
            8477,
            './tests/data/motor_lips.nii.gz',
            name='test image from cli',
            map_type='Z',
            modality='fMRI-BOLD',
        )

    target = {
        'number_of_subjects': None,
        'figure': None,
        'file': 'https://neurovault.org/media/images/8477/motor_lips.nii.gz',
        'map_type': 'Z map',
        'contrast_definition_cogatlas': None,
        'cognitive_paradigm_cogatlas': None,
        'smoothness_fwhm': None,
        'modality': 'fMRI-BOLD',
        'is_valid': False,
        'brain_coverage': 82.00785178766034,
        'reduced_representation': None,
        'perc_bad_voxels': 75.00733967111626,
        'thumbnail': None,
        'description': '',
        'statistic_parameters': None,
        'collection': 'https://neurovault.org/collections/8477/',
        'cognitive_contrast_cogatlas': None,
        'not_mni': False,
        'analysis_level': None,
        'name': 'test image from cli',
        'contrast_definition': None,
        'perc_voxels_outside': 16.94083540566778,
        'is_thresholded': False
    }

    for k, v in target.items():
        assert result_dict[k] == v


def test_read_image(client, recorder):
    with recorder.use_cassette('read_image'):
        result_dict = client.get_image(396069)

    target = {
        'number_of_subjects': None,
        'figure': None,
        'file': 'https://neurovault.org/media/images/8477/motor_lips.nii.gz',
        'map_type': 'Z map',
        'contrast_definition_cogatlas': None,
        'cognitive_paradigm_cogatlas': None,
        'smoothness_fwhm': None,
        'modality': 'fMRI-BOLD',
        'is_valid': False,
        'brain_coverage': 82.0078517876603,
        'reduced_representation': None,
        'perc_bad_voxels': 75.0073396711163,
        'description': '',
        'statistic_parameters': None,
        'collection': 'https://neurovault.org/collections/8477/',
        'cognitive_contrast_cogatlas': None,
        'not_mni': False,
        'analysis_level': None,
        'name': 'test image from cli',
        'contrast_definition': None,
        'perc_voxels_outside': 16.9408354056678,
        'is_thresholded': False
    }

    for k, v in target.items():
        assert result_dict[k] == v


def test_get_collection_images(client, recorder):
    with recorder.use_cassette('get_collection_images'):
        result_dict = client.get_collection_images(1615)

    assert result_dict['count'] == 5

    for image in result_dict['results']:
        assert len(image['name']) > 0

    with recorder.use_cassette('get_collection_images_limit'):
        result_dict = client.get_collection_images(1615, limit=1, offset=2)

    assert int(result_dict['next'].split('&offset=')[-1]) == 3
