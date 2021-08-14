import os
from django.urls.conf import path
from files.models import FilesAdmin
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import Http404,HttpResponse, response
from .form import FilesAdminForm

# Create your views here.



def home(request):
    context={'file' : FilesAdmin.objects.all()}
    return render(request,'files/index.html',context)

def uploadfile(request):
    forms = FilesAdminForm()
    if request.method == 'POST':
        forms = FilesAdminForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            context = {'Upload':"Success"}
            return render(request,'files/upload.html',context)
        else:
            form = FilesAdminForm()
    return render(request,'files/upload.html',context = {'form':forms})
    

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response = HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

        raise Http404
