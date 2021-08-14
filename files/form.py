from django import forms
from .models import FilesAdmin

class FilesAdminForm(forms.ModelForm):
    class Meta:
        model = FilesAdmin
        fields = ('adminupload','title',)