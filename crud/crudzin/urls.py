from django.urls import path
from crudzin import views

app_name='crudzin'

urlpatterns = [
    path('school_list/', views.SchoolListView.as_view(), name='list'),
    path('school_list/<pk>/', views.SchoolDetailView.as_view(), name='detail'),
    path('create/', views.SchoolCreateView.as_view(), name="create"),
    path('update/<pk>/', views.SchoolUpdateView.as_view(), name = 'update'),
    path('delete/<pk>/', views.SchoolDeleteView.as_view(), name = 'delete'),
]