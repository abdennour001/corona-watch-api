from django.urls import path
from .views import SuspectedCaseCreateListView, SuspectedCaseRetrieveDeleteView, SuspectedCaseUpdateView, DeclaredRetrieveDeleteView, DeclaredCreateListView, DeclaredUpdateView

app_name = 'reports'

urlpatterns = [
    # suspected cases urls
    path('suspected-cases/', SuspectedCaseCreateListView.as_view(), name='suspected-cases-list'),
    path('suspected-cases/<int:id>', SuspectedCaseRetrieveDeleteView.as_view(), name='suspected-cases-RUD'),
    path('suspected-cases/treat/<int:id>', SuspectedCaseUpdateView.as_view(), name='suspected-cases-update'),

    # declared urls
    path('declared-cases/', DeclaredCreateListView.as_view(), name='declared-cases-list'),
    path('declared-cases/<int:id>', DeclaredRetrieveDeleteView.as_view(), name='declared-cases-RUD'),
    path('declared-cases/treat/<int:id>', DeclaredUpdateView.as_view(), name='declared-cases-update'),
]
