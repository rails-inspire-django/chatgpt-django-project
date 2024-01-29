from django.urls import path

from .views import (
    index_view,
    message_list_view,
    message_create_view,
)

app_name = "chat"

urlpatterns = [
    path("chat/", index_view, name="index"),
    path("chat/<int:chat_pk>/message/list/", message_list_view, name="message-list"),
    path("chat/<int:chat_pk>/message/create/", message_create_view, name="message-create"),
]
