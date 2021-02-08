from django.shortcuts import render, redirect
from .forms import SimpleUploadForm, ImageUploadForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .cv_functions import cv_detect_face




def first_view(request):
    return render(request, 'opencv_webapp/first_view.html', {}) #{}비어있는 context


def simple_upload(request):
    if request.method == 'POST':

        # post로 받아온 후, 비어있는 Form에 사용자가 업로드한 데이터를 넣고 검증.
        form = SimpleUploadForm(request.POST, request.FILES)

        if form.is_valid():
            myfile = request.FILES['image'] # 'ses.jpg' # 이미지를 뽑아냄.
            fs = FileSystemStorage()

            # myfile - ses.jpg .라는 파일 자체 .
            filename = fs.save(myfile.name, myfile) # 경로명을 포함한 파일명 & 파일 객체를 넘겨주기 , save로 저장, ses.jpg'

            #업로드된 이미지 파일의 저장돤 경로()을 얻어내 Template에게 전달
            uploaded_file_url = fs.url(filename) # '/media/ses.jpg'

            context = {'form': form, 'uploaded_file_url': uploaded_file_url} # filled form
            return render(request, 'opencv_webapp/simple_upload.html', context)

    else: # GET일때
        form = SimpleUploadForm() # empty form
        context = {'form':form}
        return render(request, 'opencv_webapp/simple_upload.html', context)


def detect_face(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES) # filled form
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.document.name
                     # = '/media/' + 'ses.jpg'
                     # = '/media/ses.jpg'


            # document : ImageUploadModel Class에 선언되어 있는 “document”에 해당
            # print(
            # form.instance,                ImageUploadModel object (1)
            # form.instance.document.name,  images/2021/02/08/ses.jpg
            # form.instance.document.url    /media/images/2021/02/08/ses.jpg
            # )
            cv_detect_face(settings.MEDIA_ROOT_URL + imageURL)
            #cv_detect_face('./media/ses.jpg') # 추후 구현 예정

            context = {'form':form, 'post':post}
            return render(request, 'opencv_webapp/detect_face.html', context)
    else:
        form = ImageUploadForm() # empty forms
        return render(request, 'opencv_webapp/detect_face.html', {'form':form})
