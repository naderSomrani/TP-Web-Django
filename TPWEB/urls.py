from django.urls import path, include
from .views import *


urlpatterns = [
    path('customers/', CustomersAPI.as_view())
]
