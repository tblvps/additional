
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.decorators import secure_admin_login
from accounts.views import index_view
from github.views import list_repos
from oauth2_provider import urls as oauth2_urls

#admin.autodiscover()
#admin.site.login = secure_admin_login(admin.site.login)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', index_view, name='index'),
    path('github/', list_repos, name='list_repos'),
    path("_allauth/", include("allauth.headless.urls")),
    path('', include('env.urls')),
    path('accounts/', include('accounts.urls')),
    path('o/', include(oauth2_urls)),
   # path('api/', include('api.urls')),
   # path('ai/', include('ai.urls')),
   # path('ml/', include('ml.urls')),
   # path('aws/', include('aws.urls')),
   # path('azure/', include('azure.urls')),
    path('github/', include('github.urls')),
   # path('google/', include('google.urls')),
   # path('hotzer/', include('hotzer.urls')),
   # path('linode/', include('linode.urls')),
   # path('vuiltr/', include('vuiltr.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
