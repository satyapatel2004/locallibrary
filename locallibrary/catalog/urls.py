from django.urls import path 
from . import views 

#this is the URLConf module, specific URLS get sent to the appropriate views.  
#path methods also specifies the name of the specific mapping, so that it can be used to reverse
#the URL mapping, so we can dynamically reverse map the URL to point to the resource that 
#it points to. (use it in other parts of the application)

urlpatterns = [
    path('', views.index, name='index')

]