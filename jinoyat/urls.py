from django.urls import path
from .views import  analyze_crime, crime_analysis_view


urlpatterns = [
     path('analyze_crime/', analyze_crime, name='analyze_crime'),  # Jinoyatni tahlil qilish uchun API endpointi
     path('', crime_analysis_view, name='crime_analysis'), 
]