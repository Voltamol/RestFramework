from django.urls import path
from .views import hello_world, create_item, update_item, delete_item

urlpatterns = [
    path('hello/', hello_world),
    path('create/', create_item),
    path('update/<int:item_id>/', update_item),
    path('delete/<int:item_id>/', delete_item),
]