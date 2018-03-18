from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('vgulage.urls')),
    url(r'^vgulage/', include('vgulage.urls')),
    url(r'^admin/', admin.site.urls),
]