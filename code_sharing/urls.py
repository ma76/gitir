from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from code_sharing import settings
from .views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePage),
    path('', include('code_app.urls')),
    path('', include('account_app.urls')),
]

# --- Add Static Files --- #
if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
