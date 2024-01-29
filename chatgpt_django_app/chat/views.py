from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from turbo_helper import turbo_stream

from .models import Chat, Message
from .forms import MessageForm


class IndexView(View):

    def get(self, request):
        # If no chat exists, create a new chat and redirect to the message list page.
        chat = Chat.objects.first()
        if not chat:
            chat = Chat.objects.create()
        return HttpResponseRedirect(reverse("chat:message-list", args=[chat.pk]))

    def post(self, request, *args, **kwargs):
        # create new chat object and redirect to message list view
        instance = Chat.objects.create()
        return HttpResponseRedirect(reverse("chat:message-list", args=[instance.pk]))


index_view = IndexView.as_view()


class MessageListView(ListView):
    model = Message
    template_name = "message_list_page.html"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(chat_id=self.kwargs["chat_pk"])
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["chats"] = Chat.objects.all()
        return context


message_list_view = MessageListView.as_view()


class MessageCreateView(CreateView):
    model = Message
    template_name = "message_create.html"
    form_class = MessageForm

    def get_success_url(self):
        return None

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["chat_pk"] = self.kwargs.get("chat_pk")
        kwargs["role"] = Message.USER
        return kwargs

    def get_empty_form(self):
        """
        Return empty form so we can reset the form
        """
        form_class = self.get_form_class()
        kwargs = self.get_form_kwargs()
        kwargs.pop("data")
        kwargs.pop("files")
        kwargs.pop("instance")
        return form_class(**kwargs)

    def form_valid(self, form):
        super().form_valid(form)

        return turbo_stream.response(
            turbo_stream.replace(
                "message_create",
                template=self.template_name,
                context={
                    "form": self.get_empty_form(),
                    "view": self,
                },
                request=self.request,
            ),
        )


message_create_view = MessageCreateView.as_view()
