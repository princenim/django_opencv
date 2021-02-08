from django.contrib import admin
from .models import ImageUploadModel

#register your models

class ImageUploadAdmin(admin.ModelAdmin):
   list_display = ('description', 'document', ) # list_display 변수명은 고정 - description과 document를 뜨게해줌. ..~

admin.site.register(ImageUploadModel, ImageUploadAdmin)
