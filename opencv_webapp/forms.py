from django import forms
from .models import ImageUploadModel

# 직접 form를 구성.

#사용자로부터 이미지를  파일을 업로드받아 프로젝트 media에 저장하는 역할까지 수행.
class SimpleUploadForm(forms.Form): # 클래스 Form 상속

    title = forms.CharField(max_length=50)  #유저에게 받는 첫번째 항목.
    image = forms.ImageField()  # 이미지를 받는 부분.
    # file = forms.FileField() - 이미지가 아닌 파일을 받을 때 사용

#위와는 달리 사용자로부터 이미지 파일을 업로드 받아 Database에 저장을 마친 후,
#저장이 완료된 이미지 파일을 대상으로 Face detection까지 적용한다는 차이점이 존재
class ImageUploadForm(forms.ModelForm):
    # Form을 통해 받아들여야 할 데이터가 명시되어 있는 메타 데이터 (DB 테이블을 연결)
    class Meta:
        model = ImageUploadModel
        fields = ('description', 'document', ) # uploaded_at
