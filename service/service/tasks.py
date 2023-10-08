import time
from django.core.files import File
from FilesApp.models import File as FileModel
from celery import shared_task
from django.core.files.storage import FileSystemStorage
from pathlib import Path


@shared_task(bind=True)
def upload_file(self, path, file_name):
    # time.sleep(10)
    storage = FileSystemStorage()
    path_object = Path(path)
    with path_object.open(mode='rb') as file:
        picture = File(file, name=path_object.name)
        instance = FileModel(file=picture, processed=True)
        instance.save()
    storage.delete(file_name)
