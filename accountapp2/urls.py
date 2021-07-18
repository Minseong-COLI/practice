from django.urls import path
from accountapp2.views import hello_coli

app_name = 'accountapp2'

urlpatterns = [
    path('hello_coli/', hello_coli, name="hello_coli")
]