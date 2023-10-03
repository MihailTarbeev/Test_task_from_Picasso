from FilesApp.models import File
from FilesApp.serializers import FileSerializer
from rest_framework import viewsets


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    # def create(self, request, *args, **kwargs):
    #     # image = self.request.FILES['image'].read()
    #     #
    #     # byte = base64.b64encode(image)
    #     file = self.request.FILES['file'].read()
    #
    #     data = {
    #         # 'product_id': self.kwargs['product_pk'],
    #         'file': file,
    #         # "name": self.request.FILES['image'].name
    #     }
    #
    #     upload_image.delay(data=data)
    #
    #     return Response('Uploading...')