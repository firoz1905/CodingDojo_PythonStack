from django.urls import path
from . import views

urlpatterns = [
    path('',views.reroute),
    path('shows',views.shows),
    path('new',views.new),
    path('create',views.create),
    path('shows/<int:show_id>',views.show,name="show_info"),
    path('shows/<int:show_id>/edit',views.edit,name="edit_show"),
    path('shows/<int:show_id>/destroy',views.delete,name="delete_show"),
]
