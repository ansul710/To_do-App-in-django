from django.urls import path
from .views import *

urlpatterns = [
    path('', todoView, name='todohome'),
    path('to_do_add/', additems, name='to_do_add_new'),
    path('to_do_delete/<int:post_id>/', deleteitem, name='delete_item'),

]
