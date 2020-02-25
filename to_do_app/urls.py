from django.urls import path
from django.conf import settings
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('home/', todoView, name='todohome'),
    path('to_do_add/', additems, name='to_do_add_new'),
    path('to_do_delete/<int:post_id>/', deleteitem, name='delete_item'),
    path('cross_off/<int:pk>/', cross_off, name='cross_off'),
    path('uncross/<int:pk>/', uncross, name='uncross'),

]

# if settings.DEBUG:
#     from django.conf.urls.static import static
#     # urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)