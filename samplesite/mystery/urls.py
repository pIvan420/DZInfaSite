from django.urls import path
from .views import mainpage, by_rubric, PhotoCreateView

urlpatterns = [
    path('', mainpage, name='index'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('add/', PhotoCreateView.as_view(), name='add')
]