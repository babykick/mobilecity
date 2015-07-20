from django import forms
import os.path

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    comment = forms.CharField(max_length=100)
    file = forms.FileField()
    
def handle_uploaded_file(fobj):
    with open(os.path.join('files', fobj.name), 'wb+') as f:
        f.write(fobj.read())
           
