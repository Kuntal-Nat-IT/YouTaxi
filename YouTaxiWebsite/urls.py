from django.urls import path
from .import views

urlpatterns = [
    path('demo/', views.DemoWebsite, name=""),
    path('create/driver/', views.CreateDriver, name=""),
    path('driver/login/', views.DriverLogin, name=""),
    path('driver/sent/otp/', views.DriverLoginOTPSystem, name=""),
    path('admin/login/', views.AdminLogin, name=""),
    path('get/driver/', views.GetAllDriver, name=""),
    path('get/driver/<slug:slug>/', views.GetDriverById, name=""),
    path('update/driver/<slug:slug>/', views.UpdateDriverById, name=""),
    path('get/user/', views.GetAllUser, name=""),
    path('get/user/<slug:slug>/', views.GetUser, name=""),
    path('search/user/<slug:slug>/', views.SearchUser, name=""),
    path('search/driver/<slug:slug>/', views.SearchDriver, name=""),
    path('search/company/<slug:slug>/', views.SearchCompany, name=""),
    path('search/payment-history/<slug:slug>/', views.SearchPaymentHistoryById, name=""),
    path('search/ride-history/<slug:slug>/', views.SearchRideHistoryById, name=""),
]