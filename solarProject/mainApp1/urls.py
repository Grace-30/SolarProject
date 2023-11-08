from django.urls import path
from .import views
from .views import  ElectronicList, ElectronicsDetail, AddElectronicApp, ElectronicUpdate, ElectronicDelete
from django.contrib.auth import views as auth_views

urlpatterns=[
    
    path('',auth_views.LoginView.as_view(),name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('electronicdetail_list/',ElectronicList.as_view(), name='electronicdetails'),
     path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LoginView.as_view(),name='logout'),

    #Password
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),

   #Reset password
     path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
     path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
     path('reset/done',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

     #User Registration
     path('register/',views.register,name='register'),
     path('calculate/<int:pk>/',views.calculate,name='calculate'),

    #User Input
    
    path('appliance/<int:pk>/',ElectronicsDetail.as_view(),name='electronicdetail'),
    path('electronicdetail_form/',AddElectronicApp.as_view(), name='electronicdetail_form'),
    path('electronic-update/<int:pk>/', ElectronicUpdate.as_view(), name='electronic-update'),
    path('electronicdetail_delete/<int:pk>', ElectronicDelete.as_view(), name='electronicdetail_delete'),
]

