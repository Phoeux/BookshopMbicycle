from managebook import views
from django.urls import path


urlpatterns = [
    path('list/', views.ListBook.as_view(), name='detail'),
    path('list/page=<int>/', views.ListBook.as_view(), name='page'), #if needed
    path('authors/', views.ListAuthors.as_view(), name='authors'),
    path('buybook/', views.BoughtBooks.as_view(), name='buybook'),
    path('statall/', views.StatAll.as_view(), name='statuser'),

    path('monthlysold/', views.MonthlySoldBooks.as_view(), name='monthly_sold'),
    path('dumpbooks/', views.DumpBooks.as_view(), name='dumpbooks'),

    path('create/', views.CreateBook.as_view(), name='create_book'),

]