from django.urls import path
from .views import UserList, UserDetail, UserMedicalProfileDetail, UserCreate

urlpatterns = [

    # POST to this url to make new user

    # GET here to get a list of all users.
    path('', UserList.as_view(), name='list of users'),

    path('new-user/', UserCreate.as_view(), name='create new user'),

    # GET to return user <username> details
    path('<username>/', UserDetail.as_view(), name='detail of user'),

    # GET to this url to get user medical profile
    path('<username>/profile', UserMedicalProfileDetail.as_view(), name='medical profile of this user'),

    # TODO: update medical profile
]
