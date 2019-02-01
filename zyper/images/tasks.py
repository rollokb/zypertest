from io import BytesIO
from PIL import Image

from django.core.files import File
from celery import shared_task


@shared_task
def gen_thumbnail(image_file_id):
    from zyper.images.models import ImageFile

    image_file = ImageFile.objects.get(id=image_file_id)

    in_mem_original = BytesIO(
        image_file.file_original.open().read()
    )

    thumb = Image.open(in_mem_original)
    thumb.thumbnail((300,300))

    in_mem_thumb = BytesIO()
    thumb.save(in_mem_thumb, format='PNG')
    in_mem_thumb.seek(0)
    image_file.file_thumb.save(
        'thumb_300_{}'.format(image_file.file_original.name),
        File(in_mem_thumb)
    )
    image_file.save()

    in_mem_original.close()
    in_mem_thumb.close()
