# ChatGPT Demo Built with Django, Hotwire, Celery

This ChatGPT demo is built with Django, Hotwire, Celery and OpenAI API.

If you want to check more details, please check the [Tutorial Series: How to create ChatGPT-alike interface with Hotwire, Django and Celery](https://saashammer.com/blog/creating-chatgpt-interface-with-hotwire-django-celery/).

## Highlight Features

1. Streaming: With OpenAI streaming API call, the response is sent back incrementally in chunks via an event stream, so user do not need to wait seconds for long response.
2. Supports Markdown and code highlighting
4. The input box can autofocus and message list can auto scroll to display the new messages.
5. The input box height can auto grow with the content, so user can see the whole content when typing.
6. Press `Ctrl + Enter` to send message, without clicking the submit button

![demo gif](https://raw.githubusercontent.com/rails-inspire-django/chatgpt-django-project/main/example.gif)

## How to use

Add your OpenAI API key in `openai_factory.py`:

```bash
# build frontend assets, if you have no Node.js, please install it first
$ npm install
$ npm run build
```

```bash
# create python virtualenv
$ pip install requirements.txt
$ python manage.py migrate

# run django server
$ python manage.py runserver
```

```bash
# run celery worker
$ watchfiles --filter python 'celery -A chatgpt_django_app worker --loglevel=info'
```

Open [http://localhost:8000/chat/](http://localhost:8000/chat/), try to send message to the bot.
