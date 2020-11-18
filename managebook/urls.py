from managebook import views
from django.urls import path


urlpatterns = [
    path('list/', views.ListBook.as_view(), name='detail'),
    path('list/page=<int>/', views.ListBook.as_view(), name='page'), #if needed
    path('authors/', views.ListAuthors.as_view(), name='authors'),
    path('statistic/', views.BoughtBooks.as_view(), name='statistics'),
    path('create/', views.CreateBook.as_view(), name='create_book')

]