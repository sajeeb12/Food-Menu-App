from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('',views.index,name = 'index'),
    path('item',views.item, name = 'item'),
    path('<int:item_id>/',views.detail, name = 'detail'),
    # Add item
    path('add/',views.create_item,name = 'create_item'),
    # Update Item
    path('update/<int:id>/',views.update_item, name = 'update_item'),
    # delete Item
    path('delete/<int:id>/',views.delete_item, name = 'delete_item')
]
