from django.db import models
from django.core.validators import FileExtensionValidator
from .validators import validate_size
import re


def fileName(instance, filename) -> str:
    '''Result of this function is passed as an "upload_to" argument into ExcelFile model's FileField.
        It helps to specify the custom behaviour during creation of the uploaded file and avoid the random
        hashed extension to the filename which was yet the name of the file being uploaded previously.'''

    original_name = re.match('.*(?=\.)', filename).group(0)
    extension = re.search(r'\.[^.]*$', filename).group(0)
    uploaded_str = instance.uploaded_at.strftime("%Y-%d-%m-%H%M%S")
    return '{}_{}{}'.format(original_name, uploaded_str, extension)


class ExcelFile(models.Model):
    '''Model which contains the FileField allowing the user to upload the file into API.
        The constraints does not allow to put the blank and the validators help to avoid uploading
        the other file extension than '.xlsx'. Files bigger than 100 mb size are disallowed as well.'''

    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=fileName, blank=False, null=False, validators=[FileExtensionValidator(['xlsx']), validate_size])
    columns = models.CharField(max_length=255)

    def __str__(self):
        return '{} ({})'.format(self.columns, self.file)

