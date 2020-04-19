from django.urls import path
from .views import SuspectedCaseCreateListView, SuspectedCaseRUDView


urlpatterns = [
    # attachments urls
    path('suspected-cases/', SuspectedCaseCreateListView.as_view(), name='suspected-cases-list'),
    path('<int:id>', SuspectedCaseRUDView.as_view(), name='suspected-cases-RUD'),
]