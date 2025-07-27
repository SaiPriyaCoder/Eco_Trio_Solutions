from django.contrib import admin
from django.urls import path
from Eco_Trio_Sub import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # This handles the root URL "/"
    # Add other paths as needed
]
