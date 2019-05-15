from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = [
    # ex: /chores/
    path('', views.index, name='index'),
    # ex: /chores/5/
    path('<int:chore_id>/', views.detail, name='detail'),
    # ex: /chores/user/2/
    path('user/<int:user_id>/', views.user, name='user'),
    # ex: /chores/claim/5/
    path('claim/<int:user_id>/', views.claim, name='claim'),

]