from django.urls import path, include

from code_app.views import *

urlpatterns = [
    path('codes', UserCodeList.as_view()),
    path('codes/search', Search.as_view()),
    path('codes/<int:pk>/<str:user_name>/<repository>/<str:project_name>', UserCodeShower),
    path('upload-file', UploadForm),
    path('mycode', MyCode.as_view()),
]
