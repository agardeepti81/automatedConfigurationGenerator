from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .generator import Generator

def form(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        genObj = Generator()
        genObj.setInputFile(myfile)
        outFile = genObj.Convert()
        for i in outFile:
            converted_file_url = fs.url(i)
            return render(request, 'fileform.html', {
                'uploaded_file_url': converted_file_url
            })
    return render(request, 'fileform.html')
