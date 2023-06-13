import json

from channels.generic.websocket import AsyncWebsocketConsumer, AsyncConsumer
from asgiref.sync import sync_to_async


from .models import Group, Message
from chat.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']
        datetime = data['datetime']


        await self.save_message(username, room, message)
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room': room,
                'datetime': datetime,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']
        datetime = event['datetime']
        
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room,
            'datetime': datetime,
        }))

    @sync_to_async
    def save_message(self, username, group, message):
        user = User.objects.get(username=username)
        group = Group.objects.get(slug=group)
        
        Message.objects.create(user=user, group=group, content=message)