from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .generator import Generator

def form(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        outFile = []
        genObj = Generator()
        genObj.setInputFile(myfile)
        outFile = genObj.Convert()
        print(outFile)
        return render(request, 'fileform.html', {
                'Output_file_urls': outFile
            })

    return render(request, 'fileform.html')
