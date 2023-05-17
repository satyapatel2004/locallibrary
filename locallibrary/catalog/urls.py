from django.urls import path 
from . import views 

#this is the URLConf module, specific URLS get sent to the appropriate views.  
#path methods also specifies the name of the specific mapping, so that it can be used to reverse
#the URL mapping, so we can dynamically reverse map the URL to point to the resource that 
#it points to. (use it in other parts of the application)

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),

    #we use the Url path with  <int:pk> to capture the 
    #book's id, which needs to be a specially formatted string
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]