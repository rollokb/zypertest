import pytest
import boto3

from unittest.mock import MagicMock
from io import BytesIO
from moto import mock_s3

from zyper.images.models import ImageFile


@pytest.mark.django_db
def test_index(client):
    image_file1 = ImageFile.objects.create()
    image_file2 = ImageFile.objects.create()
    res = client.get('/images/')
    assert len(res.json()) == 2


@pytest.mark.django_db
def test_get(client):
    image_file1 = ImageFile.objects.create(
        name='test'
    )

    res = client.get(
        '/images/{}/'.format(image_file1.id)
    )

    assert res.json().items() >= {
        'name': 'test',
        'id': 1
    }.items()


@pytest.mark.django_db
def test_post(client, monkeypatch):
    with mock_s3():
        conn = boto3.resource('s3', region_name='eu-west-2')
        conn.create_bucket(Bucket='zypertest')

        monkeypatch.setattr(
            'zyper.images.views.gen_thumbnail',
            MagicMock()
        )

        res = client.post(
            '/images/',
            {
                'name': 'test',
                'file_original': BytesIO(b'test')
            }
        )

        assert res.json().items() >= {
            'id': 1,
            'file_thumb': None,
            'file_original': 'https://zypertest.s3.amazonaws.com/file_original',
            'name': 'test', 
        }.items()
