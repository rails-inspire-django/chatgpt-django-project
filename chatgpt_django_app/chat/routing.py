from django.urls import path

from actioncable import ActionCableConsumer, cable_channel_register
from turbo_helper.channels.streams_channel import TurboStreamCableChannel

cable_channel_register(TurboStreamCableChannel)


urlpatterns = [
    path("cable", ActionCableConsumer.as_asgi()),
]
