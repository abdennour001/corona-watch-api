from django.urls import path
from .views import LocationListCreate, LocationRUD, RegionListCreate, RegionRUD, ReceptionCenterListCreate, ReceptionCenterRUD

urlpatterns = [
    # location urls
    path('locations/', LocationList.as_view(), name='locations-list'),
    path('locations/<int:id>', LocationRUD.as_view(), name='locations-rud'),

    # region urls
    path('regions/', RegionListCreate.as_view(), name='region-list'),
    path('regions/<int:id>', RegionRUD.as_view(), name='region-rud'),

    # reception center urls
    path('reception-centers/', ReceptionCenterListCreate.as_view(), name='reception-center-list'),
    path('reception-centers/<int:id>', ReceptionCenterRUD.as_view(), name='reception-center-rud'),
]
