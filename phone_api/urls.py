from django.urls import path
from phone_api import views


urlpatterns=[
    path('CompanyProducts/', views.CompanyListAPIView.as_view(), name='company-products'), #List

    path('CompanyProducts/<str:company_id>/', views.CompanyRetDesAPIView.as_view(), name='company-products-id'), #Retrive and Destroy

    path('CreateCompany/', views.CompanyCreateAPIView.as_view(), name='create-company'), #Create Company

    path('<str:company_id>/CreateProduct/', views.ProductCreateApiView.as_view(), name='str-create-product'),

    path('UpdateProduct/<str:product_id>/', views.ProductUpdateAPIView.as_view(), name='update-product'), #Update Product
    
    path('DeleteProduct/<str:product_id>/', views.ProductDeleteAPIView.as_view(), name='delete-product'), #Delete Product

    path('PhoneRecharges/', views.RechargeCreateAPIView.as_view(), name='phone-recharges'), #Create Recharge
    
    path('PhoneRecharges/id/<int:pk>/', views.RechargeRetriveAPIView.as_view(), name='phone-recharges-id'), #Retrieve single Recharge

    path('PhoneRecharges/<str:phone_number>/', views.RechargeListAPIView.as_view(), name='phone-recharges-str'), #List Recharges

]