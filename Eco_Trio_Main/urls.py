from django.contrib import admin
from django.urls import path,include
from Eco_Trio_Sub import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Eco_Trio_Sub.urls')),  # This handles the root URL "/"
    # Add other paths as needed
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)