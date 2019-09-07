from django.urls import path
from thingsdone import views

urlpatterns = [
  path('', views.mainView, name='main'),
  path('days/', views.DayList.as_view(), name='days-list'),
  path('days/<int:pk>/', views.DayDetail, name='days-detail'),
  path('days/create/', views.DayCreate, name='days-create'),
  path('days/<int:pk>/edit/', views.DayEdit, name='days-edit'),
  path('days/<int:pk>/delete/', views.DayDelete.as_view(), name='days-delete'),  
  
  path('months/', views.MonthList.as_view(), name='months-list'),
  path('months/<int:pk>/', views.MonthDetail, name='months-detail'),
  path('months/create/', views.MonthCreate, name='months-create'),
  path('months/<int:pk>/edit/', views.MonthEdit, name='months-edit'),
  
  path('weeks/', views.WeekList.as_view(), name='weeks-list'),
  path('weeks/<int:pk>/', views.WeekDetail, name='weeks-detail'),
  path('weeks/create/', views.WeekCreate, name='weeks-create'),
  path('weeks/<int:pk>/edit/', views.WeekEdit, name='weeks-edit')
]