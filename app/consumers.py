import json

from channels import Group
from django.contrib.staticfiles.templatetags.staticfiles import static

from app.models import Nyanpasu

GROUP_NAME = 'nyanpasu'


def ws_connect(message):
    Group(GROUP_NAME).add(message.reply_channel)
    send_nyanpasu_count(message.reply_channel, 'にゃんぱすー', False)


def ws_receive(message):
    text = message['text']
    increment_count(text)
    send_nyanpasu_count(message.reply_channel, text)


def ws_disconnect(message):
    Group(GROUP_NAME).discard(message.reply_channel)


def send_nyanpasu_count(reply_channel, text, is_broadcast=True):
    nyanpasu = Nyanpasu.objects.filter(name=text)[:1]
    if nyanpasu:
        jdict = {'count': nyanpasu[0].count, 'mp3': static('nyanpasu.mp3')}
        send_data = {'text': '{0}'.format(json.dumps(jdict))}
    else:
        send_data = {'text': '*** {0} ***'.format(text)}
        is_broadcast = False

    if is_broadcast:
        Group(GROUP_NAME).send(send_data)
    else:
        reply_channel.send(send_data)


def increment_count(text):
    nyanpasu = Nyanpasu.objects.filter(name=text)[:1]
    if nyanpasu:
        nyanpasu[0].count += 1
        nyanpasu[0].save()
