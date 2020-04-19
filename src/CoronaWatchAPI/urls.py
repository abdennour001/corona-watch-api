from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from django.conf import settings

API_PREFIX = f'coronawatch-api/{settings.API_VERSION}'

urlpatterns = [
    path('admin/', admin.site.urls),

    path(f'{API_PREFIX}/feeds/', include('feeds.api.urls'), name='api-publications'),
    path(f'{API_PREFIX}/attachments/', include('attachments.api.urls'), name='api-attachments'),
    path(f'{API_PREFIX}/reports/', include('reports.api.urls'), name='api-reports'),
    path(f'{API_PREFIX}/geolocation/', include('geolocation.api.urls'), name='api-geolocation'),

    path(f'{API_PREFIX}/docs/', include_docs_urls(title='CoronaWatch API'))
]
