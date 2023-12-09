from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('home/', views.html_index),
    path('date/', views.html_date),
    path('persons/', views.html_person),
    path('images/', views.html_image),
    path('images2/<str:imgvar>', views.html_image2),
    path('forms/', views.html_forms),
    path('forms_get/', views.html_forms_get, name = 'forms'),
    path('djangoforms/', views.django_forms),
]