from django.urls import path
from . import views

urlpatterns = [
    path('', views.take_test, name='take_test'),
    path('save-result/', views.save_result, name='save_result'),
    path('my-results/', views.my_results, name='my_results'),
    path('test_instructions/', views.test_instructions, name='test_instructions'),
    path("question-bank/", views.question_bank, name="question_bank"),
    path("question-bank/add/", views.add_question, name="add_question"),
    path("question-bank/edit/<int:pk>/", views.edit_question, name="edit_question"),
    path("question-bank/delete/<int:pk>/", views.delete_question, name="delete_question"),
]