from django.urls import path

from .apis import house_apis

app_name = 'house_api'
urlpatterns = [
    path('v1/house/<house_id>',
         house_apis.get_house_by_id,
         name='get_house_by_id'),
    path('v1/house/',
         house_apis.get_houses_by_params,
         name='get_houses_by_params'),
]
