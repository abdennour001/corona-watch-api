from django.urls import path
from .views import LocationList, LocationRetrieve, RegionListCreate, RegionRUD, ReceptionCenterListCreate, ReceptionCenterRUD, StateList, StateRetrieve, TownList, TownRetrieveUpdate, \
    StateTownList


urlpatterns = [
    # location urls
    path('locations/', LocationList.as_view(), name='locations-list'),
    path('locations/<int:id>', LocationRetrieve.as_view(), name='locations-retrieve'),

    # state urls
    path('states/', StateList.as_view(), name='states-list'),
    path('states/<int:id>', StateRetrieve.as_view(), name='states-retrieve'),
    path('states/<int:state_id>/towns', StateTownList.as_view(), name='states-list-town'),

    # town urls
    path('towns/', TownList.as_view(), name='towns-list'),
    # endpoint towns/
    path('towns/<int:id>', TownRetrieveUpdate.as_view(), name='towns-retrieve-update'),

    # region urls
    path('regions/', RegionListCreate.as_view(), name='region-list'),
    path('regions/<int:id>', RegionRUD.as_view(), name='region-rud'),

    # reception center urls
    path('reception-centers/', ReceptionCenterListCreate.as_view(), name='reception-center-list'),
    path('reception-centers/<int:id>', ReceptionCenterRUD.as_view(), name='reception-center-rud'),


    # advanced statistic endpoints
    # use risked=true to fetch only the risked towns.
    # use validated=true to fetch only the validated towns.
]
