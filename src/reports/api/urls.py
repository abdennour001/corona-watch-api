from django.urls import path
from .views import SuspectedCaseListView, ReportSuspectedCase, SuspectedCaseRUDView


urlpatterns = [
    # attachments urls
    path('', SuspectedCaseListView.as_view(), name='suspected-cases-list'),
    path('report', ReportSuspectedCase.as_view(), name='report-case'),
    path('<int:id>', SuspectedCaseRUDView.as_view(), name='suspected-cases-RUD'),
]