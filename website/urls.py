from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='web'),
    path('work/', work, name='work'),
    path('work/category/<int:category_id>', work, name='category'),
    path('work/page/<int:page_number>', work, name='paginator'),
    path('work/<str:pk>', project_detail, name='project_detail'),
    path('about/', about, name='about'),
]
