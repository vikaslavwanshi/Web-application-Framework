from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    # path('<int:book_id>', views.post_detail),
    path('<int:post_id>', views.post_det)
]