from django.db import models


class Chat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]


class Message(models.Model):
    SYSTEM = 0
    ASSISTANT = 10
    USER = 20
    ROLE_CHOICES = (
        (SYSTEM, "System"),
        (ASSISTANT, "Assistant"),
        (USER, "User"),
    )

    role = models.IntegerField(choices=ROLE_CHOICES)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    @property
    def role_label(self):
        role_label = self.get_role_display()
        return role_label

    @classmethod
    def for_openai(cls, messages):
        return [
            {"role": message.role_label.lower(), "content": message.content}
            for message in messages
        ]
