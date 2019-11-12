from django.urls import path
from phone_api import views


urlpatterns=[
    path('company/', views.company_list),
    path('company/<str:company_id>', views.company_detail),
]