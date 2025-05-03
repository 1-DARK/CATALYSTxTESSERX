from django.urls import path
from . import views

urlpatterns = [
    path('', views.query),
    path('pdf', views.PdfViewSet),
    path('verify-trxn', views.VerifyTxn)
]