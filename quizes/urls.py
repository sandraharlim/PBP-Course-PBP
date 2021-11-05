from django.urls import path
from .views import (
    QuizViewList,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
)

app_name = 'quizes'

urlpatterns = [
    path('', QuizViewList.as_view(), name='main-view'),
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
]