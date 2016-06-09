from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('peliculas.urls')),
    url(r'^accounts/', include('accounts.urls')),
]
