from django.urls import path
from phone_api import views


urlpatterns=[
    path('CompanyProducts/', views.CompanyList.as_view()),
    path('CompanyProducts/<str:company_id>/', views.CompanyDetail.as_view()),
    path('CreateProduct/<str:company_id>/', views.CreateProduct.as_view()), 
]