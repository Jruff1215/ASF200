from django.urls import path, include
from django.contrib import admin

#from ..contacts import views

add_name = "contact"

urlpatterns = [
    
   # path('', views.show_all_contacts ),
   # path('<int:contactid>',  views.show_contact ), 
     path('admin/', admin.site.urls),
     path('', include("contacts.urls"))   

]