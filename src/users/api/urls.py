from django.conf.urls import url
from django.urls import path
from .views import UserList, UserDetail, UserMedicalProfileDetail, UserCreate, UserAuthToken
from rest_framework.authtoken import views

urlpatterns = [

    # POST to this url to make new user

    # GET here to get a list of all users.
    path('', UserList.as_view(), name='list of users'),

    path('new-user', UserCreate.as_view(), name='create new user'),

    # GET to this url to get user medical profile
    path('<username>/profile', UserMedicalProfileDetail.as_view(), name='medical profile of this user'),

    path('api-token-auth', UserAuthToken.as_view()),

    # GET to return user <username> details
    path('<username>', UserDetail.as_view(), name='detail of user'),

    # TODO: update medical profile
]
