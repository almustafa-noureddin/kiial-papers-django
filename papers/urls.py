from django.urls import path
from .views import (
    IndexListView,
    PaperListView,
    PaperDetailView,
    PaperCreateView,
    PaperUpdateView,
    PaperDeleteView,
    ResearcherListView,
    ResearcherDetailView,
    ResearcherCreateView,
    ResearcherUpdateView,
    ResearcherDeleteView,
    SupervisorListView,
    SupervisorDetailView,
    SupervisorCreateView,
    SupervisorUpdateView,
    SupervisorDeleteView,
)

app_name = "papers"

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('papers/', PaperListView.as_view(), name='papers_list'),
    path('paper/<int:pk>/', PaperDetailView.as_view(), name='paper_detail'),
    path('create/paper/', PaperCreateView.as_view(), name='create_paper'),
    path('update/paper/<int:pk>/', PaperUpdateView.as_view(), name='update_paper'),
    path('delete/paper/<int:pk>/', PaperDeleteView.as_view(), name='delete_paper'),
    path('researchers/', ResearcherListView.as_view(), name='researchers_list'),
    path('researcher/<int:pk>/', ResearcherDetailView.as_view(), name='researcher_detail'),
    path('create/researcher/', ResearcherCreateView.as_view(), name='create_researcher'),
    path('update/researcher/<int:pk>/', ResearcherUpdateView.as_view(), name='update_researcher'),
    path('delete/researcher/<int:pk>/', ResearcherDeleteView.as_view(), name='delete_researcher'),
    path('supervisors/', SupervisorListView.as_view(), name='supervisors_list'),
    path('supervisor/<int:pk>/', SupervisorDetailView.as_view(), name='supervisor_detail'),
    path('create/supervisor/', SupervisorCreateView.as_view(), name='create_supervisor'),
    path('update/supervisor/<int:pk>/', SupervisorUpdateView.as_view(), name='update_supervisor'),
    path('delete/supervisor/<int:pk>/', SupervisorDeleteView.as_view(), name='delete_supervisor'),
#    path('<int:pk>',.as_view(), name='papers-details'),
]