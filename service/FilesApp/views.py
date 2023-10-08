from FilesApp.models import File as FileModel
from FilesApp.serializers import FileSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponseNotFound


class FileViewSet(viewsets.ModelViewSet):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        file = self.request.FILES['file']
        serializer = FileSerializer(
            data=request.data,
            context={
                'file': file
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Загружаем Ваш файл')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")