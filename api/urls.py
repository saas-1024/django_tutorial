from api.spectacular.urls import urlpatterns as doc_urls
from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += doc_urls
