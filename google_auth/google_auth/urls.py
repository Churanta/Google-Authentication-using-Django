
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #step 5
    path('accounts/', include('allauth.urls')),
]
