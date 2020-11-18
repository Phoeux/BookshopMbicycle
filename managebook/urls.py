from managebook import views
from django.urls import path


urlpatterns = [
    path('list/', views.ListBook.as_view(), name='detail'),
    path('list/page=<int>/', views.ListBook.as_view(), name='page'), #if needed

]