from django.urls import path
from phone_api import views


urlpatterns=[
    path('CompanyProducts/', views.CompanyListAPIView.as_view()), #List

    path('CompanyProducts/<str:company_id>/', views.CompanyRetDesAPIView.as_view()), #Retrive and Destroy

    path('CreateCompany/', views.CompanyCreateAPIView.as_view()), #Create Company

    path('<str:company_id>/CreateProduct/', views.ProductCreateApiView.as_view()),

    path('UpdateProduct/<str:product_id>/', views.ProductUpdateAPIView.as_view()), #Update Product
    
    path('DeleteProduct/<str:product_id>/', views.ProductDeleteAPIView.as_view()), #Delete Product

    path('PhoneRecharges/', views.RechargeCreateAPIView.as_view()), #Create Recharge
    
    path('PhoneRecharges/id/<int:pk>/', views.RechargeRetriveAPIView.as_view()), #Retrieve single Recharge

    path('PhoneRecharges/<str:phone_number>/', views.RechargeListAPIView.as_view()), #List Recharges

]