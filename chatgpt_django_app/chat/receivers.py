from chatgpt_django_app.chat.tasks import task_ai_chat

from functools import partial
from django.db import transaction
from turbo_helper import after_create_commit, after_update_commit, dom_id
from turbo_helper.channels.broadcasts import broadcast_action_to

from .models import Message


@after_create_commit(sender=Message)
def create_message_content(sender, instance, created, **kwargs):
    broadcast_action_to(
        "chat",
        instance.chat_id,
        action="append",
        template="message_item.html",
        context={
            "instance": instance,
        },
        target=dom_id(instance.chat_id, "message_list"),
    )

    if instance.role == Message.USER:
        # for new user input, create reply message "Thinking..." and trigger celery task
        message_instance = Message.objects.create(
            role=Message.ASSISTANT,
            content="Thinking...",
            chat=instance.chat,
        )

        # call openai chat task in Celery worker
        transaction.on_commit(
            partial(
                task_ai_chat.delay,
                message_instance.pk,
            ),
        )


@after_update_commit(sender=Message)
def update_message_content(sender, instance, created, **kwargs):
    """
    When Celery worker update the message content, update the message div via Turbo Stream
    """
    broadcast_action_to(
        "chat",
        instance.chat_id,
        action="append",
        template="message_item.html",
        context={
            "instance": instance,
        },
        target=dom_id(instance.chat_id, "message_list"),
    )
