def test_create_image_with_missing_fields():
    pass


def test_create_image(client, recorder):
    with recorder.use_cassette('add_image'):
        result_dict = client.add_image(
            1167,
            './tests/data/motor_lips.nii.gz',
            name='test image from cli',
            map_type='Z',
            modality='fMRI-BOLD',
        )

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


def test_read_image(client, recorder):
    with recorder.use_cassette('read_image'):
        image = client.get_image(15826)

    assert image == {
        'cognitive_contrast_cogatlas_id': None,
        'number_of_subjects': None,
        'cognitive_paradigm_cogatlas': None,
        'file': 'http://neurovault.org/media/images/1167/motor_lips.nii.gz',
        'file_size': 856688,
        'brain_coverage': 82.0078517876603,
        'id': 15826,
        'contrast_definition_cogatlas': None,
        'figure': None,
        'add_date': '2016-02-05T21:18:46.661420Z',
        'cognitive_paradigm_cogatlas_id': None,
        'smoothness_fwhm': None,
        'modality': 'fMRI-BOLD',
        'is_valid': False,
        'reduced_representation': 'http://neurovault.org'
                                  '/media/images/1167/transform_4mm_15826.npy',
        'not_mni': False,
        'thumbnail': 'http://neurovault.org'
                     '/media/images/1167/glass_brain_15826.jpg',
        'collection_id': 1167,
        'description': '',
        'statistic_parameters': None,
        'collection': 'http://neurovault.org/collections/1167/',
        'cognitive_contrast_cogatlas': None,
        'map_type': 'T map',
        'perc_bad_voxels': 75.0073396711163,
        'analysis_level': None,
        'name': 'new_image_name',
        'url': 'http://neurovault.org/images/15826/',
        'contrast_definition': None,
        'image_type': 'statistic_map',
        'modify_date': '2016-02-05T21:18:49.547536Z',
        'perc_voxels_outside': 16.9408354056678,
        'is_thresholded': False
    }


def test_update_image(client, recorder):
    with recorder.use_cassette('update_image'):
        image = client.get_image(15826)
        new_name = image['name'] + ' <updated>'
        updated_image = client.update_image(15826, name=new_name)
    assert updated_image['name'] == new_name


def test_delete_image(client, recorder):
    with recorder.use_cassette('delete_image'):
        response = client.delete_image(15826)
    assert response.ok


def test_get_collection_images(client, recorder):
    with recorder.use_cassette('get_collection_images'):
        result_dict = client.get_collection_images(1615)

    assert result_dict['count'] == 2

    for image in result_dict['results']:
        assert len(image['name']) > 0

    with recorder.use_cassette('get_collection_images'):
        result_dict = client.get_collection_images(1615,limit=1,offset=2)
    assert int(i['next'].split('&offset=')[-1]) == 3

