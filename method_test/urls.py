from django.urls import path
from . import views


urlpatterns = [
    path('method_test/', views.post_test),
]
