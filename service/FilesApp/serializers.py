from rest_framework import serializers
from FilesApp.models import File
from django.core.files.storage import FileSystemStorage
from service.tasks import upload_file


class FileSerializer(serializers.ModelSerializer):
    uploaded_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = File
        fields = 'file', 'uploaded_at', 'processed',
        read_only_fields = 'uploaded_at', 'processed'

    def create(self, validated_data):
        file = self.context['file']
        storage = FileSystemStorage()
        storage.save(file.name, file)
        return upload_file.delay(path=storage.path(file.name), file_name=file.name)
