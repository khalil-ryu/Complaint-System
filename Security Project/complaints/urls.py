from django.urls import path
from .views import submit_complaint, list_complaints, view_complaint

app_name = 'complaints'  # This is the application namespace

urlpatterns = [
    path('submit/', submit_complaint, name='submit_complaint'),
    path('list/', list_complaints, name='list_complaints'),
    path('<int:pk>/', view_complaint, name='view_complaint'),
]
