from rest_framework import viewsets, permissions
from .serializers import ExcelFileCreateSerializer, ExcelFileDetailedSerializer
from .models import ExcelFile


class ExcelViewSet(viewsets.ModelViewSet):

    queryset = ExcelFile.objects.all()

    def get_serializer_class(self):
        '''This overwrite of get_serializer_class method allows to assign the specific serializer
            for 'create' action of instance and the different one for any other actions.'''

        if self.action == 'create':
            return ExcelFileCreateSerializer
        return ExcelFileDetailedSerializer

    def get_permissions(self):
        '''This overwrite of get_permissions method allows to perform all the actions by any user besides
            the 'delete' action which is restricted to be performed only by the logged-in user with admin rights.'''

        if self.request.method == 'DELETE':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
