from django.urls import path

from . import views

urlpatterns = [
    path("<item_id>", views.slot_list),
]
