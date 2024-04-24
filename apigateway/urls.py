from django.contrib import admin
from django.urls import path, include
from api.views import CodeView
from api.views import def_resource
# from oauth2_provider.views.generic import AuthorizationView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('codigo/', CodeView.as_view(), name='pk_view'),
    path('recurso/', def_resource, name='pk_proctected_view'),
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
