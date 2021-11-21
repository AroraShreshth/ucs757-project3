from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as ml_views

urlpatterns = [
    path('dashboard/', ml_views.DashBoard.as_view(), name='dashboard-home'),
    path('dashboard/project1/list', ml_views.CallList.as_view(), name='dashboard-list'),
    path('dashboard/project1/<uuid:pk>/', ml_views.TriggerEmotion.as_view(), name='trigger-call'),
    path('dashboard/project1/<uuid:pk>/delete',
         ml_views.DeleteView.as_view(), name='dashboard-delete'),
    path('dashboard/project1/upload', ml_views.ImageUpload, name='dashboard-upload'),
]