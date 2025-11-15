from django.urls import path
from . import views

urlpatterns = [
    path('', views.take_test, name='take_test'),
    path('save-result/', views.save_result, name='save_result'),
    path('my-results/', views.my_results, name='my_results'),
    path('test_instructions/', views.test_instructions, name='test_instructions'),
]