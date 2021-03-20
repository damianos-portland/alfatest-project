
from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'applications'


urlpatterns = [
    path('', views.new_application,name='new_application'),
    path('all_applications/', views.all_applications, name="all_applications"),
    path('updateOrder/<str:pk>/', views.updateOrder, name='updateOrder'),
    path('newcustomer', views.newcustomer, name='newcustomer'),
    path('all_customers', views.all_customers, name='all_customers'),
    path('updateCustomer/<str:pk>/', views.updateCustomer, name='updateCustomer'),
    path('createXL/<str:pk>/', views.createXL, name='createXL'),
    path('ajax/load_trials/', views.load_trials, name='load_trials'),



    #path('', views.existed_applications,name='existed_applications'),



]
