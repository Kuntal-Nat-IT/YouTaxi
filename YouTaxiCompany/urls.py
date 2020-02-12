from django.urls import path
from .import views


urlpatterns = [
    path('create/', views.CreateCompany, name=""),
    path('show/list/', views.GetAllCompany, name=""),
    path('get/<slug:slug>/', views.GetCompanyByID, name=""),
    path('update/<slug:slug>/', views.UpdateCompanyByID, name=""),
    path('status/change/<slug:slug>/', views.ChangeStatus, name=""),
    path('activite/deactivate/<slug:slug>/', views.ActivateDactivate, name=""),
    
]