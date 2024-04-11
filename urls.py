from django.urls import path

from portfolio.views import hi

urlpatterns = [
    path('',hi,name='hi')
]
