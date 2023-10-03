from django.contrib import admin
from FilesApp.models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ["file", "uploaded_at", "processed"]


admin.site.register(File, FileAdmin)
