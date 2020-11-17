from managebook import views
from django.urls import path


urlpatterns = [
    path('list/<int:id>/', views.ListBook.as_view(), name='detail'),
    path('list/', views.ListBook.as_view(), name='list'),

]