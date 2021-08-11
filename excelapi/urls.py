from django.urls import path
from .views import ExcelViewSet

file_list = ExcelViewSet.as_view({"get": "list"})
file_detail = ExcelViewSet.as_view({"get": "retrieve", "delete": "destroy"})
file_create = ExcelViewSet.as_view({"post": "create"})

urlpatterns = [
    path("files/create/", file_create, name="file-create"),
    path("files/", file_list, name="file-list"),
    path("files/<int:pk>/", file_detail, name="file-detail")
]