from django.core.exceptions import ValidationError


def validate_size(data):
    '''Validator which  allows to restrict the maximum size of the file up to 100 mb.
        It is used directly in ExcelFile model's FileField as an argument next to FileExtensionValidator'''

    if data.size > 100000000:
        raise ValidationError("The maximum file size is restricted to 100 mb. Please check your file and try once again.")